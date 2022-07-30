import os
from os.path import exists

from PIL import Image
from PIL.Image import Resampling  # this is not an error.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import ExploringFilePopUp
import ImageSettingPage
import LogoSetting
import ProcessingPopUp
import ProgressBar
import SetupFile
import popupmsg


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
    try:
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
    except:
        print("Add logo failed")


# method to resize original image.
def resizeImage(originalImagePath):
    try:
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
    except:
        print("Resize Failed")


# Open the test model MainWindow
def openLogoSetting(self):
    self.window = QtWidgets.QMainWindow()
    self.window = LogoSetting.MyWindow()
    self.window.show()
    self.window.pushButton.clicked.connect(lambda: CheckAndUpdate(self))


# Open the test model MainWindow
def openImageSetting(self):
    self.window = QtWidgets.QMainWindow()
    self.window = ImageSettingPage.MyWindow()
    self.window.show()
    self.window.pushButton.clicked.connect(lambda: CheckAndUpdate(self))


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


# get the object of exploring file pop up.
def getExploringFilePopUp(self):
    self.ExploringFilePopUp = QtWidgets.QMainWindow()
    self.ExploringFilePopUp = ExploringFilePopUp.MyWindow()
    return self.ExploringFilePopUp


# function to get the progress bar object.
def getProgressBar(self):
    self.ProgressBar = QtWidgets.QMainWindow()
    self.ProgressBar = ProgressBar.MyWindow()
    return self.ProgressBar


# function to get the processing pop up object.
def getProcessingPopUp(self):
    self.ProcessingPopUp = QtWidgets.QMainWindow()
    self.ProcessingPopUp = ProcessingPopUp.MyWindow()
    return self.ProcessingPopUp
