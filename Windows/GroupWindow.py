# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GroupWindowMDkgwn.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
                               QFrame, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc


class Ui_GroupWindow(object):
    def setupUi(self, GroupWindow):
        if not GroupWindow.objectName():
            GroupWindow.setObjectName(u"GroupWindow")
        GroupWindow.resize(640, 480)
        self.centralwidget = QWidget(GroupWindow)
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
                                         "\n"
                                         "\n"
                                         "QHeaderView::section, QTableWidget QTableCornerButton::section {\n"
                                         "	background-color: rgb(71, 80, 83);\n"
                                         "    border: 1px solid #fffff8;\n"
                                         "	font: 12pt \"Roboto\";\n"
                                         "	color: rgb(220, 220, 220);\n"
                                         "}\n"
                                         "\n"
                                         "QTableWidget {\n"
                                         "	background-color: rgb(30, 31, 34);\n"
                                         "    gridline-color: #fffff8;\n"
                                         "	font:11pt \"Roboto\";\n"
                                         "	color: rgb(220, 220, 220);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
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

        self.horizontalLayout_2.addWidget(self.label_2)

        self.groupInput = QLineEdit(self.EmailFrame)
        self.groupInput.setObjectName(u"groupInput")

        self.horizontalLayout_2.addWidget(self.groupInput)

        self.verticalLayout.addWidget(self.EmailFrame)

        self.groupLessonTableWidget = QTableWidget(self.centralwidget)
        if (self.groupLessonTableWidget.columnCount() < 1):
            self.groupLessonTableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.groupLessonTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.groupLessonTableWidget.setObjectName(u"groupLessonTableWidget")
        self.groupLessonTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.groupLessonTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.groupLessonTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.groupLessonTableWidget.setShowGrid(True)
        self.groupLessonTableWidget.setGridStyle(Qt.SolidLine)
        self.groupLessonTableWidget.setWordWrap(True)
        self.groupLessonTableWidget.setCornerButtonEnabled(True)
        self.groupLessonTableWidget.setRowCount(0)
        self.groupLessonTableWidget.setColumnCount(1)
        self.groupLessonTableWidget.horizontalHeader().setDefaultSectionSize(586)
        self.groupLessonTableWidget.horizontalHeader().setHighlightSections(False)
        self.groupLessonTableWidget.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.groupLessonTableWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addLesson = QPushButton(self.frame)
        self.addLesson.setObjectName(u"addLesson")

        self.horizontalLayout.addWidget(self.addLesson)

        self.lessonBox = QComboBox(self.frame)
        self.lessonBox.setObjectName(u"lessonBox")
        self.lessonBox.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lessonBox)

        self.deleteLesson = QPushButton(self.frame)
        self.deleteLesson.setObjectName(u"deleteLesson")

        self.horizontalLayout.addWidget(self.deleteLesson)

        self.verticalLayout.addWidget(self.frame)

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

        GroupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GroupWindow)

        QMetaObject.connectSlotsByName(GroupWindow)

    # setupUi

    def retranslateUi(self, GroupWindow):
        GroupWindow.setWindowTitle(QCoreApplication.translate("GroupWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("GroupWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        ___qtablewidgetitem = self.groupLessonTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("GroupWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None))
        self.addLesson.setText(
            QCoreApplication.translate("GroupWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteLesson.setText(
            QCoreApplication.translate("GroupWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.addButton.setText(
            QCoreApplication.translate("GroupWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(
            QCoreApplication.translate("GroupWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi
