from PyQt5 import QtCore, QtGui, QtWidgets
from purification import Ui_Purification
from other_scripts import Ui_OtherScripts
import sys
from time import sleep


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        """
        The initialization for the Main Window that is run 
        upon opening the GUI
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 10))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.connect_device_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_device_btn.setMinimumSize(QtCore.QSize(0, 100))
        self.connect_device_btn.setObjectName("connect_device_btn")
        self.connect_device_btn.clicked.connect(self.onClick_connect_device)
        self.verticalLayout_2.addWidget(self.connect_device_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.purification_btn = QtWidgets.QPushButton(self.centralwidget)
        self.purification_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.purification_btn.setObjectName("purification_btn")
        self.purification_btn.clicked.connect(self.onClick_purification_btn)
        self.verticalLayout.addWidget(self.purification_btn)
        self.otherscripts_btn = QtWidgets.QPushButton(self.centralwidget)
        self.otherscripts_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.otherscripts_btn.setObjectName("otherscripts_btn")
        self.verticalLayout.addWidget(self.otherscripts_btn)
        self.otherscripts_btn.clicked.connect(self.onClick_otherscripts_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 22))
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
        self.label.setText(_translate("MainWindow", "Step 1: Establish Connection"))
        self.connect_device_btn.setText(_translate("MainWindow", "Connect To Device"))
        self.label_2.setText(_translate("MainWindow", "Step 2: Choose Procedure"))
        self.purification_btn.setText(_translate("MainWindow", "Basic Purification"))
        self.otherscripts_btn.setText(_translate("MainWindow", "Other Scripts"))

    def onClick_connect_device(self):
        self.connect_device_btn.setEnabled(False)
        self.connect_hardware = QtWidgets.QPushButton('Connect To Protein Purifier')
        self.run_simulator = QtWidgets.QPushButton('Run Simulation Mode')
        self.connect_hardware.clicked.connect(self.onClickConnect_hardware)
        self.run_simulator.clicked.connect(self.onClickRunSim)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.addButton(self.connect_hardware, QtWidgets.QMessageBox.NoRole)
        msg.addButton(self.run_simulator, QtWidgets.QMessageBox.NoRole)
        msg.exec()

    def onClickConnect_hardware(self):
        print('connection made')
    
    def onClickRunSim(self):
        print('running simulator')
    
    def onClick_purification_btn(self):
        self.purifier = QtWidgets.QMainWindow()
        self.purifier_ui = Ui_Purification(self.purifier)
        self.purifier.show()

    def onClick_otherscripts_btn(self):
        self.oth_sc_window = QtWidgets.QMainWindow()
        self.oth_sc_ui = Ui_OtherScripts(self.oth_sc_window)
        self.oth_sc_window.show() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
