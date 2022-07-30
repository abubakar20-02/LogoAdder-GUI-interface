from os import walk

from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QSemaphore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from Functions import *

NumberOfPhotos = 0
Close = False
sem = QSemaphore(1)
Stop = False


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

        self.ButtonConnections()
        self.MenuBarConnections()

    # Connects buttons to methods.
    def ButtonConnections(self):
        self.ImportImageButton.clicked.connect(self.ImportImage)
        self.ConvertButton.clicked.connect(self.Save)

    # Connects drop down menu attributes to methods.
    def MenuBarConnections(self):
        self.LogoSetting.triggered.connect(lambda: openLogoSetting(self))
        self.ImageSetting.triggered.connect(lambda: openImageSetting(self))

    # save multiple combined photos in a folder.
    def SaveMultipleImages(self):
        ProgressBar = getProgressBar(self)
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
            self.worker = SaveMultipleImages(directory, self.FilePath.text(), NumberOfPhotos)

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
        if not len(self.FilePath.text()) == 0:
            name, extension = os.path.splitext(self.FilePath.text())
            if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
                SaveNewImage()
            else:
                global NumberOfPhotos
                if not NumberOfPhotos == 0:
                    self.SaveMultipleImages()
                else:
                    openPopUpWindow(self, "No images found in the folder!")
        else:
            openPopUpWindow(self, "No images to work with!")

    # update the main screen with original image and preview of the combined image.
    def update(self):
        name, extension = os.path.splitext(self.FilePath.text())
        if extension.upper() == "":
            self.updateMultipleFileView()
        else:
            self.updateSingleImageView()

    # updates the main page when a folder is dropped.
    def updateMultipleFileView(self):
        ExploringFilePopUp = getExploringFilePopUp(self)
        ExploringFilePopUp.CancelButton.clicked.connect(self.CloseExplorerPopUp)
        name, extension = os.path.splitext(self.FilePath.text())
        if extension == "":
            dir_path = self.FilePath.text()
            # add to thread
            # start a thread and move the worker to it.
            self.my_thread = QThread()
            self.worker = MultipleFileView(dir_path)

            # We're connecting things to the correct spots
            self.worker.moveToThread(self.my_thread)  # move worker to thread.
            # Note: Ui elements should only be updated via the main thread.
            self.worker.TotalFiles.connect(ExploringFilePopUp.setMessage)  # using signal and slots,
            # update ui elements
            self.my_thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.my_thread.quit)  # safely close the thread.
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finished.connect(self.finished)
            self.worker.finished.connect(ExploringFilePopUp.Cancel)
            self.my_thread.finished.connect(self.finishThread)
            self.worker.stop.connect(self.ClearScreen)
            self.worker.SystemDriveTriedtoAccess1.connect(self.WarnUser)
            self.worker.SystemDriveTriedtoAccess.connect(ExploringFilePopUp.ShowFileExplorer)

            self.my_thread.start()
            # end of thread

    # Closes the explorer pop up.
    def CloseExplorerPopUp(self):
        global Stop
        Stop = True
        self.ClearScreen()

    # Warns user if system drive tried to access. The reason why system drive is not allowed is that they also
    # contain temp files, recycle bin as well which might change when we try to process that image.
    def WarnUser(self, SystemDriveTriedtoAccess):
        if SystemDriveTriedtoAccess:
            self.ClearScreen()
            openPopUpWindow(self, "Restricted Access")

    # Once all the image files are found we update the main screen.
    def finished(self):
        global NumberOfPhotos
        global Stop
        self.OriginalImage.setText("Loaded from folder")
        self.OriginalImage.setAlignment(Qt.AlignCenter)
        self.OriginalImage.setStyleSheet(SetupFile.EmptyImage)
        self.PreviewImage.setText("No preview for folder\n Number of Images in folder : " + str(NumberOfPhotos))
        self.PreviewImage.setAlignment(Qt.AlignCenter)
        self.PreviewImage.setStyleSheet(SetupFile.EmptyImage)
        Stop = False

    # update screen when single file added.
    # used multithreading as processing can take time.
    def updateSingleImageView(self):
        ProcessingPopUp = getProcessingPopUp(self)
        name, extension = os.path.splitext(self.FilePath.text())
        if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG":
            if not len(self.FilePath.text()) == 0:
                ProcessingPopUp.show()
                self.my_thread = QThread()
                self.worker = SingleImageView(self.FilePath)

                # We're connecting things to the correct spots
                self.worker.moveToThread(self.my_thread)  # move worker to thread.
                # update ui elements
                self.my_thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.updateScreen)
                self.worker.finished.connect(self.my_thread.quit)  # safely close the thread.
                self.worker.finished.connect(self.worker.deleteLater)
                self.worker.finished.connect(ProcessingPopUp.Close)
                self.my_thread.finished.connect(self.finishThread)

                self.my_thread.start()
                # end of thread

    def updateScreen(self):
        self.OriginalImage.setText("")
        self.PreviewImage.setText("")
        self.OriginalImage.setStyleSheet("QLabel{\n"
                                         "    border: 1px solid;\n"
                                         "    image: url(" + self.FilePath.text() + ");\n"
                                                                                    "background-color: gray;\n "
                                                                                    "     }\n"
                                                                                    "")
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
        self.ClearScreen()
        self.ConvertButton.setEnabled(True)
        FilePath = [u.toLocalFile() for u in event.mimeData().urls()]
        name, extension = os.path.splitext(str(FilePath[0]))
        if extension.upper() == ".JPEG" or extension.upper() == ".JPG" or extension.upper() == ".PNG" or extension.upper() == "":
            self.FilePath.setText(str(FilePath[0]))
            self.update()
        else:
            self.ClearScreen()
            openPopUpWindow(self, "Please drop a folder or file")

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


