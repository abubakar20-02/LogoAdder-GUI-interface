import os
import time
from functools import partial
from os import walk
from os.path import exists

from PIL import Image
from PIL.Image import Resampling
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, Qt, QThread, QSemaphore, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QApplication

import ImageSettingPage
import LogoSetting
import ProgressBar
import SetupFile
import popupmsg

PhotoFiles = []
trial = []
NumberOfPhotos = 0
total = 0


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
        savedFile, check = QFileDialog.getSaveFileName(None, "Save Image",
                                                       "Output", "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
        if check:
            img1 = Image.open(SetupFile.SavedPathWithLogo)
            img1.save(savedFile)
            os.startfile(savedFile)


# add logo to the image.
def AddLogo(OriginalImage):
    try:
        LogoPath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth = LogoSetting.getValuesFromFile()
        resizeImage(OriginalImage)
        Background = Image.open(SetupFile.SavedPathWithResize)
        BackgroundWidth = Background.size[0]
        BackgroundHeight = Background.size[1]

        if len(LogoPath.strip()) == 0:
            print("not found")
            # self.openPopUpWindow("No logo found!")
        else:
            Logo = Image.open(LogoPath.strip())
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

            # Save the image in the desired path.
            Background.save(SetupFile.SavedPathWithLogo)
    except:
        print("can't add logo")


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
        # Folder check
        FolderPresentEnsured(SetupFile.ProgramFilesFolder)
        FolderPresentEnsured(SetupFile.ResourceFolder)
        FolderPresentEnsured(SetupFile.OutputFolder)
        FolderPresentEnsured(SetupFile.LogoFolder)

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

    def trial(self):
        print("trial")

    # save multiple combined photos in a folder.
    def SaveMultipleImages(self):
        ProgressBar=self.getProgressBar()
        ProgressBar.progressBar.setValue(0)
        global NumberOfPhotos
        print("Start of multiple save")
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if not len(directory) == 0:
            ProgressBar.show()

            # self.showProgressBar()
            self.my_thread = QThread()
            self.worker = Worker(directory, self.FilePath.text(), NumberOfPhotos)

            # We're connecting things to the correct spots
            self.worker.moveToThread(self.my_thread)
            self.worker.progressbar.connect(ProgressBar.updateProgressBar)
            self.my_thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.my_thread.quit)
            # #
            self.worker.finished.connect(self.worker.deleteLater)
            self.my_thread.finished.connect(self.my_thread.deleteLater)
            # self.worker.progress.connect(self.reportProgress)

            self.my_thread.start()

        # @QtCore.pyqtSlot()
        # def x(self, MainWindow, ProgressBar1, directory, FilePath, NumberOfPhotos1):
        #     self.loadthread = MultipleImages(MainWindow, directory, FilePath, ProgressBar1, NumberOfPhotos1)
        #     print(FilePath)
        #     print(NumberOfPhotos)
        #     self.loadthread.start()

    # check if it is to save a single image or multiple images.
    def Save(self):
        name, extension = os.path.splitext(self.FilePath.text())
        LogoPath, LogoPositionHeight, LogoPositionWidth, LogoSizeHeight, LogoSizeWidth = LogoSetting.getValuesFromFile()
        if not len(LogoPath.strip()) == 0:
            if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                SaveNewImage()
            else:
                global NumberOfPhotos
                if not NumberOfPhotos == 0:
                    print("not empty")
                    self.SaveMultipleImages()
                else:
                    self.openPopUpWindow("No images found in the folder!")
        else:
            self.openPopUpWindow("Logo not found!")

    # Open the test model MainWindow
    def openLogoSetting(self):
        self.window = QtWidgets.QMainWindow()
        self.window = LogoSetting.MyWindow()
        self.window.show()
        self.window.pushButton.clicked.connect(self.update)

    # Open the test model MainWindow
    def openImageSetting(self):
        self.window = QtWidgets.QMainWindow()
        self.window = ImageSettingPage.MyWindow()
        self.window.show()
        self.window.pushButton.clicked.connect(self.update)

    # Open the pop-up MainWindow.
    def openPopUpWindow(self, message):
        self.window = QtWidgets.QMainWindow()
        self.window = popupmsg.MyWindow()
        self.window.setMessage(message)
        self.window.show()

    def getProgressBar(self):
        self.ProgressBar = QtWidgets.QMainWindow()
        self.ProgressBar = ProgressBar.MyWindow()
        return self.ProgressBar

    # # Show the progress bar.
    # def showProgressBar(self):
    #     print("hi")
    #     self.window = QtWidgets.QMainWindow()
    #     self.window = ProgressBar.MyWindow()
    #     self.window.show()
    #     # self.ContinuouslyUpdateProgressBar(self.window)

    # @QtCore.pyqtSlot()
    # def ContinuouslyUpdateProgressBar(self, window):
    #     self.loadthread = UpdateProgressBar(window)
    #     self.loadthread.start()

    # update the main screen with original image and preview of the combined image.
    def update(self):
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
        if extension == "":
            print("Folder detected")
            global NumberOfPhotos
            dir_path = self.FilePath.text()
            res = []
            NumberOfPhotos = 0
            global PhotoFiles
            PhotoFiles = []
            for (dir_path, dir_names, file_names) in walk(dir_path):
                for file in file_names:
                    name, extension = os.path.splitext(file)
                    if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                        PhotoFiles.append(file)
                        NumberOfPhotos = NumberOfPhotos + 1
                res.extend(file_names)
            print(PhotoFiles)
            print(NumberOfPhotos)

            self.OriginalImage.setText("Loaded from folder")
            self.OriginalImage.setAlignment(Qt.AlignCenter)
            self.OriginalImage.setStyleSheet("QLabel{\n"
                                             "    border: 1px solid;\n"
                                             "background-color: white;\n "
                                             "     }\n"
                                             "")

            self.PreviewImage.setText("No preview for folder\n Number of Images in folder : " + str(NumberOfPhotos))
            self.PreviewImage.setAlignment(Qt.AlignCenter)
            self.PreviewImage.setStyleSheet("QLabel{\n"
                                            "    border: 1px solid;\n"
                                            "background-color: white;\n "
                                            "     }\n"
                                            "")

            # send to add logo to all images

    # Open file dialog to import image
    def ImportImage(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'Import Image',
                                                   'Image', "Image(*.jpeg);;Image(*.jpg);;Image(*.png)")
            path = filename[0]
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
        FilePath = [u.toLocalFile() for u in event.mimeData().urls()]
        try:
            for f in FilePath:
                name, extension = os.path.splitext(f)
                if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG" or extension.upper() == "":
                    self.FilePath.setText(f)
                    self.update()
                else:
                    self.OriginalImage.setStyleSheet(SetupFile.EmptyImage)
                    self.OriginalImage.setText("")
                    self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)
                    self.PreviewImage.setText("")
                    self.FilePath.setText("")
                    self.openPopUpWindow("Please drop a folder or an image file")

            global trial
            dir_path = self.FilePath.text()
            for (dir_path, dir_names, file_names) in walk(dir_path):
                for file in file_names:
                    name, extension = os.path.splitext(file)
                    if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                        trial.append(os.path.join(dir_path, file))
            print(trial)
        except:
            None

    # when user closes the main MainWindow, remove temp files and close all other sub windows.
    def closeEvent(self, event):
        if exists(SetupFile.SavedPathWithLogo):
            os.remove(SetupFile.SavedPathWithLogo)
        if exists(SetupFile.SavedPathWithResize):
            os.remove(SetupFile.SavedPathWithResize)
        for window in QApplication.topLevelWidgets():
            window.close()


