import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject

import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(386, 114)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setMaximumSize(QtCore.QSize(50, 50))
        self.Image.setObjectName("Image")
        self.horizontalLayout_2.addWidget(self.Image)
        self.Text = QtWidgets.QLabel(Form)
        self.Text.setObjectName("Text")
        self.horizontalLayout_2.addWidget(self.Text)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CloseButton = QtWidgets.QPushButton(Form)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton)
        self.OpenFolderButton = QtWidgets.QPushButton(Form)
        self.OpenFolderButton.setObjectName("OpenFolderButton")
        self.horizontalLayout.addWidget(self.OpenFolderButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Text.setText(_translate("Form", "TextLabel"))
        self.CloseButton.setText(_translate("Form", "Close"))
        self.OpenFolderButton.setText(_translate("Form", "Open Folder"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    directory = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Conversion complete")
        self.setStyleSheet(SetupFile.MainBackground)
        self.Image.setStyleSheet(SetupFile.CompleteImage)
        self.CloseButton.setStyleSheet(SetupFile.Button)
        self.OpenFolderButton.setStyleSheet(SetupFile.Button)

        self.Text.setText("Conversion complete!")
        self.CloseButton.clicked.connect(self.close)
        self.OpenFolderButton.clicked.connect(self.openDirectory)

    def setDirectory(self, directory):
        self.directory = directory

    def openDirectory(self):
        self.close()
        os.startfile(self.directory)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
