import os
from os import walk
from os.path import exists
import ctypes
from PIL import Image
from PIL.Image import Resampling
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QSemaphore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QApplication

import ExploringFilePopUp
import ImageSettingPage
import LogoSetting
import ProgressBar
import SetupFile
import popupmsg

PhotoFiles = []
trial = []
NumberOfPhotos = 0
total = 0
Close = False
sem = QSemaphore(1)


# checks if required folder is present, if it isn't present, it makes the folder.
def FolderPresentEnsured(Folder):
    if not exists(Folder):
        os.mkdir(Folder)


# checks if logo is transparent or not.
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


# save the new combined single image.
def SaveNewImage():
    if exists(SetupFile.SavedPathWithLogo):
        img1 = Image.open(SetupFile.SavedPathWithLogo)
        if has_transparency(img1):
            savedFile, check = QFileDialog.getSaveFileName(None, "Save Image",
                                                           "Output", "Image(*.png)")
        else:
            savedFile, check = QFileDialog.getSaveFileName(None, "Save Image",
                                                           "Output", "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
        if check:
            img1.save(savedFile)
            os.startfile(savedFile)


# add logo to the image if logo is present, otherwise just resize the image.
def AddLogo(OriginalImage):
    LogoPath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth = LogoSetting.getValuesFromFile()
    resizeImage(OriginalImage)
    Background = Image.open(SetupFile.SavedPathWithResize)
    if has_transparency(Background):
        Background.convert("RGBA")
    else:
        Background.convert("RGB")
    BackgroundWidth = Background.size[0]
    BackgroundHeight = Background.size[1]
    try:
        Logo = Image.open(LogoPath.strip())
        if has_transparency(Logo):
            Logo.convert("RGBA")
        else:
            Logo.convert("RGB")
        # resize on the scale of the background
        Logo = Logo.resize(
            (int((LogoSizeWidth / 100) * BackgroundWidth), int((LogoSizeHeight / 100) * BackgroundHeight)))
        LogoWidth = Logo.size[0]
        LogoHeight = Logo.size[1]

        maxWidth = BackgroundWidth - LogoWidth
        maxHeight = BackgroundHeight - LogoHeight

        # set position of logo on the scale of the background
        if has_transparency(Logo):
            Background.paste(Logo,
                             (int((LogoPositionWidth / 100) * maxWidth),
                              int((LogoPositionHeight / 100) * maxHeight)),
                             Logo)
        else:
            Background.paste(Logo,
                             (int((LogoPositionWidth / 100) * maxWidth),
                              int((LogoPositionHeight / 100) * maxHeight)))
    except:
        None
    Background.save(SetupFile.SavedPathWithLogo)


# method to resize original image.
def resizeImage(originalImagePath):
    img = Image.open(originalImagePath)
    file = open(SetupFile.ImageSetupFilePath, "r")
    RadioButtonFlagText = file.readline().strip()
    if RadioButtonFlagText == "True":
        RadioButtonChecked = True
    else:
        RadioButtonChecked = False
    ComboBoxCurrentIndex = int(file.readline().strip())
    ImageWidth = int(file.readline().strip())
    ImageHeight = int(file.readline().strip())
    file.close()
    if not RadioButtonChecked:
        if ComboBoxCurrentIndex == 0:
            img = img.resize((1280, 720), Resampling.LANCZOS)
        if ComboBoxCurrentIndex == 1:
            img = img.resize((1920, 1080), Resampling.LANCZOS)
        if ComboBoxCurrentIndex == 2:
            img = img.resize((2560, 1440), Resampling.LANCZOS)
        if ComboBoxCurrentIndex == 3:
            img = img.resize((3840, 2160), Resampling.LANCZOS)
        if ComboBoxCurrentIndex == 4:
            img = img.resize((ImageWidth, ImageHeight), Resampling.LANCZOS)
    img.save(SetupFile.SavedPathWithResize)


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        # Folder and file checks.
        FolderPresentEnsured(SetupFile.ProgramFilesFolder)
        FolderPresentEnsured(SetupFile.ResourceFolder)
        FolderPresentEnsured(SetupFile.OutputFolder)
        FolderPresentEnsured(SetupFile.LogoFolder)
        ImageSettingPage.FilePresentEnsured()

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

        self.LogoSetting = QtWidgets.QAction(MainWindow)
        self.LogoSetting.setObjectName("LogoSetting")
        self.menuFile.addAction(self.LogoSetting)
        self.menubar.addAction(self.menuFile.menuAction())

        self.ImageSetting = QtWidgets.QAction(MainWindow)
        self.ImageSetting.setObjectName("ImageSetting")
        self.menuFile.addAction(self.ImageSetting)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logo-Adder"))
        self.ImportImageButton.setText(_translate("MainWindow", "Import Image"))
        self.ConvertButton.setText(_translate("MainWindow", "Convert"))
        self.menuFile.setTitle(_translate("MainWindow", SetupFile.MenuTitle_Setting))
        self.LogoSetting.setText(_translate("MainWindow", SetupFile.LogoSettingPageTitle))
        self.ImageSetting.setText(_translate("MainWindow", SetupFile.ImageSettingPageTitle))


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowIcon(QIcon(SetupFile.MainIcon))
        self.ImportImageButton.clicked.connect(self.ImportImage)
        self.ConvertButton.clicked.connect(self.Save)
        self.LogoSetting.triggered.connect(self.openLogoSetting)
        self.ImageSetting.triggered.connect(self.openImageSetting)

    # save multiple combined photos in a folder.
    def SaveMultipleImages(self):
        ProgressBar = self.getProgressBar()
        ProgressBar.StopButton.clicked.connect(self.Close)
        ProgressBar.progressBar.setValue(0)
        global NumberOfPhotos
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not len(directory) == 0:
            ProgressBar.setDirectory(directory)
            self.ConvertButton.setEnabled(False)
            ProgressBar.show()

            # start a thread and move the worker to it.
            self.my_thread = QThread()
            self.worker = Worker(directory, self.FilePath.text(), NumberOfPhotos)

            # We're connecting things to the correct spots
            self.worker.moveToThread(self.my_thread)  # move worker to thread.
            # Note: Ui elements should only be updated via the main thread.
            self.worker.progressbarParameters.connect(ProgressBar.updateProgressBar)  # using signal and slots,
            # update ui elements
            self.my_thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.my_thread.quit)  # safely close the thread.
            self.worker.finished.connect(self.worker.deleteLater)
            self.my_thread.finished.connect(self.finishThread)

            self.my_thread.start()

    # Once the thread finishes, safely close the thread and enable convert button for use again.
    def finishThread(self):
        self.ConvertButton.setEnabled(True)
        self.my_thread.deleteLater()

    # Use of semaphore so that there is no race condition.
    def Close(self):
        sem.acquire(1)
        global Close
        Close = True
        sem.release()

    # check if it is to save a single image or multiple images.
    def Save(self):
        name, extension = os.path.splitext(self.FilePath.text())
        if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
            SaveNewImage()
        else:
            global NumberOfPhotos
            if not NumberOfPhotos == 0:
                self.SaveMultipleImages()
            else:
                self.openPopUpWindow("No images found in the folder!")

    # Open the test model MainWindow
    def openLogoSetting(self):
        self.window = QtWidgets.QMainWindow()
        self.window = LogoSetting.MyWindow()
        self.window.show()
        self.window.pushButton.clicked.connect(self.CheckAndUpdate)

    # Open the test model MainWindow
    def openImageSetting(self):
        self.window = QtWidgets.QMainWindow()
        self.window = ImageSettingPage.MyWindow()
        self.window.show()
        self.window.pushButton.clicked.connect(self.CheckAndUpdate)

    # Update only if there is a file path, this is to ensure update doesn't occur without the required files.
    def CheckAndUpdate(self):
        if not len(self.FilePath.text()) == 0:
            self.updateSingleImageView()

    # Open the pop-up MainWindow.
    def openPopUpWindow(self, message):
        self.window = QtWidgets.QMainWindow()
        self.window = popupmsg.MyWindow()
        self.window.setMessage(message)
        self.window.show()

    def getExploringFilePopUp(self):
        self.a = QtWidgets.QMainWindow()
        self.a = ExploringFilePopUp.MyWindow()
        return self.a

    # function to get the progress bar object.
    def getProgressBar(self):
        self.ProgressBar = QtWidgets.QMainWindow()
        self.ProgressBar = ProgressBar.MyWindow()
        return self.ProgressBar

    # update the main screen with original image and preview of the combined image.
    def update(self):
        name, extension = os.path.splitext(self.FilePath.text())
        if extension.upper() == "":
            self.updateMultipleFileView()
        else:
            self.updateSingleImageView()

    def updateMultipleFileView(self):
        ExploringFilePopUp1 = self.getExploringFilePopUp()
        name, extension = os.path.splitext(self.FilePath.text())
        if extension == "":
            dir_path = self.FilePath.text()
            # add to thread
            # start a thread and move the worker to it.
            self.my_thread = QThread()
            self.worker = Worker1(dir_path)

            # We're connecting things to the correct spots
            self.worker.moveToThread(self.my_thread)  # move worker to thread.
            # Note: Ui elements should only be updated via the main thread.
            self.worker.TotalFiles.connect(ExploringFilePopUp1.setMessage)  # using signal and slots,
            # update ui elements
            self.my_thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.my_thread.quit)  # safely close the thread.
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finishedAllFiles.connect(self.finished)
            self.my_thread.finished.connect(self.finishThread)
            self.worker.SystemDriveTriedtoAccess.connect(self.WarnUser)
            self.worker.SystemDriveTriedtoAccess.connect(ExploringFilePopUp1.closeWindow)

            self.my_thread.start()
            # end of thread

    def WarnUser(self, SystemDriveTriedtoAccess):
        if SystemDriveTriedtoAccess:
            self.ClearScreen()
            self.openPopUpWindow("Restricted Access")

    def finished(self):
        global NumberOfPhotos
        self.OriginalImage.setText("Loaded from folder")
        self.OriginalImage.setAlignment(Qt.AlignCenter)
        self.OriginalImage.setStyleSheet(SetupFile.EmptyImage)
        self.PreviewImage.setText("No preview for folder\n Number of Images in folder : " + str(NumberOfPhotos))
        self.PreviewImage.setAlignment(Qt.AlignCenter)
        self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)

    def updateSingleImageView(self):
        name, extension = os.path.splitext(self.FilePath.text())
        if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
            if not len(self.FilePath.text()) == 0:
                self.OriginalImage.setText("")
                self.PreviewImage.setText("")
                self.OriginalImage.setStyleSheet("QLabel{\n"
                                                 "    border: 1px solid;\n"
                                                 "    image: url(" + self.FilePath.text() + ");\n"
                                                                                            "background-color: gray;\n "
                                                                                            "     }\n"
                                                                                            "")
                AddLogo(self.FilePath.text())
                self.PreviewImage.setStyleSheet(SetupFile.PreviewImage)

    # Open file dialog to import image
    def ImportImage(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Import Image',
                                                   'Image', "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
            path = filename[0]
            self.FilePath.setText(path)
            if not len(path) == 0:
                self.updateSingleImageView()
        except:
            None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.ConvertButton.setEnabled(True)
        FilePath = [u.toLocalFile() for u in event.mimeData().urls()]
        try:
            for f in FilePath:
                name, extension = os.path.splitext(f)
                if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG" or extension.upper() == "":
                    self.FilePath.setText(f)
                    self.update()
                else:
                    self.ClearScreen()
                    self.openPopUpWindow("Please drop a folder or file")
        except:
            None

    def ClearScreen(self):
        self.OriginalImage.setStyleSheet(SetupFile.EmptyImage)
        self.OriginalImage.setText("")
        self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)
        self.PreviewImage.setText("")
        self.FilePath.setText("")
        self.ConvertButton.setEnabled(False)

    # when user closes the main MainWindow, remove temp files and close all other sub windows.
    def closeEvent(self, event):
        if exists(SetupFile.SavedPathWithLogo):
            os.remove(SetupFile.SavedPathWithLogo)
        if exists(SetupFile.SavedPathWithResize):
            os.remove(SetupFile.SavedPathWithResize)
        for window in QApplication.topLevelWidgets():
            window.close()


