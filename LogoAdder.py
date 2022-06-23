import os
from os.path import exists

from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog

import LogoSetting
import SetupFile


def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


def AddLogo(OriginalImage):
    LogoPath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth = LogoSetting.getValuesFromFile()
    print(SetupFile.SavedPath)
    # Opening the primary image (used in background)
    print(LogoPath)
    img1 = Image.open(OriginalImage)
    img1Width = img1.size[0]
    img1Height = img1.size[1]
    print(img1Width, img1Height)
    # Opening the secondary image (overlay image)
    img2 = Image.open(LogoPath.strip())
    # w h
    img2 = img2.resize((int((LogoSizeWidth / 100) * img1Width), int((LogoSizeHeight / 100) * img1Height)))
    img2Width = img2.size[0]
    img2Height = img2.size[1]
    print(img2Width, img2Height)

    maxWidth = img1Width - img2Width
    maxHeight = img1Height - img2Height

    # Pasting img2 image on top of img1
    # starting at coordinates (0, 0)
    if has_transparency(img2):
        img1.paste(img2, (int((LogoPositionWidth / 100) * maxWidth), int((LogoPositionHeight / 100) * maxHeight)), img2)
    else:
        img1.paste(img2,(int((LogoPositionWidth / 100) * maxWidth), int((LogoPositionHeight / 100) * maxHeight)))

    img1.save(SetupFile.SavedPath)


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 542)
        MainWindow.setStyleSheet(SetupFile.MainBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.MainGrid = QtWidgets.QGridLayout()
        self.MainGrid.setObjectName("MainGrid")
        self.Images = QtWidgets.QHBoxLayout()

        self.Images.setContentsMargins(10, 10, 10, 10)
        self.Images.setSpacing(50)
        self.Images.setObjectName("Images")

        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImage.setMinimumSize(QtCore.QSize(300, 375))
        self.OriginalImage.setAcceptDrops(True)
        self.OriginalImage.setStyleSheet(SetupFile.EmptyImage)
        self.OriginalImage.setText("")
        self.OriginalImage.setObjectName("OriginalImage")

        self.Images.addWidget(self.OriginalImage)

        self.PreviewImage = QtWidgets.QLabel(self.centralwidget)
        self.PreviewImage.setMinimumSize(QtCore.QSize(300, 375))
        self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)
        self.PreviewImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PreviewImage.setText("")
        self.PreviewImage.setObjectName("PreviewImage")
        self.Images.addWidget(self.PreviewImage)
        self.MainGrid.addLayout(self.Images, 1, 0, 1, 1)

        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setContentsMargins(10, 20, -1, -1)
        self.InputLayout.setSpacing(10)
        self.InputLayout.setObjectName("InputLayout")
        self.ImportImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.ImportImageButton.setStyleSheet(SetupFile.Button)
        self.ImportImageButton.setObjectName("ImportImageButton")
        self.InputLayout.addWidget(self.ImportImageButton)
        self.FilePath = QtWidgets.QLabel(self.centralwidget)
        self.FilePath.setMinimumSize(QtCore.QSize(400, 0))
        self.FilePath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.FilePath.setStyleSheet(SetupFile.FilePath)
        self.FilePath.setObjectName("FilePath")
        self.InputLayout.addWidget(self.FilePath)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputLayout.addItem(spacerItem)
        self.MainGrid.addLayout(self.InputLayout, 0, 0, 1, 1)
        self.ConvertGrid = QtWidgets.QHBoxLayout()
        self.ConvertGrid.setContentsMargins(-1, -1, 10, -1)
        self.ConvertGrid.setObjectName("ConvertGrid")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ConvertGrid.addItem(spacerItem1)
        self.ConvertButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConvertButton.setStyleSheet(SetupFile.Button)
        self.ConvertButton.setObjectName("ConvertButton")
        self.ConvertGrid.addWidget(self.ConvertButton)
        self.MainGrid.addLayout(self.ConvertGrid, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.MainGrid)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet(SetupFile.MenuBar)

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImportImageButton.setText(_translate("MainWindow", "Import Image"))
        self.ConvertButton.setText(_translate("MainWindow", "Convert"))
        self.menuFile.setTitle(_translate("MainWindow", "User"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))


def SaveNewImage():
    if exists(SetupFile.SavedPath):
        PDFfile, check = QFileDialog.getSaveFileName(None, "Save Image",
                                                     "Image", "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
        if check:
            img1 = Image.open(SetupFile.SavedPath)
            img1.save(PDFfile)
            os.startfile(PDFfile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.ImportImageButton.clicked.connect(self.ImportData)
        self.ConvertButton.clicked.connect(SaveNewImage)
        self.actionSettings.triggered.connect(self.openLogoSetting)

    # Open the test model window
    def openLogoSetting(self):
        self.window = QtWidgets.QMainWindow()
        self.window = LogoSetting.MyWindow()
        self.window.show()
        self.window.pushButton.clicked.connect(self.update)

    def update(self):
        if not len(self.FilePath.text()) == 0:
            AddLogo(self.FilePath.text())
            self.OriginalImage.setStyleSheet("QLabel{\n"
                                             "    border: 1px solid;\n"
                                             "    image: url(" + self.FilePath.text() + ");\n"
                                                                                        "    background-color: gray;\n"
                                                                                        "     }\n"
                                                                                        "")
            AddLogo(self.FilePath.text())
            self.PreviewImage.setStyleSheet(SetupFile.PreviewImage)

    # Open file dialog to import data
    def ImportData(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Import Image',
                                                   'Image', "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
            path = filename[0]
            print(path)
            self.FilePath.setText(path)
            self.update()
        except:
            None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        FilePath = event.mimeData().urls()[0].toLocalFile()
        try:
            self.FilePath.setText(FilePath)
            self.update()
        except:
            print("didnt work")

    def closeEvent(self, event):
        if exists("saved.SetupFile.SavedPath"):
            os.remove("SetupFile.SavedPath.png")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
