from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QIcon

import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Form.setObjectName("Form")
        Form.setMinimumSize(QtCore.QSize(398, 118))
        Form.setMaximumSize(QtCore.QSize(450, 150))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Message = QtWidgets.QLabel(Form)
        self.Message.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Message.setObjectName("Message")
        self.Message.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.Message)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Processing..."))
        self.Message.setText(_translate("Form", "Hang in tight! Processing..."))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(SetupFile.MainIcon))
        self.setStyleSheet(SetupFile.MainBackground)
        self.Message.setStyleSheet(SetupFile.FilePath)

    # Close pop up window.
    def Close(self):
        self.close()