class SaveMultipleImages(QObject):
    progressbarParameters = pyqtSignal(int, int, name="ProgressBarParameters")
    finished = pyqtSignal()

    def __init__(self, directory, FilePath, TotalNumberOfPhotos):
        super(SaveMultipleImages, self).__init__()
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
                    if str(extension.upper()) == ".JPEG" or str(extension.upper()) == ".JPG" or str(
                            extension.upper()) == ".PNG":
                        AddLogo(os.path.join(dir_path, file))
                        CurrentNumberOfPhotos = CurrentNumberOfPhotos + 1
                        self.progressbarParameters.emit(CurrentNumberOfPhotos, NumberOfPhotos)
                        img1 = Image.open(SetupFile.SavedPathWithLogo)
                        img1.save(self.directory + "/" + file)
        self.finished.emit()


class MultipleFileView(QObject):
    TotalFiles = pyqtSignal(int, name="TotalFiles")
    SystemDriveTriedtoAccess = pyqtSignal(bool)
    SystemDriveTriedtoAccess1 = pyqtSignal(bool)
    finished = pyqtSignal()
    finishedAllFiles = pyqtSignal()
    stop = pyqtSignal()

    def __init__(self, directory):
        super(MultipleFileView, self).__init__()
        self.directory = directory

    def run(self):
        if not self.directory == str(os.getenv("SystemDrive")) + "/":
            self.SystemDriveTriedtoAccess.emit(False)
            global NumberOfPhotos
            NumberOfPhotos = 0
            global Stop
            for (dir_path, dir_names, file_names) in walk(self.directory):
                if Stop:
                    break
                for file in file_names:
                    if Stop:
                        break
                    name, extension = os.path.splitext(file)
                    if str(extension.upper()) == ".JPEG" or str(extension.upper()) == ".JPG" or str(
                            extension.upper()) == ".PNG":
                        NumberOfPhotos = NumberOfPhotos + 1
                        self.TotalFiles.emit(NumberOfPhotos)
        self.finished.emit()
        if self.directory == str(os.getenv("SystemDrive")) + "/":
            self.SystemDriveTriedtoAccess1.emit(True)
        if Stop:
            self.stop.emit()


class SingleImageView(QObject):
    finished = pyqtSignal()

    def __init__(self, FilePath):
        super(SingleImageView, self).__init__()
        self.FilePath = FilePath

    def run(self):
        AddLogo(self.FilePath.text())
        self.finished.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
