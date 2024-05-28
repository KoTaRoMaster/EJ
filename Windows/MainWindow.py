# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maineiyYLl.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
                               QFrame, QHBoxLayout, QHeaderView, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)
import res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
                                         "border-radius: 12px;\n"
                                         "background-color: rgb(30, 31, 34);\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.startFrame = QVBoxLayout()
        self.startFrame.setSpacing(0)
        self.startFrame.setObjectName(u"startFrame")
        self.topMenu = QFrame(self.centralwidget)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 32))
        self.topMenu.setMaximumSize(QSize(16777215, 32))
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.menuButton = QPushButton(self.topMenu)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(48, 32))
        self.menuButton.setMaximumSize(QSize(48, 32))
        self.menuButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))
        self.menuButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.menuButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.restoreButton = QPushButton(self.topMenu)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setEnabled(True)
        self.restoreButton.setMinimumSize(QSize(48, 32))
        self.restoreButton.setMaximumSize(QSize(48, 32))
        self.restoreButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setIconSize(QSize(24, 24))
        self.restoreButton.setCheckable(False)

        self.horizontalLayout.addWidget(self.restoreButton)

        self.minimizeButton = QPushButton(self.topMenu)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(48, 32))
        self.minimizeButton.setMaximumSize(QSize(48, 32))
        self.minimizeButton.setFocusPolicy(Qt.StrongFocus)
        self.minimizeButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/toast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.minimizeButton)

        self.exitButton = QPushButton(self.topMenu)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setEnabled(True)
        self.exitButton.setMinimumSize(QSize(48, 32))
        self.exitButton.setMaximumSize(QSize(48, 32))
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.exitButton.setIconSize(QSize(24, 24))
        self.exitButton.setCheckable(False)
        self.exitButton.setChecked(False)
        self.exitButton.setAutoDefault(False)
        self.exitButton.setFlat(False)

        self.horizontalLayout.addWidget(self.exitButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.startFrame.addWidget(self.topMenu)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
                                  "	background-color: rgb(49, 51, 56);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton {\n"
                                  "	border-radius: 5px; \n"
                                  "	border: 1.5px solid rgb(91,231,255); \n"
                                  "	background-color: white; \n"
                                  "	font: 22pt \"Segoe Print\";\n"
                                  "	color: rgb(255, 255, 255);\n"
                                  "	background-color: rgb(74, 118, 148);\n"
                                  "	transition: background-color 2s ease-out 100ms\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "	border: 1.4px solid rgb(73,186,205);\n"
                                  " }\n"
                                  "QPushButton:hover {\n"
                                  "	font-size: 16px;\n"
                                  "	background-color: rgb(109, 174, 218);\n"
                                  "}")
        self.mainMenu = QHBoxLayout(self.widget)
        self.mainMenu.setSpacing(0)
        self.mainMenu.setObjectName(u"mainMenu")
        self.mainMenu.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.widget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setFocusPolicy(Qt.StrongFocus)
        self.leftMenu.setStyleSheet(u"QFrame {\n"
                                    "	border-top-left-radius: 0;\n"
                                    "	border-top-right-radius: 0;\n"
                                    "	border-bottom-right-radius: 0;\n"
                                    "	background-color: rgb(43, 45, 49);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.studentButton = QPushButton(self.leftMenu)
        self.studentButton.setObjectName(u"studentButton")
        self.studentButton.setEnabled(True)
        self.studentButton.setStyleSheet(u"")
        self.studentButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.studentButton)

        self.studentButtonsFrame = QFrame(self.leftMenu)
        self.studentButtonsFrame.setObjectName(u"studentButtonsFrame")
        self.studentButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.studentButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.studentButtonsFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.studentSchedule = QPushButton(self.studentButtonsFrame)
        self.studentSchedule.setObjectName(u"studentSchedule")

        self.verticalLayout_15.addWidget(self.studentSchedule)

        self.verticalLayout_3.addWidget(self.studentButtonsFrame)

        self.teacherButton = QPushButton(self.leftMenu)
        self.teacherButton.setObjectName(u"teacherButton")
        self.teacherButton.setEnabled(True)
        self.teacherButton.setStyleSheet(u"")
        self.teacherButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.teacherButton)

        self.teacherButtonsFrame = QFrame(self.leftMenu)
        self.teacherButtonsFrame.setObjectName(u"teacherButtonsFrame")
        self.teacherButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.teacherButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.teacherButtonsFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.teacherSchedule = QPushButton(self.teacherButtonsFrame)
        self.teacherSchedule.setObjectName(u"teacherSchedule")

        self.verticalLayout_16.addWidget(self.teacherSchedule)

        self.verticalLayout_3.addWidget(self.teacherButtonsFrame)

        self.adminButton = QPushButton(self.leftMenu)
        self.adminButton.setObjectName(u"adminButton")
        self.adminButton.setEnabled(True)
        self.adminButton.setStyleSheet(u"")
        self.adminButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.adminButton)

        self.adminButtonsFrame = QFrame(self.leftMenu)
        self.adminButtonsFrame.setObjectName(u"adminButtonsFrame")
        self.adminButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.adminButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.adminButtonsFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.adminShedulesButton = QPushButton(self.adminButtonsFrame)
        self.adminShedulesButton.setObjectName(u"adminShedulesButton")

        self.verticalLayout_11.addWidget(self.adminShedulesButton)

        self.adminTeachersButton = QPushButton(self.adminButtonsFrame)
        self.adminTeachersButton.setObjectName(u"adminTeachersButton")

        self.verticalLayout_11.addWidget(self.adminTeachersButton)

        self.adminStudentsButton = QPushButton(self.adminButtonsFrame)
        self.adminStudentsButton.setObjectName(u"adminStudentsButton")

        self.verticalLayout_11.addWidget(self.adminStudentsButton)

        self.adminGroupsButton = QPushButton(self.adminButtonsFrame)
        self.adminGroupsButton.setObjectName(u"adminGroupsButton")

        self.verticalLayout_11.addWidget(self.adminGroupsButton)

        self.adminLessonsButton = QPushButton(self.adminButtonsFrame)
        self.adminLessonsButton.setObjectName(u"adminLessonsButton")

        self.verticalLayout_11.addWidget(self.adminLessonsButton)

        self.verticalLayout_3.addWidget(self.adminButtonsFrame)

        self.optionsButtons = QPushButton(self.leftMenu)
        self.optionsButtons.setObjectName(u"optionsButtons")

        self.verticalLayout_3.addWidget(self.optionsButtons)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.leaveButton = QPushButton(self.leftMenu)
        self.leaveButton.setObjectName(u"leaveButton")

        self.verticalLayout_3.addWidget(self.leaveButton)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.mainMenu.addWidget(self.leftMenu)

        self.mainWindows = QStackedWidget(self.widget)
        self.mainWindows.setObjectName(u"mainWindows")
        self.mainWindows.setEnabled(True)
        self.mainWindows.setStyleSheet(u"QWidget {\n"
                                       "	border-top-left-radius: 0;\n"
                                       "	border-top-right-radius: 0;\n"
                                       "	border-bottom-left-radius: 0;\n"
                                       "}")
        self.adminPage = QWidget()
        self.adminPage.setObjectName(u"adminPage")
        self.verticalLayout_10 = QVBoxLayout(self.adminPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 30, 0)
        self.adminStackedWidget = QStackedWidget(self.adminPage)
        self.adminStackedWidget.setObjectName(u"adminStackedWidget")
        self.adminStackedWidget.setStyleSheet(u"background-color: rgb(255, 134, 229);")
        self.shedules = QWidget()
        self.shedules.setObjectName(u"shedules")
        self.verticalLayout_9 = QVBoxLayout(self.shedules)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 300)
        self.frame = QFrame(self.shedules)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(480, 0, 312, 191))
        self.calendarWidget.setInputMethodHints(Qt.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.verticalLayout_9.addWidget(self.frame)

        self.adminSheduleTable = QTableWidget(self.shedules)
        if (self.adminSheduleTable.columnCount() < 20):
            self.adminSheduleTable.setColumnCount(20)
        if (self.adminSheduleTable.rowCount() < 7):
            self.adminSheduleTable.setRowCount(7)
        self.adminSheduleTable.setObjectName(u"adminSheduleTable")
        self.adminSheduleTable.setMinimumSize(QSize(600, 461))
        self.adminSheduleTable.setMaximumSize(QSize(16777215, 16777215))
        self.adminSheduleTable.setStyleSheet(u"background-color: rgb(148, 156, 158);")
        self.adminSheduleTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.adminSheduleTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.adminSheduleTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.adminSheduleTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.adminSheduleTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.adminSheduleTable.setRowCount(7)
        self.adminSheduleTable.setColumnCount(20)
        self.adminSheduleTable.horizontalHeader().setVisible(True)
        self.adminSheduleTable.horizontalHeader().setMinimumSectionSize(0)
        self.adminSheduleTable.horizontalHeader().setDefaultSectionSize(170)
        self.adminSheduleTable.horizontalHeader().setHighlightSections(False)
        self.adminSheduleTable.verticalHeader().setVisible(True)
        self.adminSheduleTable.verticalHeader().setMinimumSectionSize(0)
        self.adminSheduleTable.verticalHeader().setDefaultSectionSize(60)
        self.adminSheduleTable.verticalHeader().setHighlightSections(False)

        self.verticalLayout_9.addWidget(self.adminSheduleTable)

        self.adminStackedWidget.addWidget(self.shedules)
        self.teachers = QWidget()
        self.teachers.setObjectName(u"teachers")
        self.label_3 = QLabel(self.teachers)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 240, 49, 16))
        self.adminStackedWidget.addWidget(self.teachers)
        self.students = QWidget()
        self.students.setObjectName(u"students")
        self.label_2 = QLabel(self.students)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 49, 16))
        self.studentTableWidget = QTableWidget(self.students)
        if (self.studentTableWidget.columnCount() < 4):
            self.studentTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.studentTableWidget.setObjectName(u"studentTableWidget")
        self.studentTableWidget.setGeometry(QRect(0, 100, 851, 481))
        self.studentTableWidget.setStyleSheet(u"background-color: rgb(61, 86, 115);")
        self.studentTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.studentTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.studentTableWidget.setRowCount(0)
        self.studentTableWidget.setColumnCount(4)
        self.studentTableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.studentTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.addStudentButton = QPushButton(self.students)
        self.addStudentButton.setObjectName(u"addStudentButton")
        self.addStudentButton.setGeometry(QRect(110, 620, 471, 24))
        self.addStudentButton.setStyleSheet(u"background-color: rgb(52, 83, 104);")
        self.adminStackedWidget.addWidget(self.students)

        self.verticalLayout_10.addWidget(self.adminStackedWidget)

        self.mainWindows.addWidget(self.adminPage)
        self.ratingFrame = QWidget()
        self.ratingFrame.setObjectName(u"ratingFrame")
        self.ratingFrame.setMinimumSize(QSize(0, 682))
        self.ratingFrame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.ratingFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ratingTopFrame = QFrame(self.ratingFrame)
        self.ratingTopFrame.setObjectName(u"ratingTopFrame")
        self.ratingTopFrame.setMinimumSize(QSize(0, 100))
        self.ratingTopFrame.setFrameShape(QFrame.StyledPanel)
        self.ratingTopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ratingTopFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBoxFrame = QFrame(self.ratingTopFrame)
        self.comboBoxFrame.setObjectName(u"comboBoxFrame")
        self.comboBoxFrame.setMinimumSize(QSize(200, 0))
        self.comboBoxFrame.setMaximumSize(QSize(200, 16777215))
        self.comboBoxFrame.setStyleSheet(u"QComboBox {\n"
                                         "	\n"
                                         "	background-color: rgb(134, 255, 255);\n"
                                         "}")
        self.comboBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.comboBoxFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.comboBoxFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.lessonBox = QComboBox(self.comboBoxFrame)
        self.lessonBox.setObjectName(u"lessonBox")

        self.verticalLayout_5.addWidget(self.lessonBox)

        self.groupBox = QComboBox(self.comboBoxFrame)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout_5.addWidget(self.groupBox)

        self.horizontalLayout_4.addWidget(self.comboBoxFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.userInfroFrame = QFrame(self.ratingTopFrame)
        self.userInfroFrame.setObjectName(u"userInfroFrame")
        self.userInfroFrame.setMinimumSize(QSize(300, 0))
        self.userInfroFrame.setMaximumSize(QSize(300, 16777215))
        self.userInfroFrame.setStyleSheet(u"background-color: rgb(255, 216, 253);")
        self.userInfroFrame.setFrameShape(QFrame.StyledPanel)
        self.userInfroFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.userInfroFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.infroFrame = QFrame(self.userInfroFrame)
        self.infroFrame.setObjectName(u"infroFrame")
        self.infroFrame.setStyleSheet(u"background-color: rgb(229, 249, 255);")
        self.infroFrame.setFrameShape(QFrame.StyledPanel)
        self.infroFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.infroFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lefrInfoFrame = QFrame(self.infroFrame)
        self.lefrInfoFrame.setObjectName(u"lefrInfoFrame")
        self.lefrInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.lefrInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.lefrInfoFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 0, 9)
        self.leftTypeLabel = QLabel(self.lefrInfoFrame)
        self.leftTypeLabel.setObjectName(u"leftTypeLabel")

        self.verticalLayout_7.addWidget(self.leftTypeLabel)

        self.leftNameLabel = QLabel(self.lefrInfoFrame)
        self.leftNameLabel.setObjectName(u"leftNameLabel")

        self.verticalLayout_7.addWidget(self.leftNameLabel)

        self.leftGroupLabel = QLabel(self.lefrInfoFrame)
        self.leftGroupLabel.setObjectName(u"leftGroupLabel")

        self.verticalLayout_7.addWidget(self.leftGroupLabel)

        self.horizontalLayout_6.addWidget(self.lefrInfoFrame)

        self.rightInfoFrame = QFrame(self.infroFrame)
        self.rightInfoFrame.setObjectName(u"rightInfoFrame")
        self.rightInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.rightInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.rightInfoFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.rightTypeLabel = QLabel(self.rightInfoFrame)
        self.rightTypeLabel.setObjectName(u"rightTypeLabel")

        self.verticalLayout_6.addWidget(self.rightTypeLabel)

        self.rightNameLabel = QLabel(self.rightInfoFrame)
        self.rightNameLabel.setObjectName(u"rightNameLabel")

        self.verticalLayout_6.addWidget(self.rightNameLabel)

        self.rightGroupLabel = QLabel(self.rightInfoFrame)
        self.rightGroupLabel.setObjectName(u"rightGroupLabel")

        self.verticalLayout_6.addWidget(self.rightGroupLabel)

        self.horizontalLayout_6.addWidget(self.rightInfoFrame)

        self.horizontalLayout_5.addWidget(self.infroFrame)

        self.imageFrame = QFrame(self.userInfroFrame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.imageFrame)

        self.horizontalLayout_4.addWidget(self.userInfroFrame)

        self.verticalLayout.addWidget(self.ratingTopFrame)

        self.ratingFrame_2 = QFrame(self.ratingFrame)
        self.ratingFrame_2.setObjectName(u"ratingFrame_2")
        self.ratingFrame_2.setStyleSheet(u"")
        self.ratingFrame_2.setFrameShape(QFrame.StyledPanel)
        self.ratingFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.ratingFrame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ratingWidget = QTableWidget(self.ratingFrame_2)
        if (self.ratingWidget.columnCount() < 39):
            self.ratingWidget.setColumnCount(39)
        if (self.ratingWidget.rowCount() < 22):
            self.ratingWidget.setRowCount(22)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ratingWidget.setItem(1, 0, __qtablewidgetitem4)
        self.ratingWidget.setObjectName(u"ratingWidget")
        self.ratingWidget.setEnabled(True)
        self.ratingWidget.setFocusPolicy(Qt.StrongFocus)
        self.ratingWidget.setStyleSheet(u"QTableWidget, QHeaderView   {\n"
                                        "    background-color: #333333;\n"
                                        "    color: #fffff8;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section, QTableWidget QTableCornerButton::section {\n"
                                        "    background-color: #646464;\n"
                                        "    padding: 4px;\n"
                                        "    border: 1px solid #fffff8;\n"
                                        "    font-size: 10pt;\n"
                                        "}\n"
                                        "\n"
                                        "QHeaderView::section:vertical {\n"
                                        "   width: 150px;\n"
                                        "}\n"
                                        "\n"
                                        "QTableWidget {\n"
                                        "    gridline-color: #fffff8;\n"
                                        "    font-size: 12pt;\n"
                                        "}\n"
                                        "QTableWidget::item::selected {\n"
                                        "	\n"
                                        "	background-color: rgb(27, 27, 27);\n"
                                        "}\n"
                                        "")
        self.ratingWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed | QAbstractItemView.DoubleClicked)
        self.ratingWidget.setDragEnabled(False)
        self.ratingWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ratingWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ratingWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.ratingWidget.setShowGrid(True)
        self.ratingWidget.setGridStyle(Qt.CustomDashLine)
        self.ratingWidget.setSortingEnabled(False)
        self.ratingWidget.setWordWrap(True)
        self.ratingWidget.setCornerButtonEnabled(True)
        self.ratingWidget.setRowCount(22)
        self.ratingWidget.setColumnCount(39)
        self.ratingWidget.horizontalHeader().setVisible(True)
        self.ratingWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.ratingWidget.horizontalHeader().setMinimumSectionSize(40)
        self.ratingWidget.horizontalHeader().setDefaultSectionSize(40)
        self.ratingWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.ratingWidget.horizontalHeader().setStretchLastSection(False)
        self.ratingWidget.verticalHeader().setVisible(True)
        self.ratingWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ratingWidget.verticalHeader().setMinimumSectionSize(40)
        self.ratingWidget.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_8.addWidget(self.ratingWidget)

        self.verticalLayout.addWidget(self.ratingFrame_2)

        self.mainWindows.addWidget(self.ratingFrame)

        self.mainMenu.addWidget(self.mainWindows)

        self.startFrame.addWidget(self.widget)

        self.verticalLayout_2.addLayout(self.startFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.restoreButton.clicked.connect(MainWindow.lower)
        self.menuButton.toggled.connect(self.leftMenu.setHidden)
        self.studentButton.toggled.connect(self.studentButtonsFrame.setHidden)
        self.teacherButton.toggled.connect(self.teacherButtonsFrame.setHidden)
        self.adminButton.toggled.connect(self.adminButtonsFrame.setHidden)

        self.exitButton.setDefault(False)
        self.mainWindows.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.restoreButton.setText("")
        self.minimizeButton.setText("")
        self.exitButton.setText("")
        self.studentButton.setText(QCoreApplication.translate("MainWindow", u"student", None))
        self.studentSchedule.setText(QCoreApplication.translate("MainWindow", u"shedules", None))
        self.teacherButton.setText(QCoreApplication.translate("MainWindow", u"teacher", None))
        self.teacherSchedule.setText(QCoreApplication.translate("MainWindow", u"shedules", None))
        self.adminButton.setText(QCoreApplication.translate("MainWindow", u"admin", None))
        self.adminShedulesButton.setText(QCoreApplication.translate("MainWindow", u"shedules", None))
        self.adminTeachersButton.setText(QCoreApplication.translate("MainWindow", u"teachers", None))
        self.adminStudentsButton.setText(QCoreApplication.translate("MainWindow", u"students", None))
        self.adminGroupsButton.setText(QCoreApplication.translate("MainWindow", u"groups", None))
        self.adminLessonsButton.setText(QCoreApplication.translate("MainWindow", u"lessons", None))
        self.optionsButtons.setText(QCoreApplication.translate("MainWindow", u"options", None))
        self.leaveButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"teachers", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"students", None))
        ___qtablewidgetitem = self.studentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.studentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None));
        ___qtablewidgetitem2 = self.studentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        self.addStudentButton.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0435\u043d\u0438\u043a\u0430",
                                                                 None))
        self.leftTypeLabel.setText(QCoreApplication.translate("MainWindow", u"lType", None))
        self.leftNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.leftGroupLabel.setText(
            QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.rightTypeLabel.setText("")
        self.rightNameLabel.setText(QCoreApplication.translate("MainWindow", u"rName", None))
        self.rightGroupLabel.setText(QCoreApplication.translate("MainWindow", u"rGroup", None))

        __sortingEnabled = self.ratingWidget.isSortingEnabled()
        self.ratingWidget.setSortingEnabled(False)
        self.ratingWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi


from PySide6.QtSvg import QSvgRenderer
