# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentWindowAuAbPL.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_StudentWindow(object):
    def setupUi(self, StudentWindow):
        if not StudentWindow.objectName():
            StudentWindow.setObjectName(u"StudentWindow")
        StudentWindow.resize(640, 480)
        StudentWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(StudentWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(43, 45, 49);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(71, 80, 83);\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(148, 155, 164);\n"
"}\n"
"QComboBox {\n"
"	border: 1px solid rgb(148, 155, 164);\n"
"	background-color: rgb(71, 80, 83);\n"
"	color: rgb(221, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(221, 255, 255);\n"
"	background-color: rgb(71, 80, 83);\n"
"	border: 1px solid rgb(148, 155, 164)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: rgb(184, 212, 212);\n"
"	background-color: rgb(61, 69, 72);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	color: rgb(134, 182, 182);\n"
"	background-color: rgb(34, 39, 40);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FullNameFrame = QFrame(self.centralwidget)
        self.FullNameFrame.setObjectName(u"FullNameFrame")
        self.FullNameFrame.setFrameShape(QFrame.StyledPanel)
        self.FullNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FullNameFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.FullNameFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.fullNameInput = QLineEdit(self.FullNameFrame)
        self.fullNameInput.setObjectName(u"fullNameInput")

        self.horizontalLayout.addWidget(self.fullNameInput)


        self.verticalLayout.addWidget(self.FullNameFrame)

        self.EmailFrame = QFrame(self.centralwidget)
        self.EmailFrame.setObjectName(u"EmailFrame")
        self.EmailFrame.setFrameShape(QFrame.StyledPanel)
        self.EmailFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.EmailFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.EmailFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.emailInput = QLineEdit(self.EmailFrame)
        self.emailInput.setObjectName(u"emailInput")

        self.horizontalLayout_2.addWidget(self.emailInput)


        self.verticalLayout.addWidget(self.EmailFrame)

        self.GroupFrame = QFrame(self.centralwidget)
        self.GroupFrame.setObjectName(u"GroupFrame")
        self.GroupFrame.setFrameShape(QFrame.StyledPanel)
        self.GroupFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.GroupFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.GroupFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.groupBox = QComboBox(self.GroupFrame)
        self.groupBox.setObjectName(u"groupBox")

        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.GroupFrame)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addButton = QPushButton(self.Buttons)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_4.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.Buttons)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_4.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.Buttons)

        StudentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentWindow)

        QMetaObject.connectSlotsByName(StudentWindow)
    # setupUi

    def retranslateUi(self, StudentWindow):
        StudentWindow.setWindowTitle(QCoreApplication.translate("StudentWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("StudentWindow", u"\u0424\u0418\u041e", None))
        self.label_2.setText(QCoreApplication.translate("StudentWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("StudentWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.addButton.setText(QCoreApplication.translate("StudentWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("StudentWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

