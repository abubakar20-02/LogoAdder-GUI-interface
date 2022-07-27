from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
import ConversionCompletePopUp
import SetupFile


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(363, 80)
        Form.setWindowTitle("Converting...")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowIcon(QIcon(SetupFile.MainIcon))

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.StopButton = QtWidgets.QPushButton(Form)
        self.StopButton.setObjectName("StopButton")
        self.StopButton.setText("Stop")
        self.horizontalLayout.addWidget(self.StopButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        QtCore.QMetaObject.connectSlotsByName(Form)


class MyWindow(QtWidgets.QWidget, Ui_Form):
    directory = ""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(SetupFile.MainBackground)
        self.StopButton.setStyleSheet(SetupFile.Button)
        self.StopButton.clicked.connect(self.ClosedinBetween)

    # Method to update progress bar.
    def updateProgressBar(self, current, Max):
        self.progressBar.setValue((current / Max) * 100)
        if self.progressBar.value() == 100:
            self.openConversionCompletePopUp()
            self.close()

    # Open Pop up.
    def openConversionCompletePopUp(self):
        self.window = QtWidgets.QMainWindow()
        self.window = ConversionCompletePopUp.MyWindow()
        self.window.setMessage("Conversion complete!")
        self.window.setDirectory(self.directory)
        self.window.show()

    # Open Pop up.
    def ClosedinBetween(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        self.window = ConversionCompletePopUp.MyWindow()
        self.window.setWindowTitle("Conversion stopped")
        self.window.setMessage("Conversion stopped at the given file!")
        self.window.setDirectory(self.directory)
        self.window.show()

    # Method to set directory.
    def setDirectory(self, directory):
        self.directory = directory


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
