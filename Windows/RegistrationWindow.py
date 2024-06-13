# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistrationWindowibjyXF.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        if not RegistrationWindow.objectName():
            RegistrationWindow.setObjectName(u"RegistrationWindow")
        RegistrationWindow.resize(640, 480)
        RegistrationWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(RegistrationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	border: 2px solid rgb(220, 220, 220);\n"
"	border-radius: 12px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"QFrame {\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame QWidget{\n"
"	border: none;\n"
"	color: rgb(220, 220, 220);\n"
"	font: 18pt ;\n"
"}\n"
"\n"
"QPushButton {\n"
"	outline-color: transparent;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(43, 45, 49);\n"
"	font: 18pt ;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(53, 54, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(74, 77, 84);\n"
" }\n"
"\n"
"QLineEdit {\n"
"	border:none;\n"
"	background-color: rgb(43, 45, 49);\n"
"	font:18pt;\n"
"	border-radius: 8px;\n"
"	color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 60, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.emailEdit = QLineEdit(self.frame_2)
        self.emailEdit.setObjectName(u"emailEdit")

        self.verticalLayout.addWidget(self.emailEdit)

        self.errorEmailLabel = QLabel(self.frame_2)
        self.errorEmailLabel.setObjectName(u"errorEmailLabel")
        self.errorEmailLabel.setStyleSheet(u"font: 9pt;\n"
"color: rgb(209, 76, 64);")
        self.errorEmailLabel.setTextFormat(Qt.AutoText)
        self.errorEmailLabel.setScaledContents(False)
        self.errorEmailLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.errorEmailLabel)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.passwortFrame = QFrame(self.centralwidget)
        self.passwortFrame.setObjectName(u"passwortFrame")
        self.passwortFrame.setFrameShape(QFrame.StyledPanel)
        self.passwortFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.passwortFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 60, 0, 0)
        self.label = QLabel(self.passwortFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.passwordLine = QFrame(self.passwortFrame)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setFrameShape(QFrame.StyledPanel)
        self.passwordLine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.passwordLine)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passwordEdit = QLineEdit(self.passwordLine)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setInputMask(u"")
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.passwordEdit)

        self.passwordButton = QPushButton(self.passwordLine)
        self.passwordButton.setObjectName(u"passwordButton")
        self.passwordButton.setMinimumSize(QSize(24, 0))
        self.passwordButton.setMaximumSize(QSize(24, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/images/visibility_lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.passwordButton.setIcon(icon)
        self.passwordButton.setIconSize(QSize(24, 24))
        self.passwordButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.passwordButton)


        self.verticalLayout_2.addWidget(self.passwordLine)

        self.errorLabel = QLabel(self.passwortFrame)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setStyleSheet(u"font: 9pt;\n"
"color: rgb(209, 76, 64);")
        self.errorLabel.setTextFormat(Qt.AutoText)
        self.errorLabel.setScaledContents(False)
        self.errorLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.errorLabel)


        self.verticalLayout_3.addWidget(self.passwortFrame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.enterButton = QPushButton(self.frame)
        self.enterButton.setObjectName(u"enterButton")

        self.horizontalLayout.addWidget(self.enterButton)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout_3.addWidget(self.frame)

        RegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrationWindow)
        self.closeButton.clicked.connect(RegistrationWindow.close)

        QMetaObject.connectSlotsByName(RegistrationWindow)
    # setupUi

    def retranslateUi(self, RegistrationWindow):
        RegistrationWindow.setWindowTitle(QCoreApplication.translate("RegistrationWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("RegistrationWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.errorEmailLabel.setText("")
        self.label.setText(QCoreApplication.translate("RegistrationWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.passwordEdit.setText("")
        self.passwordButton.setText("")
        self.errorLabel.setText("")
        self.enterButton.setText(QCoreApplication.translate("RegistrationWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.closeButton.setText(QCoreApplication.translate("RegistrationWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