class Worker(QObject):
    progressbarParameters = pyqtSignal(int, int, name="ProgressBarParameters")
    finished = pyqtSignal()

    def __init__(self, directory, FilePath, TotalNumberOfPhotos):
        super(Worker, self).__init__()
        self.directory = directory
        self.FilePath = FilePath
        self.NumberOfPhotos = TotalNumberOfPhotos

    def run(self):
        sem.acquire(1)
        global Close
        Close = False
        CurrentNumberOfPhotos = 0
        for (dir_path, dir_names, file_names) in walk(self.FilePath):
            for file in file_names:
                if Close:
                    break
                else:
                    sem.release(1)
                    name, extension = os.path.splitext(file)
                    if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                        AddLogo(os.path.join(dir_path, file))
                        CurrentNumberOfPhotos = CurrentNumberOfPhotos + 1
                        self.progressbarParameters.emit(CurrentNumberOfPhotos, NumberOfPhotos)
                        img1 = Image.open(SetupFile.SavedPathWithLogo)
                        img1.save(self.directory + "/" + file)
        self.finished.emit()


class Worker1(QObject):
    TotalFiles = pyqtSignal(int, name="TotalFiles")
    SystemDriveTriedtoAccess = pyqtSignal(bool)
    finished = pyqtSignal()
    finishedAllFiles = pyqtSignal()

    def __init__(self, directory):
        super(Worker1, self).__init__()
        self.directory = directory

    def run(self):
        if self.directory == str(os.getenv("SystemDrive")) + "/":
            self.SystemDriveTriedtoAccess.emit(True)
        else:
            self.SystemDriveTriedtoAccess.emit(False)
            print(self.directory)
            global NumberOfPhotos
            NumberOfPhotos = 0
            global PhotoFiles
            for (dir_path, dir_names, file_names) in walk(self.directory):
                for file in file_names:
                    name, extension = os.path.splitext(file)
                    if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                        NumberOfPhotos = NumberOfPhotos + 1
                        self.TotalFiles.emit(NumberOfPhotos)
            self.finishedAllFiles.emit()
        self.finished.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
