from PyQt5 import QtCore, QtGui, QtWidgets
from purification_gui import Ui_Purification
from custom_protocol import Ui_CustomProtocol
from calib_protocol import Ui_CalibrationProtocol
from gui_controller import GUI_Controller
import sys
from time import sleep
from multiprocessing import set_start_method

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        """
        The initialization for the Main Window that is run 
        upon opening the GUI
        """
        self.gui_controller = GUI_Controller()
        self.setupUi(MainWindow)
        self.initEvents()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.p3_expected = QtWidgets.QLabel(self.centralwidget)
        self.p3_expected.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.p3_expected.setObjectName("p3_expected")
        self.gridLayout_2.addWidget(self.p3_expected, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 4)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 7, 2, 1, 1)
        self.p1_expected = QtWidgets.QLabel(self.centralwidget)
        self.p1_expected.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.p1_expected.setObjectName("p1_expected")
        self.gridLayout_2.addWidget(self.p1_expected, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 2, 1, 1)
        self.p4_actual = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p4_actual.sizePolicy().hasHeightForWidth())
        self.p4_actual.setSizePolicy(sizePolicy)
        self.p4_actual.setObjectName("p4_actual")
        self.gridLayout_2.addWidget(self.p4_actual, 8, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)
        self.p2_actual = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2_actual.sizePolicy().hasHeightForWidth())
        self.p2_actual.setSizePolicy(sizePolicy)
        self.p2_actual.setObjectName("p2_actual")
        self.gridLayout_2.addWidget(self.p2_actual, 6, 3, 1, 1)
        self.run_calib_prot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_calib_prot_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.run_calib_prot_btn.setFont(font)
        self.run_calib_prot_btn.setObjectName("run_calib_prot_btn")
        self.gridLayout_2.addWidget(self.run_calib_prot_btn, 3, 0, 1, 4)
        self.p1_actual = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1_actual.sizePolicy().hasHeightForWidth())
        self.p1_actual.setSizePolicy(sizePolicy)
        self.p1_actual.setObjectName("p1_actual")
        self.gridLayout_2.addWidget(self.p1_actual, 5, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 4, 9, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)
        self.p2_expected = QtWidgets.QLabel(self.centralwidget)
        self.p2_expected.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.p2_expected.setObjectName("p2_expected")
        self.gridLayout_2.addWidget(self.p2_expected, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.p4_expected = QtWidgets.QLabel(self.centralwidget)
        self.p4_expected.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.p4_expected.setObjectName("p4_expected")
        self.gridLayout_2.addWidget(self.p4_expected, 8, 1, 1, 1)
        self.p3_actual = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3_actual.sizePolicy().hasHeightForWidth())
        self.p3_actual.setSizePolicy(sizePolicy)
        self.p3_actual.setObjectName("p3_actual")
        self.gridLayout_2.addWidget(self.p3_actual, 7, 3, 1, 1)
        self.columnsize_combo = QtWidgets.QComboBox(self.centralwidget)
        self.columnsize_combo.setObjectName("columnsize_combo")
        self.columnsize_combo.addItem("")
        self.columnsize_combo.addItem("")
        self.gridLayout_2.addWidget(self.columnsize_combo, 2, 1, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 4, 0, 1, 4)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.purification_btn = QtWidgets.QPushButton(self.centralwidget)
        self.purification_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.purification_btn.setFont(font)
        self.purification_btn.setObjectName("purification_btn")
        self.verticalLayout.addWidget(self.purification_btn)
        self.otherscripts_btn = QtWidgets.QPushButton(self.centralwidget)
        self.otherscripts_btn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.otherscripts_btn.setFont(font)
        self.otherscripts_btn.setObjectName("otherscripts_btn")
        self.verticalLayout.addWidget(self.otherscripts_btn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_sim_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.run_sim_btn.setFont(font)
        self.run_sim_btn.setObjectName("run_sim_btn")
        self.horizontalLayout_3.addWidget(self.run_sim_btn)
        spacerItem = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setMinimumSize(QtCore.QSize(10, 0))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_3.addWidget(self.close_btn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Protein Purifier"))
        self.p3_expected.setText(_translate("MainWindow", "10"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>The flow rate needs to be calibrated for each column</p><p><span style=\" font-weight:600;\">Calibration Factor = Expected Volume/Actual Volume</span></p><p>Please run the calibration protocol to calculate the factor</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "/"))
        self.p1_expected.setText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "Pump 3"))
        self.label_9.setText(_translate("MainWindow", "/"))
        self.label_10.setText(_translate("MainWindow", "/"))
        self.label_4.setText(_translate("MainWindow", "Pump 1"))
        self.label_12.setText(_translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "Column Calibration"))
        self.run_calib_prot_btn.setText(_translate("MainWindow", "Run Calibration Protocol"))
        self.label_5.setText(_translate("MainWindow", "Pump 2"))
        self.p2_expected.setText(_translate("MainWindow", "10"))
        self.label_7.setText(_translate("MainWindow", "Pump 4"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Column Size:</span></p></body></html>"))
        self.p4_expected.setText(_translate("MainWindow", "10"))
        self.columnsize_combo.setItemText(0, _translate("MainWindow", "1 mL"))
        self.columnsize_combo.setItemText(1, _translate("MainWindow", "5 mL"))
        self.label_2.setText(_translate("MainWindow", "Choose Procedure"))
        self.purification_btn.setText(_translate("MainWindow", "Basic Purification"))
        self.otherscripts_btn.setText(_translate("MainWindow", "Custom Protocol"))
        self.run_sim_btn.setText(_translate("MainWindow", "Run Simulation Mode"))
        self.close_btn.setText(_translate("MainWindow", "Close"))

    def initEvents(self):
        """Initialize all buttons"""
        self.run_calib_prot_btn.clicked.connect(self.onClick_calib_protocol)
        self.purification_btn.clicked.connect(self.onClick_purification_btn)
        self.otherscripts_btn.clicked.connect(self.onClick_otherscripts_btn)
        self.close_btn.clicked.connect(self.onClick_close_btn)
        self.run_sim_btn.clicked.connect(self.onClick_sim_btn)
        self.columnsize_combo.activated.connect(self.onSelect_columnSize)

        self.update_calib_disp(self.gui_controller.actualvol1mL, 10)
        self.columnsize = '1mL'

    def update_calib_disp(self, actual_val, expected_val):
        """Update the expected and actual values for the flow volume"""
        self.p1_actual.setText('{}'.format(actual_val[0]))
        self.p2_actual.setText('{}'.format(actual_val[1]))
        self.p3_actual.setText('{}'.format(actual_val[2]))
        self.p4_actual.setText('{}'.format(actual_val[3]))

        self.p1_expected.setText('{}'.format(expected_val))
        self.p2_expected.setText('{}'.format(expected_val))
        self.p3_expected.setText('{}'.format(expected_val))
        self.p4_expected.setText('{}'.format(expected_val))

    def onSelect_columnSize(self):
        """Update the default parameter display based on the column size selected"""
        if self.columnsize_combo.currentIndex() == 0:
            self.columnsize = '1mL'
            actual_val = self.gui_controller.actualvol1mL
            expected_val = 10
        else:
            self.columnsize = '5mL'
            actual_val = self.gui_controller.actualvol5mL
            expected_val = 25
        
        self.update_calib_disp(actual_val, expected_val)

    def onClick_calib_protocol(self):
        self.calib = QtWidgets.QMainWindow()
        self.calib_ui = Ui_CalibrationProtocol(self.calib, self.columnsize)
        self.calib.show()

    def onClick_sim_btn(self):
        self.confirm_connectSim()
        if self.is_sure:
            self.is_sure = None
            self.run_sim()
            self.run_sim_btn.setEnabled(False)
    
    def confirm_connectSim(self):
        """Confirms whether or not the user meant to click an action button"""
        msg = QtWidgets.QMessageBox()
        msg.setText('Are you sure you want to run the simulator mode?')
        msg.setInformativeText('If you are connected to the simulator mode and would like to '
        'switch back to the hardware please close the software and rerun it.\n\n'
        'Click Ok to start simulator')
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self._msgbtn)
        msg.exec()
    
    def _msgbtn(self, i):
        """Returns the result from the are you sure pop up"""
        self.is_sure = True if 'ok' in i.text().lower() else False

    def run_sim(self):
        """
        Call the method to run the simulator if 'run simulator' is clicked
        on the connect to device pop up
        """
        self.gui_controller.connect_to_simulator()
        msg = QtWidgets.QMessageBox()
        msg.setText('Running Simulator')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec()
    
    def onClick_purification_btn(self):
        """
        Opens the purification window 
        """
        self.purifier = QtWidgets.QMainWindow()
        self.purifier_ui = Ui_Purification(self.purifier, self.gui_controller.device_process, self.columnsize, self.percolumncalib())
        self.purifier.show()

    def onClick_otherscripts_btn(self):
        """
        Opens the other scripts window
        """
        self.oth_sc_window = QtWidgets.QMainWindow()
        self.oth_sc_ui = Ui_CustomProtocol(self.oth_sc_window, self.gui_controller.device_process)
        self.oth_sc_window.show() 
    
    def onClick_close_btn(self):
        """
        Closes the GUI
        """
        quit()

    def percolumncalib(self):
        """Create the list of per column calibration factor based on the input values in the GUI"""
        expected = 10 if self.columnsize == '1mL' else 25
        percolumn = []
        percolumn.append(expected/float(self.p1_actual.text()))
        percolumn.append(expected/float(self.p2_actual.text()))
        percolumn.append(expected/float(self.p3_actual.text()))
        percolumn.append(expected/float(self.p4_actual.text()))

        return percolumn       

if __name__ == "__main__":
    import sys
    set_start_method('spawn')
    app = QtWidgets.QApplication(sys.argv)
    # Timeout the QEvent to allow for signals to be caught
    timer = QtCore.QTimer()
    timer.start(1000)
    timer.timeout.connect(lambda : None)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())