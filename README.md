#  LogoAdder

A simple windows application built to add logo to an image. What make's this application unique is that the user can drop a folder and it would add logo to all images in the folder.

 The setup.exe file can be download from [here](https://drive.google.com/file/d/1MhuOnpHhGqo91t71o5IfRWZSZrRb0jg_/view?usp=sharing), simply run the setup file to install the software.

## Table of Contents 📘
* [Libraries](#libraries)
* [Note](#Note)
* [Adding files](#AddingFiles)
* [Settings](#Setting)

# <a name="libraries"></a>
## Libraries 💻
The following libraries were used in this project:
* PyQt5
* PIL

Download the requirements.txt file and while in virtual environment
```
pip install -r requirements.txt
```
<a name="Note"></a>
## Note 🗒️
Pyqt5 supports Python 3.5- 3.9

<a name="AddingFiles"></a>
## Adding Files
There are 2 ways of adding a file. Either by dragging and dropping the file or Selecting it from the directory using the import button.
<br><br><br>
<p>
 <img align= right width= 600 src="https://github.com/abubakar20-02/LogoAdder-GUI-interface/blob/master/gif/Import%20images.gif">
 <h4>Using the import button</h4>
 The user clicks on the import button which asks the user to give the file location via the file explorer directory.
  <br clear="right"/>
  <br><hr><br><br>
</p>

<p>
 <img align= right width= 600 src="https://github.com/abubakar20-02/LogoAdder-GUI-interface/blob/master/gif/DragAndDropLogo.gif">
<h4>Using drag and drop</h4></pre>
The user can drag and drop to the application directly.
 <br clear="right"/>
 <br><hr>
</p>
<br clear="right"/>
User can also drag and drop a directory instead of a file to process the entire directory
  <br><br><br>
<p>
  <img align = right width = 600 src="https://github.com/abubakar20-02/LogoAdder-GUI-interface/blob/master/gif/DragAndDropFile.gif">
  <h4>Using drag and drop for directory</h4>
  The user can drag and drop an entire directory to process multiple image files in one go.
  <br clear="right"/>
  <br><br><br>
</p>

<a name="Setting"></a>
## Settings
User is given 2 setting options, logo setting and image setting.
<br><br><br>
<p>
 <img align= right width= 600 src="https://github.com/abubakar20-02/LogoAdder-GUI-interface/blob/master/gif/ImageSetting.gif">
 <h4>Image Setting</h4>
 User can either choose to keep the original resolution or use some of the most common pre-defined resolutions. They can also use custom resolution ranging from 100 x 100 to max 10,000 x 10,000.
  <br clear="right"/>
  <br><hr><br><br>
</p>
<p>
 <img align= right width= 600 src="https://github.com/abubakar20-02/LogoAdder-GUI-interface/blob/master/gif/LogoSetting.gif">
 <h4>Logo Setting</h4>
 User are not required to add logo as it is optional. If they do not want the logo to appear, they simply have to set logo size width or height to 0. If they wish to have a logo, they have to select a logo followed by the size and position.
  <br clear="right"/>
  <br><br><br>
</p>
