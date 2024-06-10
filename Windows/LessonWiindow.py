# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LessonWindowxggURB.ui'
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

class Ui_LessonWindow(object):
    def setupUi(self, LessonWindow):
        if not LessonWindow.objectName():
            LessonWindow.setObjectName(u"LessonWindow")
        LessonWindow.resize(640, 478)
        LessonWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(LessonWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	background-color: rgb(30, 31, 34);\n"
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
"QWidget {\n"
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
"	ba"
                        "ckground-color: rgb(43, 45, 49);\n"
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
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.EmailFrame = QFrame(self.centralwidget)
        self.EmailFrame.setObjectName(u"EmailFrame")
        self.EmailFrame.setFrameShape(QFrame.StyledPanel)
        self.EmailFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.EmailFrame)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.EmailFrame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lessonInput = QLineEdit(self.EmailFrame)
        self.lessonInput.setObjectName(u"lessonInput")

        self.horizontalLayout_2.addWidget(self.lessonInput)


        self.verticalLayout.addWidget(self.EmailFrame)

        self.EmailFrame_2 = QFrame(self.centralwidget)
        self.EmailFrame_2.setObjectName(u"EmailFrame_2")
        self.EmailFrame_2.setFrameShape(QFrame.StyledPanel)
        self.EmailFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.EmailFrame_2)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.EmailFrame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.indexInput = QLineEdit(self.EmailFrame_2)
        self.indexInput.setObjectName(u"indexInput")

        self.horizontalLayout_3.addWidget(self.indexInput)


        self.verticalLayout.addWidget(self.EmailFrame_2)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.Buttons)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.Buttons)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.Buttons)

        LessonWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LessonWindow)

        QMetaObject.connectSlotsByName(LessonWindow)
    # setupUi

    def retranslateUi(self, LessonWindow):
        LessonWindow.setWindowTitle(QCoreApplication.translate("LessonWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("LessonWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None))
        self.label_3.setText(QCoreApplication.translate("LessonWindow", u"\u041a\u043e\u0434", None))
        self.addButton.setText(QCoreApplication.translate("LessonWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("LessonWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

