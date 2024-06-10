# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowcaRwGf.ui'
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
        self.centralwidget.setStyleSheet(u"font: 14pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.centralwidget)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 32))
        self.topMenu.setMaximumSize(QSize(16777215, 32))
        self.topMenu.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius: 12px;\n"
"	border-top-right-radius: 12px;\n"
"	background-color: rgb(30, 31, 34);\n"
"}\n"
"QPushButton {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 46, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(53, 54, 60);\n"
"}")
        self.topMenu.setFrameShape(QFrame.StyledPanel)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topMenu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.topMenu)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(48, 32))
        self.menuButton.setMaximumSize(QSize(48, 32))
        self.menuButton.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 12px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))
        self.menuButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.menuButton)

        self.horizontalSpacer = QSpacerItem(1081, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.exitButton.setStyleSheet(u"QPushButton {\n"
"	border-top-right-radius: 12px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.exitButton.setIconSize(QSize(24, 24))
        self.exitButton.setCheckable(False)
        self.exitButton.setChecked(False)
        self.exitButton.setAutoDefault(False)
        self.exitButton.setFlat(False)

        self.horizontalLayout.addWidget(self.exitButton)


        self.verticalLayout_2.addWidget(self.topMenu)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton {\n"
"	border-radius: 4px;\n"
"	background-color: rgb(71, 80, 83);\n"
"	font: 22pt ;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(53, 54, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30, 31, 34);\n"
" }")
        self.mainMenu = QHBoxLayout(self.widget)
        self.mainMenu.setSpacing(0)
        self.mainMenu.setObjectName(u"mainMenu")
        self.mainMenu.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.widget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setFocusPolicy(Qt.StrongFocus)
        self.leftMenu.setStyleSheet(u"QFrame {\n"
"	border-bottom-left-radius: 12px;\n"
"	background-color: rgb(43, 45, 49);\n"
"}")
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
"	border-bottom-right-radius: 12px;\n"
"	background-color: rgb(49, 51, 56);\n"
"}\n"
"")
        self.adminPage = QWidget()
        self.adminPage.setObjectName(u"adminPage")
        self.verticalLayout_10 = QVBoxLayout(self.adminPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.adminStackedWidget = QStackedWidget(self.adminPage)
        self.adminStackedWidget.setObjectName(u"adminStackedWidget")
        self.adminStackedWidget.setStyleSheet(u"QTableWidget, QHeaderView   {\n"
"	font: 8pt \"Roboto\";\n"
"}\n"
"\n"
"QHeaderView::section, QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(71, 80, 83);\n"
"    padding: 4px;\n"
"    border: 1px solid #fffff8;\n"
"	font: 11pt \"Roboto\";\n"
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
"QTableWidget::item {\n"
"	color: rgb(220, 220, 220);\n"
"	font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QWidget QPushButton {\n"
"	border-radius: 4px;\n"
"	background-color: rgb(71, 80, 83);\n"
"	font: 22pt ;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(53, 54, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(30, 31, 34);\n"
" }\n"
"QWidget {\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.shedules = QWidget()
        self.shedules.setObjectName(u"shedules")
        self.verticalLayout_9 = QVBoxLayout(self.shedules)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.shedules)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(410, 0, 281, 191))
        self.calendarWidget.setStyleSheet(u"\n"
"QCalendarWidget QMenu {\n"
"  	width: 150px;\n"
"  	left: 20px;\n"
"  	color: white;\n"
"  	font-size: 18px;\n"
"  	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
" QCalendarWidget QSpinBox {\n"
"	width: 150px;\n"
"  	font-size:24px; \n"
"  	color: white; \n"
"  	selection-background-color: rgb(136, 136, 136);\n"
"  	selection-color: rgb(255, 255, 255);\n"
"}\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	color: rgb(180, 180, 180);  \n"
"  	background-color: black;  \n"
"  	selection-background-color: rgb(64, 64, 64); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}\n"
"\n"
"")
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
        self.adminSheduleTable.setStyleSheet(u"QComboBox {\n"
"	font: 12px;\n"
"	border-radius: 2px;\n"
"	color: rgb(220, 220, 220);\n"
"	background: rgb(37, 39, 42);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item::selected {\n"
"	background-color: rgb(30, 31, 34);\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item::hover {\n"
"	background-color: rgb(30, 31, 34);\n"
"}")
        self.adminSheduleTable.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.adminSheduleTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
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
        self.verticalLayout_13 = QVBoxLayout(self.teachers)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.teacherTableWidget = QTableWidget(self.teachers)
        if (self.teacherTableWidget.columnCount() < 5):
            self.teacherTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.teacherTableWidget.setObjectName(u"teacherTableWidget")
        self.teacherTableWidget.setStyleSheet(u"")
        self.teacherTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teacherTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.teacherTableWidget.setRowCount(0)
        self.teacherTableWidget.setColumnCount(5)
        self.teacherTableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.teacherTableWidget.horizontalHeader().setDefaultSectionSize(201)

        self.verticalLayout_13.addWidget(self.teacherTableWidget)

        self.addTeacherButton = QPushButton(self.teachers)
        self.addTeacherButton.setObjectName(u"addTeacherButton")
        self.addTeacherButton.setStyleSheet(u"QPushButton {\n"
"	margin: 10px;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.addTeacherButton)

        self.adminStackedWidget.addWidget(self.teachers)
        self.students = QWidget()
        self.students.setObjectName(u"students")
        self.students.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.students)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.studentTableWidget = QTableWidget(self.students)
        if (self.studentTableWidget.columnCount() < 4):
            self.studentTableWidget.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.studentTableWidget.setObjectName(u"studentTableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.studentTableWidget.sizePolicy().hasHeightForWidth())
        self.studentTableWidget.setSizePolicy(sizePolicy)
        self.studentTableWidget.setLayoutDirection(Qt.LeftToRight)
        self.studentTableWidget.setAutoFillBackground(False)
        self.studentTableWidget.setStyleSheet(u"")
        self.studentTableWidget.setFrameShape(QFrame.NoFrame)
        self.studentTableWidget.setLineWidth(1)
        self.studentTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.studentTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.studentTableWidget.setRowCount(0)
        self.studentTableWidget.setColumnCount(4)
        self.studentTableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.studentTableWidget.horizontalHeader().setDefaultSectionSize(260)

        self.verticalLayout_12.addWidget(self.studentTableWidget)

        self.addStudentButton = QPushButton(self.students)
        self.addStudentButton.setObjectName(u"addStudentButton")
        self.addStudentButton.setStyleSheet(u"QPushButton {\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_12.addWidget(self.addStudentButton)

        self.adminStackedWidget.addWidget(self.students)
        self.groups = QWidget()
        self.groups.setObjectName(u"groups")
        self.verticalLayout_14 = QVBoxLayout(self.groups)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.groupTableWidget = QTableWidget(self.groups)
        if (self.groupTableWidget.columnCount() < 3):
            self.groupTableWidget.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.groupTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.groupTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.groupTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.groupTableWidget.setObjectName(u"groupTableWidget")
        self.groupTableWidget.setStyleSheet(u"")
        self.groupTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.groupTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.groupTableWidget.setRowCount(0)
        self.groupTableWidget.setColumnCount(3)
        self.groupTableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.groupTableWidget.horizontalHeader().setDefaultSectionSize(347)

        self.verticalLayout_14.addWidget(self.groupTableWidget)

        self.addGroupButton = QPushButton(self.groups)
        self.addGroupButton.setObjectName(u"addGroupButton")
        self.addGroupButton.setStyleSheet(u"QPushButton {\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_14.addWidget(self.addGroupButton)

        self.adminStackedWidget.addWidget(self.groups)
        self.lessons = QWidget()
        self.lessons.setObjectName(u"lessons")
        self.verticalLayout_17 = QVBoxLayout(self.lessons)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lessonTableWidget = QTableWidget(self.lessons)
        if (self.lessonTableWidget.columnCount() < 3):
            self.lessonTableWidget.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.lessonTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.lessonTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.lessonTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        self.lessonTableWidget.setObjectName(u"lessonTableWidget")
        self.lessonTableWidget.setStyleSheet(u"")
        self.lessonTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lessonTableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.lessonTableWidget.setRowCount(0)
        self.lessonTableWidget.setColumnCount(3)
        self.lessonTableWidget.horizontalHeader().setMinimumSectionSize(35)
        self.lessonTableWidget.horizontalHeader().setDefaultSectionSize(336)

        self.verticalLayout_17.addWidget(self.lessonTableWidget)

        self.addLessonButton = QPushButton(self.lessons)
        self.addLessonButton.setObjectName(u"addLessonButton")
        self.addLessonButton.setStyleSheet(u"QPushButton {\n"
"	margin: 10px;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.addLessonButton)

        self.adminStackedWidget.addWidget(self.lessons)

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
        self.ratingTopFrame.setStyleSheet(u"border-radius: 0px;")
        self.ratingTopFrame.setFrameShape(QFrame.StyledPanel)
        self.ratingTopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ratingTopFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBoxFrame = QFrame(self.ratingTopFrame)
        self.comboBoxFrame.setObjectName(u"comboBoxFrame")
        self.comboBoxFrame.setMinimumSize(QSize(400, 0))
        self.comboBoxFrame.setMaximumSize(QSize(400, 16777215))
        self.comboBoxFrame.setStyleSheet(u"QComboBox {\n"
"	font: 16px;\n"
"	border-radius: 2px;\n"
"	color: rgb(220, 220, 220);\n"
"	background: rgb(37, 39, 42);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	font: 12px;\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    border: none;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item::selected {\n"
"	background-color: rgb(30, 31, 34);\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item::hover {\n"
"	background-color: rgb(30, 31, 34);\n"
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
        self.ratingWidget.setObjectName(u"ratingWidget")
        self.ratingWidget.setEnabled(True)
        self.ratingWidget.setFocusPolicy(Qt.StrongFocus)
        self.ratingWidget.setStyleSheet(u"QTableWidget, QHeaderView   {\n"
"	font: 8pt \"Roboto\";\n"
"}\n"
"\n"
"QHeaderView::section, QTableWidget QTableCornerButton::section {\n"
"	background-color: rgb(71, 80, 83);\n"
"    padding: 4px;\n"
"    border: 1px solid #fffff8;\n"
"	font: 12pt \"Roboto\";\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(30, 31, 34);\n"
"    gridline-color: #fffff8;\n"
"	font: 11pt \"Roboto\";\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"QTableWidget::item::pressed {\n"
"	font: 10pt \"Roboto\";\n"
"	color: rgb(220, 220, 220);\n"
"\n"
"}\n"
"QTableWidget::item::selected {\n"
"	background-color: rgb(84, 87, 95);\n"
"}\n"
"QWidget {\n"
"	border-radius: 0px;\n"
"	font: 11pt \"Roboto\";\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"")
        self.ratingWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
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
        self.ratingWidget.horizontalHeader().setMinimumSectionSize(55)
        self.ratingWidget.horizontalHeader().setDefaultSectionSize(55)
        self.ratingWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.ratingWidget.horizontalHeader().setStretchLastSection(False)
        self.ratingWidget.verticalHeader().setVisible(True)
        self.ratingWidget.verticalHeader().setCascadingSectionResizes(False)
        self.ratingWidget.verticalHeader().setMinimumSectionSize(45)
        self.ratingWidget.verticalHeader().setDefaultSectionSize(45)
        self.ratingWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.ratingWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.ratingWidget)


        self.verticalLayout.addWidget(self.ratingFrame_2)

        self.mainWindows.addWidget(self.ratingFrame)

        self.mainMenu.addWidget(self.mainWindows)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuButton.toggled.connect(self.leftMenu.setHidden)
        self.studentButton.toggled.connect(self.studentButtonsFrame.setHidden)
        self.teacherButton.toggled.connect(self.teacherButtonsFrame.setHidden)
        self.adminButton.toggled.connect(self.adminButtonsFrame.setHidden)
        self.restoreButton.clicked.connect(MainWindow.lower)

        self.exitButton.setDefault(False)
        self.mainWindows.setCurrentIndex(0)
        self.adminStackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.restoreButton.setText("")
        self.minimizeButton.setText("")
        self.exitButton.setText("")
        self.studentButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))
        self.studentSchedule.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.teacherButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0438\u0442\u0435\u043b\u044c", None))
        self.teacherSchedule.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.adminButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.adminShedulesButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.adminTeachersButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0438\u0442\u0435\u043b\u044c", None))
        self.adminStudentsButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b", None))
        self.adminGroupsButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.adminLessonsButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b", None))
        self.optionsButtons.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.leaveButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        ___qtablewidgetitem = self.teacherTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem1 = self.teacherTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None));
        ___qtablewidgetitem2 = self.teacherTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b", None));
        ___qtablewidgetitem3 = self.teacherTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        self.addTeacherButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0438\u0442\u0435\u043b\u044f", None))
        ___qtablewidgetitem4 = self.studentTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None));
        ___qtablewidgetitem5 = self.studentTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0447\u0442\u0430", None));
        ___qtablewidgetitem6 = self.studentTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        self.addStudentButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        ___qtablewidgetitem7 = self.groupTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
        ___qtablewidgetitem8 = self.groupTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b", None));
        self.addGroupButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443", None))
        ___qtablewidgetitem9 = self.lessonTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem10 = self.lessonTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None));
        self.addLessonButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0435\u0434\u043c\u0435\u0442", None))
        self.leftTypeLabel.setText(QCoreApplication.translate("MainWindow", u"lType", None))
        self.leftNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.leftGroupLabel.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.rightTypeLabel.setText("")
        self.rightNameLabel.setText(QCoreApplication.translate("MainWindow", u"rName", None))
        self.rightGroupLabel.setText(QCoreApplication.translate("MainWindow", u"rGroup", None))
    # retranslateUi

