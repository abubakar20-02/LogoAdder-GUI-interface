from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(QObject):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(660, 400)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(660, 400))
        Form.setStyleSheet("background-color: rgb(255, 241, 171)")

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.SelectLogoButton = QtWidgets.QPushButton(Form)
        self.SelectLogoButton.setStyleSheet("QPushButton {\n"
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
        self.SelectLogoButton.setObjectName("SelectLogoButton")
        self.horizontalLayout.addWidget(self.SelectLogoButton)

        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setMaximumSize(QtCore.QSize(600, 30))
        self.label.setStyleSheet("QLabel{\n"
                                 "     border: 1px solid;\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 10px;\n"
                                 "    \n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "     }")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)
        self.LogoSizeWidth = QtWidgets.QSlider(Form)
        self.LogoSizeWidth.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoSizeWidth.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoSizeWidth.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.LogoSizeWidth.setOrientation(QtCore.Qt.Horizontal)
        self.LogoSizeWidth.setObjectName("LogoSizeWidth")
        self.horizontalLayout_3.addWidget(self.LogoSizeWidth)

        self.LogoSizeWidthBox = QtWidgets.QSpinBox(Form)
        self.LogoSizeWidthBox.setStyleSheet("QSpinBox{\n"
                                            "    border-style: outset;\n"
                                            "    border-width: 1px;\n"
                                            "    border-radius: 10px;\n"
                                            "    border-color:black;\n"
                                            "    color: solid black;\n"
                                            "    background-color: white;\n"
                                            "    }")
        self.LogoSizeWidthBox.setObjectName("LogoSizeWidthBox")

        self.horizontalLayout_3.addWidget(self.LogoSizeWidthBox)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.LogoSizeHeight = QtWidgets.QSlider(Form)
        self.LogoSizeHeight.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoSizeHeight.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoSizeHeight.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.LogoSizeHeight.setMaximum(100)
        self.LogoSizeHeight.setOrientation(QtCore.Qt.Horizontal)
        self.LogoSizeHeight.setObjectName("LogoSizeHeight")
        self.horizontalLayout_4.addWidget(self.LogoSizeHeight)
        self.LogoSizeHeightBox = QtWidgets.QSpinBox(Form)
        self.LogoSizeHeightBox.setStyleSheet("QSpinBox{\n"
                                             "    border-style: outset;\n"
                                             "    border-width: 1px;\n"
                                             "    border-radius: 10px;\n"
                                             "    border-color:black;\n"
                                             "    background-color: white;\n"
                                             "    color: solid black;\n"
                                             "    }")
        self.LogoSizeHeightBox.setObjectName("LogoSizeHeightBox")
        self.horizontalLayout_4.addWidget(self.LogoSizeHeightBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setMaximumSize(QtCore.QSize(30, 30))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.LogoPositionWidth = QtWidgets.QSlider(Form)
        self.LogoPositionWidth.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoPositionWidth.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoPositionWidth.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.LogoPositionWidth.setMaximum(100)
        self.LogoPositionWidth.setOrientation(QtCore.Qt.Horizontal)
        self.LogoPositionWidth.setObjectName("LogoPositionWidth")
        self.horizontalLayout_7.addWidget(self.LogoPositionWidth)
        self.LogoPositionWidthBox = QtWidgets.QSpinBox(Form)
        self.LogoPositionWidthBox.setStyleSheet("QSpinBox{\n"
                                                "    border-style: outset;\n"
                                                "    border-width: 1px;\n"
                                                "    border-radius: 10px;\n"
                                                "    border-color:black;\n"
                                                "    background-color: white;\n"
                                                "    color: solid black;\n"
                                                "    }")
        self.LogoPositionWidthBox.setObjectName("LogoPositionWidthBox")
        self.horizontalLayout_7.addWidget(self.LogoPositionWidthBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setMaximumSize(QtCore.QSize(30, 30))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.LogoPositionHeight = QtWidgets.QSlider(Form)
        self.LogoPositionHeight.setMinimumSize(QtCore.QSize(100, 0))
        self.LogoPositionHeight.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogoPositionHeight.setStyleSheet("QSlider::groove:horizontal {\n"
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
        self.LogoPositionHeight.setMaximum(100)
        self.LogoPositionHeight.setOrientation(QtCore.Qt.Horizontal)
        self.LogoPositionHeight.setObjectName("LogoPositionHeight")
        self.horizontalLayout_8.addWidget(self.LogoPositionHeight)
        self.LogoPositionHeightBox = QtWidgets.QSpinBox(Form)
        self.LogoPositionHeightBox.setStyleSheet("QSpinBox{\n"
                                                 "    border-style: outset;\n"
                                                 "    border-width: 1px;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    border-color:black;\n"
                                                 "    background-color: white;\n"
                                                 "    color: solid black;\n"
                                                 "    }")
        self.LogoPositionHeightBox.setObjectName("LogoPositionHeightBox")
        self.horizontalLayout_8.addWidget(self.LogoPositionHeightBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SelectLogoButton.setText(_translate("Form", "Select Logo"))
        self.label_5.setText(_translate("Form", "Logo Size:      "))
        self.label_3.setText(_translate("Form", "w%"))
        self.label_4.setText(_translate("Form", "h%"))
        self.label_6.setText(_translate("Form", "Logo Position:"))
        self.label_7.setText(_translate("Form", "w%"))
        self.label_8.setText(_translate("Form", "h%"))
        self.pushButton.setText(_translate("Form", "Apply Changes"))


class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setLimitsToComboBox(0, 100)

        self.SelectLogoButton.clicked.connect(self.ImportLogo)

        self.LogoSizeWidthBox.valueChanged.connect(self.a)
        self.LogoSizeWidth.valueChanged.connect(self.b)

        self.LogoSizeHeightBox.valueChanged.connect(self.c)
        self.LogoSizeHeight.valueChanged.connect(self.d)

        self.LogoPositionWidthBox.valueChanged.connect(self.e)
        self.LogoPositionWidth.valueChanged.connect(self.f)

        self.LogoPositionHeightBox.valueChanged.connect(self.g)
        self.LogoPositionHeight.valueChanged.connect(self.h)

    def ImportLogo(self):
        filename = QFileDialog.getOpenFileName(self, 'Logo',
                                               'Logo', "Logo(*.png)")
        path = filename[0]
        print(path)
        if not len(path) == 0:
            self.label.setText(path)

    def a(self):
        self.LogoSizeWidth.setValue(self.LogoSizeWidthBox.value())

    def b(self):
        self.LogoSizeWidthBox.setValue(self.LogoSizeWidth.value())

    def c(self):
        self.LogoSizeHeight.setValue(self.LogoSizeHeightBox.value())

    def d(self):
        self.LogoSizeHeightBox.setValue(self.LogoSizeHeight.value())

    def e(self):
        self.LogoPositionWidth.setValue(self.LogoPositionWidthBox.value())

    def f(self):
        self.LogoPositionWidthBox.setValue(self.LogoPositionWidth.value())

    def g(self):
        self.LogoPositionHeight.setValue(self.LogoPositionHeightBox.value())

    def h(self):
        self.LogoPositionHeightBox.setValue(self.LogoPositionHeight.value())

    def setLimitsToComboBox(self, Minimum, Maximum):
        self.LogoSizeWidthBox.setMinimum(Minimum)
        self.LogoSizeWidthBox.setMaximum(Maximum)

        self.LogoSizeWidth.setMinimum(Minimum)
        self.LogoSizeWidth.setMaximum(Maximum)

        self.LogoSizeHeightBox.setMinimum(Minimum)
        self.LogoSizeHeightBox.setMaximum(Maximum)

        self.LogoSizeHeight.setMinimum(Minimum)
        self.LogoSizeHeight.setMaximum(Maximum)

        self.LogoPositionWidthBox.setMinimum(Minimum)
        self.LogoPositionWidthBox.setMaximum(Maximum)

        self.LogoPositionWidth.setMinimum(Minimum)
        self.LogoPositionWidth.setMaximum(Maximum)

        self.LogoPositionHeightBox.setMinimum(Minimum)
        self.LogoPositionHeightBox.setMaximum(Maximum)

        self.LogoPositionHeight.setMinimum(Minimum)
        self.LogoPositionHeight.setMaximum(Maximum)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
