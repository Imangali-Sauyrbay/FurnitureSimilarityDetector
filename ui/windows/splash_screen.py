# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication,
    QMetaObject, QRect, Qt)
from PyQt5.QtGui import (
    QFont)
from PyQt5.QtWidgets import (QFrame, QLabel,
    QProgressBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 410)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_border_frame = QFrame(self.centralwidget)
        self.logo_border_frame.setObjectName(u"logo_border_frame")
        self.logo_border_frame.setGeometry(QRect(41, 31, 230, 95))
        self.logo_border_frame.setStyleSheet(u"border: 3px solid  rgb(150, 3, 200);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(180, 58, 255, 255));\n"
"border-radius: 20px;")
        self.logo_border_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_border_frame.setFrameShadow(QFrame.Raised)
        self.logo_frame = QFrame(self.logo_border_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(10, 10, 210, 75))
        self.logo_frame.setStyleSheet(u"image: url(:/images/Auezov-logotip-asyl.svg);\n"
"border: none;")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.main_bg_border_frame = QFrame(self.centralwidget)
        self.main_bg_border_frame.setObjectName(u"main_bg_border_frame")
        self.main_bg_border_frame.setGeometry(QRect(130, 50, 400, 200))
        self.main_bg_border_frame.setStyleSheet(u"border-radius: 20px;\n"
"border: 10px solid rgb(93, 0, 255)")
        self.main_bg_border_frame.setFrameShape(QFrame.StyledPanel)
        self.main_bg_border_frame.setFrameShadow(QFrame.Raised)
        self.main_bg_frame = QFrame(self.main_bg_border_frame)
        self.main_bg_frame.setObjectName(u"main_bg_frame")
        self.main_bg_frame.setGeometry(QRect(0, 0, 400, 200))
        self.main_bg_frame.setStyleSheet(u"border-image: url(:/images/auezov.jpg);\n"
"border-radius: 20px;")
        self.main_bg_frame.setFrameShape(QFrame.StyledPanel)
        self.main_bg_frame.setFrameShadow(QFrame.Raised)
        self.welcome = QLabel(self.main_bg_border_frame)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(225, 150, 161, 39))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(25)
        font.setBold(True)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"border-radius: 4px;\n"
"border: 3px solid rgb(8, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(74, 16, 246,140), stop:1 rgba(188, 79, 255, 220));")
        self.bottom_info_frame = QFrame(self.centralwidget)
        self.bottom_info_frame.setObjectName(u"bottom_info_frame")
        self.bottom_info_frame.setGeometry(QRect(130, 240, 400, 120))
        font1 = QFont()
        font1.setFamilies([u"Edwardian Script ITC"])
        font1.setItalic(False)
        self.bottom_info_frame.setFont(font1)
        self.bottom_info_frame.setStyleSheet(u"background-color: rgb(70,0, 100);\n"
"border-radius: 20px;\n"
"border: 5px solid rgb(71, 40, 220);")
        self.bottom_info_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_info_frame.setFrameShadow(QFrame.Raised)
        self.info_label = QLabel(self.bottom_info_frame)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(210, 87, 179, 31))
        font2 = QFont()
        font2.setFamilies([u"Monotype Corsiva"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(True)
        self.info_label.setFont(font2)
        self.info_label.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"color: rgb(255, 255, 255)")
        self.info_loading_label = QLabel(self.bottom_info_frame)
        self.info_loading_label.setObjectName(u"info_loading_label")
        self.info_loading_label.setGeometry(QRect(110, 10, 191, 31))
        font3 = QFont()
        font3.setFamilies([u"Raleway ExtraBold"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.info_loading_label.setFont(font3)
        self.info_loading_label.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.info_loading_label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.bottom_info_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 55, 211, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color:rgb(70, 0, 100);\n"
"	border-style: none;\n"
"	border-radius: 6px;\n"
"	text-align:center;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 6px;\n"
"}")
        self.progressBar.setValue(0)
        self.loading_state_info_label = QLabel(self.bottom_info_frame)
        self.loading_state_info_label.setObjectName(u"loading_state_info_label")
        self.loading_state_info_label.setGeometry(QRect(250, 50, 141, 31))
        font4 = QFont()
        font4.setPointSize(10)
        self.loading_state_info_label.setFont(font4)
        self.loading_state_info_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none")
        MainWindow.setCentralWidget(self.centralwidget)
        self.bottom_info_frame.raise_()
        self.main_bg_border_frame.raise_()
        self.logo_border_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcome.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Made By: IP19-3tk  Suyrbai I.", None))
        self.info_loading_label.setText(QCoreApplication.translate("MainWindow", u"Initializing...", None))
        self.loading_state_info_label.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
    # retranslateUi

