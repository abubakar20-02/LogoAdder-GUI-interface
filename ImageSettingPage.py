from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 242)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(660, 400))
        Form.setStyleSheet("background-color: rgb(255, 241, 171)")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TextForRadioButton = QtWidgets.QLabel(Form)
        self.TextForRadioButton.setObjectName("TextForRadioButton")
        self.horizontalLayout.addWidget(self.TextForRadioButton)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setEditable(False)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_3.setStyleSheet("QDoubleSpinBox{\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 1px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color:black;\n"
                                           "    color: solid black;\n"
                                           "    background-color: white;\n"
                                           "    }")
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_4.setStyleSheet("QDoubleSpinBox{\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 1px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color:black;\n"
                                           "    background-color: white;\n"
                                           "    color: solid black;\n"
                                           "    }")
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(107, 0, 0);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 1px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color:white;\n"
                                      "    color: rgb(255, 241, 171);\n"
                                      "    font: bold 12px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    color: white;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TextForRadioButton.setText(_translate("Form", "Use original image resolution:"))
        self.label.setText(_translate("Form", "Image resolution:"))
        self.comboBox.setCurrentText(_translate("Form", "1280 x 720 HD"))
        self.comboBox.setItemText(0, _translate("Form", "1280 x 720 HD"))
        self.comboBox.setItemText(1, _translate("Form", "1920 x 1080 FHD"))
        self.comboBox.setItemText(2, _translate("Form", "2560 x 1440 2K"))
        self.comboBox.setItemText(3, _translate("Form", "3840 x 2160 4K"))
        self.comboBox.setItemText(4, _translate("Form", "Custom"))
        self.label_5.setText(_translate("Form", "Image Size:      "))
        self.label_3.setText(_translate("Form", "w%"))
        self.label_4.setText(_translate("Form", "h%"))
        self.pushButton.setText(_translate("Form", "Apply Changes"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.clicked.connect(self.checkRadio)
        self.comboBox.currentIndexChanged.connect(self.checkCombo)

    def checkRadio(self):
        print(self.radioButton.isChecked())

    def checkCombo(self):
        print(self.comboBox.currentText())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
