import zmq
import logging
from logging import NullHandler
import socket
from multiprocessing import Process
from czpurifier.middleware import SimulatorInterface, DeviceInterface
from os import chdir, path, kill, getpid
from signal import signal, SIGQUIT, SIGCONT, SIGUSR1, SIGTERM, SIGUSR2
from json import load
from run_purification import RunPurification
from run_custom_protocol import RunCustomProtol
from PyQt5.QtWidgets import QMessageBox

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class GUI_Controller:
    def __init__(self):
        """
        1. Controls the communication between device and controller interface and the GUI
        2. Contains all common methods between the different GUI windows
        3. Controls all access to external file reads i.e. JSON file for default parameters
        """
        logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
        self.device_process = None
        self.device_present = False
        self.controller_ip = 'pure2.local'
        self.controller_interface_PID = None
        self.ctrl_proc = None
        chdir(path.dirname(path.realpath(__file__)))
        with open('purifier.log', 'w') as f:
            f.close()
        with open('purification_parameters.json', 'r') as f:
            self._p = load(f)
        self.default_param = [self._p['NUM_COL']['default'], self._p['COL_VOLUME']['default'],
                            self._p['EQUILIBRATE_VOLUME']['default'], self._p['LOAD_VOLUME']['default'],
                            self._p['WASH_VOLUME']['default'], self._p['ELUTE_VOLUME']['default']]

    def connect_to_device(self):
        """Try to bind to device ip and check if a connection is already there"""
        self.device_present = False
        #self.controller_ip = 'pure2.local'
        #self.device_present = True
        return self.device_present
        
    def connect_to_simulator(self):
        """Connect to the simulator by opening a pub/sub connection at local ip"""
        self.device_process = Process(target=self._connect_simulator)
        self.device_process.daemon = True
        self.device_process.start()
        self.controller_ip = '127.0.0.1'

    def _connect_simulator(self):
        """Method run in the new process generated to connect to the simulator"""
        si = SimulatorInterface()
        si.autorun()
    
    def run_purification_script(self, is_basic_purification, parameters, fractions):
        """
        Run the purification protocal on a new process
        If the protocol is run on the simulator a signal is sent to the simulator
        to be the device and pass the 'device is available check' on the controller
        """
        targ = RunPurification if is_basic_purification else RunCustomProtol
        if not self.device_present:
            kill(self.device_process.pid, SIGUSR1)
        self.ctrl_proc = Process(target=targ, args=(parameters, fractions, self.controller_ip, getpid(),))
        self.ctrl_proc.daemon = True
        self.ctrl_proc.start()
        self.controller_interface_PID = self.ctrl_proc.pid

    def pause_clicked(self):
        """Sends SIGQUIT signal to raise pause flag if pause is clicked"""
        kill(self.controller_interface_PID, SIGQUIT)
    
    def hold_clicked(self):
        """Sends SIGUSR1 signal to raise hold flag if hold is clicked"""
        kill(self.controller_interface_PID, SIGUSR1)
    
    def resume_clicked(self):
        """Sends SIGCONT signal to resume from pause/hold if resume is clicked"""
        kill(self.controller_interface_PID, SIGCONT)
    
    def skip_clicked(self):
        """Sends SIGUSR2 signal to raise skip flag if skip is clicked"""
        kill(self.controller_interface_PID, SIGUSR2)

    def stop_clicked(self):
        """Sends SIGTERM signal to disconnect controller interface"""
        self._needs_connection = False
        kill(self.controller_interface_PID, SIGTERM)
        self.ctrl_proc.join()

    def calc_step_times(self, parameters, fractions):
        """Calculates an estimate time for each step"""
        stage_moving_time = 10
        pump_vol_times = 60
        step_times = []
        i = 2
        for f in fractions:
            pump_total = parameters[i]*pump_vol_times
            if f is None:
                stage_total = 0
            else:
                stage_total = len(f)*stage_moving_time
            step_times.append(pump_total+stage_total)
            i +=2
        return step_times

    def areYouSureMsg(self, action):
        """Confirms whether or not the user meant to click an action button"""
        msg = QMessageBox()
        msg.setText('Are you sure you want to {}'.format(action))
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self._msgbtn)
        msg.exec()
    
    def _msgbtn(self, i):
        """Returns the result from the are you sure pop up"""
        self.is_sure = True if 'ok' in i.text().lower() else False

if __name__ == "__main__":
    t = GUI_Controller()
    t.connect_to_device()