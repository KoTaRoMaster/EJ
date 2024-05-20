import time

from PySide6.QtWidgets import QMainWindow, QWidget, QButtonGroup, QTableWidgetItem, QApplication, QAbstractItemView, \
    QComboBox
from PySide6.QtGui import QSinglePointEvent, QDrag
from PySide6.QtCore import Slot, QObject, Signal

import ui.reg_ui
from ui.main_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QMimeData, QMimeType
import threading
from data_sql import Connect
import os


class TableComboBox(QComboBox):
    speak = Signal()

    def __init__(self, column: int, row: int, con: Connect, ui: Ui_MainWindow):
        super(TableComboBox, self).__init__()
        self.speak.connect(self.updateSQLDate)
        self.column = column
        self.row = row
        self.text = None
        self.con = con
        self.ui = ui

    def speakingMethod(self, text):
        self.text = text
        self.speak.emit()

    def updateSQLDate(self):
        selectedDate = self.ui.calendarWidget.selectedDate().toPython()
        group = self.ui.adminSheduleTable.horizontalHeaderItem(self.column).text()
        idCount = self.row + 1
        lesson = self.ui.adminSheduleTable.cellWidget(self.row, self.column).currentText()
        lesson_ = ' '.join(lesson.split('\n')[0].split(' ')[:-1])
        schedule = self.con.get_schedule_group(selectedDate, group, idCount)
        if not schedule:
            if lesson_ != 'Нет':
                print('Insert_schedule', selectedDate, group, lesson_, idCount)
                self.con.insert_schedule(selectedDate, group, lesson_, idCount)
            return

        if schedule[0] != lesson_:
            if lesson_ == 'Нет':
                print('Delete_schedule', selectedDate, group, lesson, idCount)
                self.con.delete_schedule(selectedDate, group, idCount)
                return

            print('Update_schedule', selectedDate, group, lesson_, idCount)
            self.con.update_schedule(selectedDate, group, lesson_, idCount)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.con = Connect()
        # self.user = user
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.check = False
        self.items = []
        self.cellCheck = False

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(True)

        self.buttonGroup.addButton(self.ui.adminButton, 0)
        self.buttonGroup.addButton(self.ui.studentButton, 1)
        self.buttonGroup.addButton(self.ui.teacherButton, 2)

        self.buttonGroup.buttonClicked.connect(self.load)

        self.adminButtonGroup = QButtonGroup()
        self.adminButtonGroup.setExclusive(True)

        self.adminButtonGroup.addButton(self.ui.shedulesButton, 0)
        self.adminButtonGroup.addButton(self.ui.teachersButton, 1)
        self.adminButtonGroup.addButton(self.ui.studentsButton, 2)

        self.adminButtonGroup.buttonClicked.connect(self.adminButtons)

        self.ui.minimizeButton.clicked.connect(self.showMinMaxWindow)

        self.ui.lessonBox.currentIndexChanged.connect(self.load_groups)
        self.ui.groupBox.currentTextChanged.connect(self.load_group_teacher)

        self.ui.ratingWidget.cellChanged.connect(self.changedCell)

        self.ui.calendarWidget.clicked.connect(self.schedulesFrame)

        self.ui.exitButton.clicked.connect(self.close)

        self.ui.topMenu.mouseMoveEvent = self.moveWindow

        self.ui.menuButton.toggled.connect(self.menuButtonToggled)
        self.menuButtonToggled(False)

        # self.load()

    def adminButtons(self, button):
        id: int = self.adminButtonGroup.id(button)
        self.ui.adminStackedWidget.setCurrentIndex(id)
        match self.adminButtonGroup.button(id).text():
            case 'shedules':
                self.loadSchedulesFrame()
            case 'teachers':
                print('teachers')
            case 'students':
                print('students')

    def loadSchedulesFrame(self):
        groups = self.con.get_groups()
        self.ui.adminSheduleTable.setColumnCount(len(groups))
        cellSizeHorizontal = 190
        self.ui.adminSheduleTable.setMinimumSize(cellSizeHorizontal * len(groups) + 15, 461)
        self.ui.adminSheduleTable.setMaximumSize(cellSizeHorizontal * len(groups) + 15, 461)
        self.ui.adminSheduleTable.setHorizontalHeaderLabels(groups)
        for column in range(self.ui.adminSheduleTable.columnCount()):
            currentGroup = self.ui.adminSheduleTable.horizontalHeaderItem(column).text()
            lessons = self.con.get_lessons_group(currentGroup)
            lessons_ = [f'{lesson[0]} {lesson[1]}\n{lesson[3]} {lesson[2][0]}. {lesson[4][0]}.' for lesson in lessons]
            for row in range(self.ui.adminSheduleTable.rowCount()):
                scheduleComboBox = TableComboBox(column, row, self.con, self.ui)
                scheduleComboBox.addItem('Нет занятий')
                scheduleComboBox.addItems(lessons_)
                scheduleComboBox.currentTextChanged.connect(scheduleComboBox.speakingMethod)
                self.ui.adminSheduleTable.setCellWidget(row, column, scheduleComboBox)
        self.schedulesFrame()

    def schedulesFrame(self):
        selectedDate = self.ui.calendarWidget.selectedDate().toPython()
        schedules = self.con.get_schedule_admin(selectedDate)
        count = 0
        for column in range(self.ui.adminSheduleTable.columnCount()):
            currentGroup = self.ui.adminSheduleTable.horizontalHeaderItem(column).text()
            comboBox = self.ui.adminSheduleTable.cellWidget(0, column)
            comboBoxItems = [comboBox.itemText(i).split('\n')[0] for i in range(1, comboBox.count())]
            lessons = [' '.join(item.split(' ')[:-1]) for item in comboBoxItems]
            for row in range(self.ui.adminSheduleTable.rowCount()):
                if schedules and count < len(schedules) and currentGroup in schedules[count] and schedules[count][
                    3] == row + 1:
                    self.ui.adminSheduleTable.cellWidget(row, column).setCurrentIndex(
                        lessons.index(schedules[count][0]) + 1)
                    count += 1
                else:
                    self.ui.adminSheduleTable.cellWidget(row, column).setCurrentIndex(0)

    def menuButtonToggled(self, toggle):
        self.ui.leftMenu.setVisible(toggle)
        self.ui.leftMenu_2.setHidden(toggle)
        self.ui.mainWindows.setCurrentIndex(toggle)

    def changedCell(self, row, column):
        if not self.check:
            return

        if self.cellCheck:
            self.cellCheck = not self.cellCheck
            return

        ratingList = ['2', '3', '4', '5']
        rating = self.ui.ratingWidget.item(row, column).text()
        assessments = ''
        for i in range(len(rating)):
            if rating[i] not in ratingList:
                continue
            assessments += rating[i]

        result = ''
        for assessment in assessments:
            result += assessment + ','

        rating = result[:-1]
        date = self.ui.ratingWidget.horizontalHeaderItem(column).text()
        name = self.ui.ratingWidget.verticalHeaderItem(row).text()
        group = self.ui.groupBox.currentText()
        lesson = self.ui.lessonBox.currentText().split(',')[0]

        if not date:
            self.ui.ratingWidget.item(row, column).setText('')
            return

        if self.ui.ratingWidget.item(row, column).text() != rating:
            self.cellCheck = not self.cellCheck
        self.ui.ratingWidget.item(row, column).setText(rating)

        self.con.update_rating_group(assessments, date, name, group, lesson)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Backspace:
            if self.ui.ratingWidget.cellActivated:
                item = self.ui.ratingWidget.currentItem()
                if item:
                    item.setText('')

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragStartPos = event.pos()

    def moveWindow(self, event):
        self.move(event.globalPos() - self.dragStartPos)

    def load_group_teacher(self, button=''):
        lesson = self.ui.lessonBox.currentText().split(',')[0]
        group = self.ui.groupBox.currentText()
        if group == '':
            return
        rows = self.con.get_students_group(group)
        columns = self.con.get_groups_date_lesson(group, lesson)
        items = self.con.get_groups_rating_lesson(group, lesson)

        items_ = [(' '.join([names for names in item[:3]]), item[3], item[4]) for item in items]
        rows_ = [' '.join([names for names in row]) for row in rows]

        self.load_tale_widget(rows_, columns, items_)

    def showMinMaxWindow(self):
        if MainWindow.isMaximized(self):
            MainWindow.showNormal(self)
        else:
            MainWindow.showMaximized(self)

    def load(self, button):
        # print(self.user[3])
        # match self.user[3]:
        #     case 'admin':
        #         self.swap_to_admin()
        #     case 'student':
        #         self.swap_to_student()
        #     case 'teacher':
        #         self.swap_to_teacher('sidorenkov@mail.ru')
        self.ui.ratingWidget.clear()

        match button.text():
            case 'admin':
                self.swap_to_admin()
            case 'student':
                self.swap_to_student()
            case 'teacher':
                self.swap_to_teacher('sidorenkov@mail.ru')

    def swap_to_admin(self, email='admin@mail.ru'):
        user = self.con.get_admin(email)
        self.ui.leftTypeLabel.setText('Админ')
        self.ui.leftGroupLabel.setText('')
        self.ui.rightGroupLabel.setText('')
        self.ui.rightNameLabel.setText(f'{user[2]} {user[1][0]}. {user[3][0]}.')

    def swap_to_student(self, email='pubggrekov@mail.ru'):
        user = self.con.get_student(email)

        self.ui.leftTypeLabel.setText('Студент')
        self.ui.leftGroupLabel.setText('Группа')
        self.ui.rightGroupLabel.setText(user[5])
        self.ui.comboBoxFrame.setVisible(False)
        self.ui.rightNameLabel.setText(f'{user[2]} {user[1][0]}. {user[3][0]}.')

        self.ui.ratingWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        rows = self.con.get_lessons_student(email)
        columns = self.con.get_date_rating_student(email)
        items = self.con.get_assessment_rating_student(email)

        rows_ = [row[1] for row in rows]

        self.load_tale_widget(rows_, columns, items)

    def swap_to_teacher(self, email='shitova@gmail.com'):
        user = self.con.get_teacher(email)
        self.ui.leftTypeLabel.setText('Учитель')
        self.ui.leftGroupLabel.setText('')
        self.ui.rightGroupLabel.setText('')
        self.ui.rightNameLabel.setText(f'{user[2]} {user[1][0]}. {user[3][0]}.')
        self.ui.comboBoxFrame.setVisible(True)

        self.ui.ratingWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.AnyKeyPressed | QAbstractItemView.EditTrigger.DoubleClicked)

        lessons = self.con.get_lessons_teacher(email)
        lessons_ = [f'{lesson[0]}, {lesson[1]}' for lesson in lessons]

        self.ui.lessonBox.clear()

        self.ui.lessonBox.addItems(lessons_)

    def load_groups(self, button=''):
        lesson = self.ui.lessonBox.currentText()

        groups = self.con.get_groups_lesson(lesson.split(',')[0])
        groups_ = [f'{group[0]}' for group in groups]

        self.ui.groupBox.clear()

        self.ui.groupBox.addItems(groups_)

    def load_headers(self, rows, columns):
        rowCount = self.ui.ratingWidget.rowCount()
        columnCount = self.ui.ratingWidget.columnCount()

        if len(rows) > rowCount:
            rowCount = len(rows)
            self.ui.ratingWidget.setRowCount(rowCount)
        if len(columns) > columnCount:
            columnCount = len(columns)
            self.ui.ratingWidget.setColumnCount(columnCount)

        for x in range(columnCount):
            column = QTableWidgetItem()

            if x < len(columns):
                column.setText('.'.join(str(columns[x][0]).split('-')[1::]))
            else:
                column.setText('')

            self.ui.ratingWidget.setHorizontalHeaderItem(x, column)

        for y in range(rowCount):
            row = QTableWidgetItem()

            if y < len(rows):
                row.setText(str(rows[y]))
            else:
                row.setText('')

            self.ui.ratingWidget.setVerticalHeaderItem(y, row)

    def load_tale_widget(self, rows, columns, items):
        self.check = False
        self.ui.ratingWidget.clear()

        self.load_headers(rows, columns)

        dateList = [self.ui.ratingWidget.horizontalHeaderItem(i).text() for i in
                    range(self.ui.ratingWidget.columnCount()) if
                    self.ui.ratingWidget.horizontalHeaderItem(i).text() != '']
        lessonList = [self.ui.ratingWidget.verticalHeaderItem(i).text() for i in range(self.ui.ratingWidget.rowCount())
                      if self.ui.ratingWidget.verticalHeaderItem(i).text()]

        for item in items:
            row = lessonList.index(item[0])
            column = dateList.index(item[2].strftime('%m.%d'))
            qItem = self.ui.ratingWidget.item(row, column)
            if not qItem:
                qItem = QTableWidgetItem(str(item[1]))
                self.ui.ratingWidget.setItem(row, column, qItem)
                continue
            qItem.setText(f'{qItem.text()},{item[1]}')
        self.check = True
