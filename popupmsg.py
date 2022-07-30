from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon

import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Form.setObjectName("Form")
        Form.resize(350, 105)
        Form.setMinimumSize(QtCore.QSize(350, 105))
        Form.setMaximumSize(QtCore.QSize(660, 400))

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Icon = QtWidgets.QLabel(Form)
        self.Icon.setMinimumSize(QtCore.QSize(50, 50))
        self.Icon.setMaximumSize(QtCore.QSize(50, 50))
        self.Icon.setObjectName("Icon")
        self.horizontalLayout.addWidget(self.Icon)

        self.Text = QtWidgets.QLabel(Form)
        self.Text.setText("")
        self.Text.setObjectName("Text")
        self.horizontalLayout.addWidget(self.Text)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.clicked.connect(self.close)
        self.horizontalLayout_3.addWidget(self.CloseButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseButton.setText(_translate("Form", "Close"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(SetupFile.MainIcon))
        self.setStyleSheet(SetupFile.MainBackground)
        self.CloseButton.setStyleSheet(SetupFile.Button)
        self.Icon.setStyleSheet(SetupFile.WarningImage)
        self.setMessage("File not found")
        self.setTitle("Warning")

    # Method to set message for the pop-up message.
    def setMessage(self, Message):
        self.Text.setText(Message)

    # Method to set title for the pop-up message.
    def setTitle(self, Title):
        self.setWindowTitle(Title)
