"""Interfaces between communication layer and psuedo hardware (used for testing)"""
import logging
from time import sleep
from czpurifier.middleware import DeviceInterface
from czpurifier.hardware import HardwareController 
from logging import NullHandler
from signal import signal, SIGUSR1, SIGTERM, getsignal
from os import kill, getpid

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

class SimulatorInterface(DeviceInterface):
    """Device interface of protein purifier.
    """
    def __init__(self, ip_address='127.0.0.1', timeout_recv=1):
        super().__init__(ip_address, timeout_recv)
        self._ip_addr = ip_address
        signal(SIGUSR1, self._fake_socket_availability)
        self._SIGTERM_default = getsignal(SIGTERM)
        signal(SIGTERM, self._close_connection)
    
    def _fake_socket_availability(self, signalNumber, frame):
        """Fake device is up for the controller interface availability check"""
        for _ in range(5):
            sleep(1)
            self.socket_availability.send_pyobj('')
    
    def _close_connection(self, signalNumber, frame):
        """Close the connection when the GUI is closed"""
        self.socket_data_in.disconnect("tcp://" + self._ip_addr + ":5100")
        self.socket_data_out.disconnect("tcp://" + self._ip_addr + ":5200")
        self.socket_availability.disconnect("tcp://" + self._ip_addr + ":5000")
        signal(SIGTERM, self._SIGTERM_default)
        kill(getpid(), SIGTERM)
        
    def loadConfig(self, config_mode: str):
        """Update command list with settings defined in config file.

        Parameters
        ----------
        config_mode : str
            Configuration option listed in config file.
        """
        Hardware = HardwareController(self.hardware_config_file, config_mode, True)
        self.cmd_dict.update({'reportFracCollectorPositions': Hardware.reportFracCollectorPositions,
                              'moveFracCollector': Hardware.moveFracCollector,
                              'homeFracCollector': Hardware.homeFracCollector,
                              'setInputValves': Hardware.setInputValves,
                              'setWasteValves': Hardware.setWasteValves,
                              'getInputValves': Hardware.getInputValves,
                              'getWasteValves': Hardware.getWasteValves,
                              'reportRotaryPorts': Hardware.reportRotaryPorts,
                              'getCurrentPort': Hardware.getCurrentPort,
                              'renameRotaryPort': Hardware.renameRotaryPort,
                              'moveRotaryValve': Hardware.moveRotaryValve,
                              'homeRotaryValve': Hardware.homeRotaryValve,
                              'getPumpStatus': Hardware.getPumpStatus,
                              'getFlowRate': Hardware.getFlowRate,
                              'setFlowRate': Hardware.setFlowRate,
                              'startPumping': Hardware.startPumping,
                              'stopPumping': Hardware.stopPumping,
                              'getFractionDuration': Hardware.getFractionDuration,
                              })

if __name__ == "__main__":
    #current_address = socket.gethostbyname(socket.getfqdn() + '.local')
    logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
    si = SimulatorInterface()
    si.autorun()