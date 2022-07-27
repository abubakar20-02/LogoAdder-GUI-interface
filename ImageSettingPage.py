from os.path import exists

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 242)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(660, 400))
        Form.setStyleSheet(SetupFile.MainBackground)
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
        self.comboBox.setStyleSheet(SetupFile.ComboBox)
        self.horizontalLayout_11.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ImageSizeText = QtWidgets.QLabel(Form)
        self.ImageSizeText.setObjectName("ImageSizeText")
        self.horizontalLayout_5.addWidget(self.ImageSizeText)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ImageSizeWidthText = QtWidgets.QLabel(Form)
        self.ImageSizeWidthText.setMaximumSize(QtCore.QSize(30, 30))
        self.ImageSizeWidthText.setObjectName("ImageSizeWidthText")
        self.horizontalLayout_3.addWidget(self.ImageSizeWidthText)
        self.ImageWidth = QtWidgets.QSpinBox(Form)
        self.ImageWidth.setObjectName("ImageWidth")
        self.ImageWidth.setMinimumWidth(60)
        self.ImageWidth.setMinimum(100)
        self.ImageWidth.setMaximum(10000)
        self.horizontalLayout_3.addWidget(self.ImageWidth)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ImageSizeHeightText = QtWidgets.QLabel(Form)
        self.ImageSizeHeightText.setMaximumSize(QtCore.QSize(30, 30))
        self.ImageSizeHeightText.setObjectName("ImageSizeHeightText")
        self.horizontalLayout_4.addWidget(self.ImageSizeHeightText)
        self.ImageHeight = QtWidgets.QSpinBox(Form)
        self.ImageHeight.setObjectName("ImageHeight")
        self.ImageHeight.setMinimumWidth(60)
        self.ImageHeight.setMinimum(100)
        self.ImageHeight.setMaximum(10000)
        self.horizontalLayout_4.addWidget(self.ImageHeight)
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
        self.pushButton.setStyleSheet(SetupFile.Button)
        self.pushButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
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
        self.ImageSizeText.setText(_translate("Form", "Image Size:      "))
        self.ImageSizeWidthText.setText(_translate("Form", "w:"))
        self.ImageSizeHeightText.setText(_translate("Form", "h:"))
        self.pushButton.setText(_translate("Form", "Apply Changes"))


def FilePresentEnsured():
    if not exists(SetupFile.ImageSetupFilePath):
        method_name(True, 0, 100, 100)


def method_name(RadioButton, ComboBoxIndex, ImageWidth, ImageHeight):
    file = open(SetupFile.ImageSetupFilePath, "w")
    file.write(str(RadioButton) + "\n")
    file.write(str(ComboBoxIndex) + "\n")
    file.write(str(ImageWidth) + "\n")
    file.write(str(ImageHeight) + "\n")
    file.close()


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(SetupFile.ImageSettingPageTitle)
        self.setWindowIcon(QIcon(SetupFile.MainIcon))
        FilePresentEnsured()
        self.method()
        self.ImageWidth.setStyleSheet(SetupFile.SpinBox)
        self.ImageHeight.setStyleSheet(SetupFile.SpinBox)

        self.radioButton.clicked.connect(self.checkRadio)
        self.comboBox.currentIndexChanged.connect(self.checkCombo)
        self.pushButton.clicked.connect(self.ApplyChanges)

    def method(self):
        file = open(SetupFile.ImageSetupFilePath, "r")
        RadioButtonFlagText = file.readline().strip()
        if RadioButtonFlagText == "True":
            Flag = True
        else:
            Flag = False

        self.radioButton.setChecked(Flag)
        self.comboBox.setCurrentIndex(int(file.readline().strip()))
        self.ImageWidth.setValue(int(file.readline().strip()))
        self.ImageHeight.setValue(int(file.readline().strip()))
        file.close()
        self.checkRadio()

    def ApplyChanges(self):
        print("apply changes")
        method_name(self.radioButton.isChecked(), self.comboBox.currentIndex(), self.ImageWidth.value(),
                    self.ImageHeight.value())

        print(self.radioButton.isChecked())
        print(self.comboBox.currentIndex())
        print(self.ImageWidth.value())
        print(self.ImageHeight.value())
        self.close()

    def checkRadio(self):
        print(self.radioButton.isChecked())
        if self.radioButton.isChecked():
            print("block everything below")
            self.EnableButtons(False)
        else:
            print("Enable everything below")
            self.EnableButtons(True)
        self.checkCombo()

    def checkCombo(self):
        print(self.comboBox.currentText())
        if (not self.radioButton.isChecked()) and self.comboBox.currentIndex() == 4:
            self.EnableImageSize(True)
        else:
            self.EnableImageSize(False)

    def EnableButtons(self, Boolean):
        self.comboBox.setEnabled(Boolean)
        self.label.setEnabled(Boolean)

    def EnableImageSize(self, Boolean):
        self.ImageSizeHeightText.setEnabled(Boolean)
        self.ImageSizeWidthText.setEnabled(Boolean)
        self.ImageSizeText.setEnabled(Boolean)
        self.ImageWidth.setEnabled(Boolean)
        self.ImageHeight.setEnabled(Boolean)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
