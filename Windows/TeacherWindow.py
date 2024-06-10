# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeacherWindowyJcyrh.ui'
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

class Ui_TeacherWindow(object):
    def setupUi(self, TeacherWindow):
        if not TeacherWindow.objectName():
            TeacherWindow.setObjectName(u"TeacherWindow")
        TeacherWindow.resize(640, 480)
        TeacherWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(TeacherWindow)
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
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.EmailFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.emailInput = QLineEdit(self.EmailFrame)
        self.emailInput.setObjectName(u"emailInput")

        self.horizontalLayout_2.addWidget(self.emailInput)


        self.verticalLayout.addWidget(self.EmailFrame)

        self.TeacherFrame = QFrame(self.centralwidget)
        self.TeacherFrame.setObjectName(u"TeacherFrame")
        self.TeacherFrame.setFrameShape(QFrame.StyledPanel)
        self.TeacherFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TeacherFrame)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.TeacherFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.groupBox = QComboBox(self.TeacherFrame)
        self.groupBox.setObjectName(u"groupBox")

        self.horizontalLayout_5.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.TeacherFrame)

        self.LessonFrame1 = QFrame(self.centralwidget)
        self.LessonFrame1.setObjectName(u"LessonFrame1")
        self.LessonFrame1.setFrameShape(QFrame.StyledPanel)
        self.LessonFrame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.LessonFrame1)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.LessonFrame1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lessonBox1 = QComboBox(self.LessonFrame1)
        self.lessonBox1.setObjectName(u"lessonBox1")

        self.horizontalLayout_3.addWidget(self.lessonBox1)


        self.verticalLayout.addWidget(self.LessonFrame1)

        self.LessonFrame2 = QFrame(self.centralwidget)
        self.LessonFrame2.setObjectName(u"LessonFrame2")
        self.LessonFrame2.setFrameShape(QFrame.StyledPanel)
        self.LessonFrame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.LessonFrame2)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.LessonFrame2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lessonBox2 = QComboBox(self.LessonFrame2)
        self.lessonBox2.setObjectName(u"lessonBox2")

        self.horizontalLayout_6.addWidget(self.lessonBox2)


        self.verticalLayout.addWidget(self.LessonFrame2)

        self.Buttons = QFrame(self.centralwidget)
        self.Buttons.setObjectName(u"Buttons")
        self.Buttons.setFrameShape(QFrame.StyledPanel)
        self.Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Buttons)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.Buttons)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_4.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.Buttons)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_4.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.Buttons)

        TeacherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TeacherWindow)

        QMetaObject.connectSlotsByName(TeacherWindow)
    # setupUi

    def retranslateUi(self, TeacherWindow):
        TeacherWindow.setWindowTitle(QCoreApplication.translate("TeacherWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TeacherWindow", u"\u0424\u0418\u041e", None))
        self.label_2.setText(QCoreApplication.translate("TeacherWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("TeacherWindow", u"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("TeacherWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442 \u21161", None))
        self.label_5.setText(QCoreApplication.translate("TeacherWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442 \u21162", None))
        self.addButton.setText(QCoreApplication.translate("TeacherWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("TeacherWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

