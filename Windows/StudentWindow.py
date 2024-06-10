# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentWindowcZWqUW.ui'
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
"QComboBox {\n"
"	border-radius: 4px;\n"
"	background-color: rgb(43, 45, 49);\n"
"	font: 18pt ;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	font: 12px;\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QCom"
                        "boBox QAbstractItemView::item {\n"
"	background-color: rgb(43, 45, 49);\n"
"    border: none;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item::selected {\n"
"	background-color: rgb(30, 31, 34);\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item::hover {\n"
"	background-color: rgb(30, 31, 34);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
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
        self.label_3.setMaximumSize(QSize(90, 16777215))

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

