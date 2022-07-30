from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject

import LogoAdder
import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMinimumSize(QtCore.QSize(350, 76))
        Form.setMaximumSize(QtCore.QSize(400, 100))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Message = QtWidgets.QLabel(Form)
        self.Message.setObjectName("Message")
        self.Message.setMinimumSize(QtCore.QSize(60, 20))
        self.verticalLayout.addWidget(self.Message)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CancelButton = QtWidgets.QPushButton(Form)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Finding images files..."))
        self.Message.setText(_translate("Form", "TextLabel"))
        self.CancelButton.setText(_translate("Form", "Cancel"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(SetupFile.MainBackground)
        self.CancelButton.setStyleSheet(SetupFile.Button)
        self.Message.setStyleSheet(SetupFile.FilePath)
        self.setMessage(0)

    def setMessage(self, NumberOfImages):
        message = " Found " + str(NumberOfImages) + " image files"
        self.Message.setText(message)

    def closeWindow(self, SystemDriveTriedtoAccess):
        print(SystemDriveTriedtoAccess)
        if not SystemDriveTriedtoAccess:
            self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
