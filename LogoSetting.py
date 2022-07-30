from os.path import exists

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QLabel

import SetupFile


# get values from file
def getValuesFromFile():
    # if the file doesn't exist, we make a file
    if not exists(SetupFile.LogoSetUpFilePath):
        file = open(SetupFile.LogoSetUpFilePath, "w")
        file.writelines("\n")
        file.writelines("0" + "\n")
        file.writelines("0" + "\n")
        file.writelines("0" + "\n")
        file.writelines("0")
        file.close()
    file = open(SetupFile.LogoSetUpFilePath, "r")
    FilePath = file.readline().strip()
    LogoSizeWidth = int(file.readline().strip())
    LogoSizeHeight = int(file.readline().strip())
    LogoPositionWidth = int(file.readline().strip())
    LogoPositionHeight = int(file.readline().strip())
    file.close()
    return FilePath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 400)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(660, 400))
        Form.setStyleSheet(SetupFile.MainBackground)

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.SelectLogoButton = QtWidgets.QPushButton(Form)
        self.SelectLogoButton.setStyleSheet(SetupFile.Button)
        self.SelectLogoButton.setObjectName("SelectLogoButton")
        self.horizontalLayout.addWidget(self.SelectLogoButton)

        self.FilePath = QtWidgets.QLabel(Form)
        self.FilePath.setMinimumSize(QtCore.QSize(300, 0))
        self.FilePath.setMaximumSize(QtCore.QSize(600, 30))
        self.FilePath.setStyleSheet(SetupFile.FilePath)
        self.FilePath.setText("")
        self.FilePath.setObjectName("FilePath")
        self.horizontalLayout.addWidget(self.FilePath)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.LogoSizeText = QtWidgets.QLabel(Form)
        self.LogoSizeText.setObjectName("LogoSizeText")

        self.horizontalLayout_5.addWidget(self.LogoSizeText)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.LogoSizeWidthText = QtWidgets.QLabel(Form)
        self.LogoSizeWidthText.setMaximumSize(QtCore.QSize(40, 40))
        self.LogoSizeWidthText.setObjectName("LogoSizeWidthText")
        self.horizontalLayout_3.addWidget(self.LogoSizeWidthText)

        self.LogoSizeWidth = QtWidgets.QSlider(Form)
        self.LogoSizeWidth.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoSizeWidth.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoSizeWidth.setStyleSheet(SetupFile.Slider)
        self.LogoSizeWidth.setOrientation(QtCore.Qt.Horizontal)
        self.LogoSizeWidth.setObjectName("LogoSizeWidth")
        self.horizontalLayout_3.addWidget(self.LogoSizeWidth)

        self.LogoSizeWidthBox = QtWidgets.QSpinBox(Form)
        self.LogoSizeWidthBox.setStyleSheet(SetupFile.SpinBox)
        self.LogoSizeWidthBox.setObjectName("LogoSizeWidthBox")

        self.horizontalLayout_3.addWidget(self.LogoSizeWidthBox)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.LogoSizeHeightText = QtWidgets.QLabel(Form)
        self.LogoSizeHeightText.setMaximumSize(QtCore.QSize(30, 30))
        self.LogoSizeHeightText.setObjectName("LogoSizeHeightText")
        self.horizontalLayout_4.addWidget(self.LogoSizeHeightText)

        self.LogoSizeHeight = QtWidgets.QSlider(Form)
        self.LogoSizeHeight.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoSizeHeight.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoSizeHeight.setStyleSheet(SetupFile.Slider)
        self.LogoSizeHeight.setOrientation(QtCore.Qt.Horizontal)
        self.LogoSizeHeight.setObjectName("LogoSizeHeight")
        self.horizontalLayout_4.addWidget(self.LogoSizeHeight)

        self.LogoSizeHeightBox = QtWidgets.QSpinBox(Form)
        self.LogoSizeHeightBox.setStyleSheet(SetupFile.SpinBox)
        self.LogoSizeHeightBox.setObjectName("LogoSizeHeightBox")
        self.horizontalLayout_4.addWidget(self.LogoSizeHeightBox)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.PreviewImage = QLabel(Form)
        self.PreviewImage.setObjectName(u"PreviewImage")
        self.PreviewImage.setMinimumSize(QSize(200, 200))
        self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)

        self.horizontalLayout_5.addWidget(self.PreviewImage)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.LogoPositionText = QtWidgets.QLabel(Form)
        self.LogoPositionText.setObjectName("LogoPositionText")
        self.horizontalLayout_6.addWidget(self.LogoPositionText)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem4)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.LogoPositionWidthText = QtWidgets.QLabel(Form)
        self.LogoPositionWidthText.setMaximumSize(QtCore.QSize(40, 40))
        self.LogoPositionWidthText.setObjectName("LogoPositionWidthText")
        self.horizontalLayout_7.addWidget(self.LogoPositionWidthText)

        self.LogoPositionWidth = QtWidgets.QSlider(Form)
        self.LogoPositionWidth.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoPositionWidth.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoPositionWidth.setStyleSheet(SetupFile.Slider)
        self.LogoPositionWidth.setOrientation(QtCore.Qt.Horizontal)
        self.LogoPositionWidth.setObjectName("LogoPositionWidth")
        self.horizontalLayout_7.addWidget(self.LogoPositionWidth)

        self.LogoPositionWidthBox = QtWidgets.QSpinBox(Form)
        self.LogoPositionWidthBox.setStyleSheet(SetupFile.SpinBox)
        self.LogoPositionWidthBox.setObjectName("LogoPositionWidthBox")
        self.horizontalLayout_7.addWidget(self.LogoPositionWidthBox)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.LogoPositionHeightText = QtWidgets.QLabel(Form)
        self.LogoPositionHeightText.setMaximumSize(QtCore.QSize(30, 30))
        self.LogoPositionHeightText.setObjectName("LogoPositionHeightText")
        self.horizontalLayout_8.addWidget(self.LogoPositionHeightText)

        self.LogoPositionHeight = QtWidgets.QSlider(Form)
        self.LogoPositionHeight.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoPositionHeight.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoPositionHeight.setStyleSheet(SetupFile.Slider)
        self.LogoPositionHeight.setOrientation(QtCore.Qt.Horizontal)
        self.LogoPositionHeight.setObjectName("LogoPositionHeight")
        self.horizontalLayout_8.addWidget(self.LogoPositionHeight)

        self.LogoPositionHeightBox = QtWidgets.QSpinBox(Form)
        self.LogoPositionHeightBox.setStyleSheet(SetupFile.SpinBox)
        self.LogoPositionHeightBox.setObjectName("LogoPositionHeightBox")
        self.horizontalLayout_8.addWidget(self.LogoPositionHeightBox)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.blank = QtWidgets.QLabel(Form)
        self.blank.setObjectName("blank")
        self.blank.setMinimumSize(QSize(200, 200))
        self.horizontalLayout_6.addWidget(self.blank)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)

        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(SetupFile.Button)
        self.horizontalLayout_2.addWidget(self.CloseButton)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet(SetupFile.Button)
        self.pushButton.setObjectName("CloseButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", SetupFile.LogoSettingPageTitle))
        self.SelectLogoButton.setText(_translate("Form", "Select Logo"))
        self.LogoSizeText.setText(_translate("Form", "Logo Size:      "))
        self.LogoSizeWidthText.setText(_translate("Form", "w%"))
        self.LogoSizeHeightText.setText(_translate("Form", "h%"))
        self.LogoPositionText.setText(_translate("Form", "Logo Position:"))
        self.LogoPositionWidthText.setText(_translate("Form", "w%"))
        self.LogoPositionHeightText.setText(_translate("Form", "h%"))
        self.CloseButton.setText(_translate("Form", "Close"))
        self.pushButton.setText(_translate("Form", "Apply Changes"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(SetupFile.MainIcon))
        self.setLimitsToComboBox(0, 100)
        self.setValuesFromFile()

        self.LogoSizeWidthBox.valueChanged.connect(self.AdjustLogoSizeWidthSlider)
        self.LogoSizeWidth.valueChanged.connect(self.AdjustLogoSizeWidthBox)

        self.LogoSizeHeightBox.valueChanged.connect(self.AdjustLogoSizeHeightSlider)
        self.LogoSizeHeight.valueChanged.connect(self.AdjustLogoSizeHeightBox)

        self.LogoPositionWidthBox.valueChanged.connect(self.AdjustLogoPositionWidthSlider)
        self.LogoPositionWidth.valueChanged.connect(self.AdjustLogoPositionWidthBox)

        self.LogoPositionHeightBox.valueChanged.connect(self.AdjustLogoPositionHeightSlider)
        self.LogoPositionHeight.valueChanged.connect(self.AdjustLogoPositionHeightBox)

        self.SelectLogoButton.clicked.connect(self.ImportLogo)
        self.pushButton.clicked.connect(self.ApplyChanges)
        self.CloseButton.clicked.connect(self.close)

    # Set values from file.
    def setValuesFromFile(self):
        FilePath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth = getValuesFromFile()

        self.FilePath.setText(FilePath)
        self.LogoSizeWidthBox.setValue(LogoSizeWidth)
        self.LogoSizeWidth.setValue(LogoSizeWidth)
        self.LogoSizeHeightBox.setValue(LogoSizeHeight)
        self.LogoSizeHeight.setValue(LogoSizeHeight)
        self.LogoPositionWidthBox.setValue(LogoPositionWidth)
        self.LogoPositionWidth.setValue(LogoPositionWidth)
        self.LogoPositionHeightBox.setValue(LogoPositionHeight)
        self.LogoPositionHeight.setValue(LogoPositionHeight)
        self.PreviewImage.setStyleSheet(
            "QLabel{border: 1px solid;image: url(" + FilePath + ");background-color: "
                                                                "gray;}")

    # save input from ui to file
    # when called by the main file it also updates the screen.
    def ApplyChanges(self):
        if not len(self.FilePath.text()) == 0:
            file = open(SetupFile.LogoSetUpFilePath, "w")
            file.writelines(self.FilePath.text() + "\n")
            file.writelines(str(self.LogoSizeWidthBox.value()) + "\n")
            file.writelines(str(self.LogoSizeHeightBox.value()) + "\n")
            file.writelines(str(self.LogoPositionWidthBox.value()) + "\n")
            file.writelines(str(self.LogoPositionHeightBox.value()))
            file.close()

    # Import logo and add it to logo previewer.
    def ImportLogo(self):
        filename = QFileDialog.getOpenFileName(self, 'Logo',
                                               'Logo', "Logo(*.png);;Logo(*.jpeg);;Logo(*.jpg)")
        path = filename[0]
        if not len(path) == 0:
            self.FilePath.setText(path)
            self.PreviewImage.setStyleSheet(
                "QLabel{border: 1px solid;image: url(" + self.FilePath.text() + ");background-color: "
                                                                                "gray;}")

    # adjust slider according to box
    def AdjustLogoSizeWidthSlider(self):
        self.LogoSizeWidth.setValue(self.LogoSizeWidthBox.value())

    # adjust box according to slider
    def AdjustLogoSizeWidthBox(self):
        self.LogoSizeWidthBox.setValue(self.LogoSizeWidth.value())

    # adjust slider according to box
    def AdjustLogoSizeHeightSlider(self):
        self.LogoSizeHeight.setValue(self.LogoSizeHeightBox.value())

    # adjust box according to slider
    def AdjustLogoSizeHeightBox(self):
        self.LogoSizeHeightBox.setValue(self.LogoSizeHeight.value())

    # adjust slider according to box
    def AdjustLogoPositionWidthSlider(self):
        self.LogoPositionWidth.setValue(self.LogoPositionWidthBox.value())

    # adjust box according to slider
    def AdjustLogoPositionWidthBox(self):
        self.LogoPositionWidthBox.setValue(self.LogoPositionWidth.value())

    # adjust slider according to box
    def AdjustLogoPositionHeightSlider(self):
        self.LogoPositionHeight.setValue(self.LogoPositionHeightBox.value())

    # adjust box according to slider
    def AdjustLogoPositionHeightBox(self):
        self.LogoPositionHeightBox.setValue(self.LogoPositionHeight.value())

    # set max and min limits to spinbox and slider
    def setLimitsToComboBox(self, Minimum, Maximum):
        self.LogoSizeWidthBox.setMinimum(Minimum)
        self.LogoSizeWidthBox.setMaximum(Maximum)

        self.LogoSizeWidth.setMinimum(Minimum)
        self.LogoSizeWidth.setMaximum(Maximum)

        self.LogoSizeHeightBox.setMinimum(Minimum)
        self.LogoSizeHeightBox.setMaximum(Maximum)

        self.LogoSizeHeight.setMinimum(Minimum)
        self.LogoSizeHeight.setMaximum(Maximum)

        self.LogoPositionWidthBox.setMinimum(Minimum)
        self.LogoPositionWidthBox.setMaximum(Maximum)

        self.LogoPositionWidth.setMinimum(Minimum)
        self.LogoPositionWidth.setMaximum(Maximum)

        self.LogoPositionHeightBox.setMinimum(Minimum)
        self.LogoPositionHeightBox.setMaximum(Maximum)

        self.LogoPositionHeight.setMinimum(Minimum)
        self.LogoPositionHeight.setMaximum(Maximum)
