# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desgin_files/single_step.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# WARNING!! Manual change made to the file


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StepWidget(object):
    def setupUi(self, StepWidget):
        StepWidget.setObjectName("StepWidget")
        StepWidget.resize(530, 300)
        self.layoutWidget = StepWidget  # the widget object passed needs to be set to this widget
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 506, 266))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.valve_inp_lbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valve_inp_lbl.setFont(font)
        self.valve_inp_lbl.setObjectName("valve_inp_lbl")
        self.gridLayout_3.addWidget(self.valve_inp_lbl, 1, 0, 1, 1)
        self.port_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.port_lbl.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_lbl.setFont(font)
        self.port_lbl.setObjectName("port_lbl")
        self.gridLayout_3.addWidget(self.port_lbl, 2, 0, 1, 1)
        self.vol_lbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vol_lbl.setFont(font)
        self.vol_lbl.setObjectName("vol_lbl")
        self.gridLayout_3.addWidget(self.vol_lbl, 3, 0, 1, 1)
        self.flowpath_lbl = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.flowpath_lbl.setFont(font)
        self.flowpath_lbl.setObjectName("flowpath_lbl")
        self.gridLayout_3.addWidget(self.flowpath_lbl, 4, 0, 1, 1)
        self.flowpath_combo_box = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.flowpath_combo_box.setFont(font)
        self.flowpath_combo_box.setObjectName("flowpath_combo_box")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.flowpath_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.flowpath_combo_box, 4, 1, 1, 1)
        self.volume_slider = QtWidgets.QSlider(self.layoutWidget)
        self.volume_slider.setMaximum(200)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.gridLayout_3.addWidget(self.volume_slider, 3, 1, 1, 1)
        self.valve_inp_combo_box = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valve_inp_combo_box.setFont(font)
        self.valve_inp_combo_box.setObjectName("valve_inp_combo_box")
        self.valve_inp_combo_box.addItem("")
        self.valve_inp_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.valve_inp_combo_box, 1, 1, 1, 1)
        self.port_combo_box = QtWidgets.QComboBox(self.layoutWidget)
        self.port_combo_box.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_combo_box.setFont(font)
        self.port_combo_box.setObjectName("port_combo_box")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.port_combo_box.addItem("")
        self.gridLayout_3.addWidget(self.port_combo_box, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 3)
        self.volume_val_lbl = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_val_lbl.sizePolicy().hasHeightForWidth())
        self.volume_val_lbl.setSizePolicy(sizePolicy)
        self.volume_val_lbl.setMaximumSize(QtCore.QSize(60, 16777215))
        self.volume_val_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.volume_val_lbl.setObjectName("volume_val_lbl")
        self.gridLayout_3.addWidget(self.volume_val_lbl, 3, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 5, 1, 1, 3)
        self.step_num = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.step_num.setFont(font)
        self.step_num.setAlignment(QtCore.Qt.AlignCenter)
        self.step_num.setObjectName("step_num")
        self.gridLayout_3.addWidget(self.step_num, 0, 0, 1, 1)

        self.retranslateUi(StepWidget)
        QtCore.QMetaObject.connectSlotsByName(StepWidget)

    def retranslateUi(self, StepWidget):
        _translate = QtCore.QCoreApplication.translate
        StepWidget.setWindowTitle(_translate("StepWidget", "Single Step"))
        self.valve_inp_lbl.setText(_translate("StepWidget", "Valve Input:"))
        self.port_lbl.setText(_translate("StepWidget", "Port:"))
        self.vol_lbl.setText(_translate("StepWidget", "Total Volume:"))
        self.flowpath_lbl.setText(_translate("StepWidget", "Flow Path:"))
        self.flowpath_combo_box.setItemText(0, _translate("StepWidget", "Pre Column Waste"))
        self.flowpath_combo_box.setItemText(1, _translate("StepWidget", "Post Column Waste"))
        self.flowpath_combo_box.setItemText(2, _translate("StepWidget", "Fraction Column"))
        self.flowpath_combo_box.setItemText(3, _translate("StepWidget", "Flow Through Column"))
        self.valve_inp_combo_box.setItemText(0, _translate("StepWidget", "Load"))
        self.valve_inp_combo_box.setItemText(1, _translate("StepWidget", "Buffer"))
        self.port_combo_box.setItemText(0, _translate("StepWidget", "Wash"))
        self.port_combo_box.setItemText(1, _translate("StepWidget", "Load Buffer"))
        self.port_combo_box.setItemText(2, _translate("StepWidget", "Elution"))
        self.port_combo_box.setItemText(3, _translate("StepWidget", "Base"))
        self.label_2.setText(_translate("StepWidget", "ml"))
        self.volume_val_lbl.setInputMask(_translate("StepWidget", "9999"))
        self.volume_val_lbl.setText(_translate("StepWidget", "2"))
        self.step_num.setText(_translate("StepWidget", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StepWidget = QtWidgets.QWidget()
    ui = Ui_StepWidget()
    ui.setupUi(StepWidget)
    StepWidget.show()
    sys.exit(app.exec_())
