# Folder
ProgramFilesFolder = "Program Files"
ResourceFolder = "Resources"
OutputFolder = "Output"
LogoFolder = "Logo"

LogoSettingPageTitle = "Logo Settings"
ImageSettingPageTitle = "Image Settings"

MenuTitle_Setting = "Settings"

MainBackground = "background-color: rgb(255, 241, 171)"

EmptyImage = ("QLabel{\n"
              "    border: 1px solid;\n"
              "    background-color: rgb(250, 250, 250);\n"
              "     }\n"
              "")

Button = ("QPushButton {\n"
          "    background-color: rgb(107, 0, 0);\n"
          "    border-style: outset;\n"
          "    border-width: 1px;\n"
          "    border-radius: 10px;\n"
          "    border-color:white;\n"
          "    color: rgb(255, 241, 171);\n"
          "    font: bold 12px;\n"
          "    min-width: 10em;\n"
          "    padding: 6px;\n"
          "}\n"
          "QPushButton:hover {\n"
          "    color: white;\n"
          "}")

FilePath = ("QLabel{\n"
            "     border: 1px solid;\n"
            "    border-style: outset;\n"
            "    border-width: 1px;\n"
            "    border-radius: 10px;\n"
            "    \n"
            "    background-color: rgb(255, 255, 255);\n"
            "     }")

MenuBar = "QMenuBar{background-color: white}""QMenu{background-color: white}""QMenu::item:selected { ""background" \
          "-color: #1261A0;color: rgb(255,255,""255);} "

SavedPathWithLogo = ResourceFolder + "/SavedwithLogo.png"

SavedPathWithResize = ResourceFolder + "/SavedwithResize.png"


PreviewImage = ("QLabel{border: 1px solid;image: url(" + SavedPathWithLogo + ");background-color: gray;}")

Slider = ("QSlider::groove:horizontal {\n"
          "    border: 1px solid black;\n"
          "    height: 8px;\n"
          "    background: solid white;\n"
          "    margin: 2px 0;\n"
          "}\n"
          "\n"
          "QSlider::handle:horizontal {\n"
          "    background: rgb(107, 0, 0);\n"
          "    border: 1px solid black;\n"
          "    width: 18px;\n"
          "    margin: -2px 0; \n"
          "    border-radius: 3px;\n"
          "}")

SpinBox = ("QSpinBox{\n"
           "    border-style: outset;\n"
           "    border-width: 1px;\n"
           "    border-color:black;\n"
           "    color: solid black;\n"
           "    background-color: white;\n"
           "    }")

ComboBox = ("QComboBox{\n"
            "    border-style: outset;\n"
            "    border-width: 1px;\n"
            "    border-color:black;\n"
            "    color: solid black;\n"
            "    background-color: white;\n"
            "    }"
            "QListView"
            "{"
            "background-color: white;"
            "}"
            )

SetUpFilePath = ProgramFilesFolder + "/Setup.txt"

ImageSetupFilePath = ProgramFilesFolder + "/ImageSetup.txt"

MainIcon = ResourceFolder + "/Logo.png"

WarningImage = "QLabel{image: url(Resources/Warning.png);}"

CompleteImage = "QLabel{image: url(Resources/Complete.png);}"