# class UpdateProgressBar(QThread):
#     def __init__(self, window):
#         QThread.__init__(self)
#         self.window = window
#
#     def run(self):
#         while True:
#             print(str(sem.tryAcquire(1)))
#             if sem.tryacquire(1):
#                 global NumberOfPhotos
#                 global total
#                 print(str(sem.tryAcquire(1)))
#                 sem.acquire(1)
#                 print("woak")
#                 # if not (total == NumberOfPhotos):
#                 #     print((total/NumberOfPhotos)*100)
#                 #     self.MainWindow.updateProgressBar(total, NumberOfPhotos)
#                 if total == NumberOfPhotos:
#                     print("break")
#                     sem.release(1)
#                     break
#                 else:
#                     print(((total + 1) / NumberOfPhotos) * 100)
#                     print("total: " + str(total + 1))
#                     print("Photos: " + str(NumberOfPhotos))
#                     self.window.updateProgressBar(total + 1, NumberOfPhotos)
#                     sem.release(1)

class Worker(QObject):
    progressbar = pyqtSignal(int, int, name="ProgressBarParameters")
    finished = pyqtSignal()

    def __init__(self, directory, FilePath, NumberOfPhotos):
        super(Worker, self).__init__()
        self.directory = directory
        self.FilePath = FilePath
        self.NumberOfPhotos = NumberOfPhotos

    def run(self):
        print("heyyyyyyyyyyyyyy" + self.directory)
        print("directory: " + self.directory)
        print("dir_path: " + self.FilePath)
        total1 = 0
        for (dir_path, dir_names, file_names) in walk(self.FilePath):
            for file in file_names:
                print(file)
                name, extension = os.path.splitext(file)
                if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                    # trial.append(os.path.join(dir_path, file))
                    AddLogo(os.path.join(dir_path, file))
                    total1 = total1 + 1
                    self.progressbar.emit(total1, NumberOfPhotos)
                    img1 = Image.open(SetupFile.SavedPathWithLogo)
                    img1.save(self.directory + "/" + file)
        self.finished.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
