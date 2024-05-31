from PySide6.QtWidgets import QMainWindow, QButtonGroup, QTableWidgetItem, QAbstractItemView, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtSvg import QSvgRenderer

from Windows.MainWindow import Ui_MainWindow
from Windows.StudentWindow import Ui_StudentWindow
from Windows.TeacherWindow import Ui_TeacherWindow

from CustomClasses.TableQPushButton import TableQPushButton
from CustomClasses.TableQComboBox import TableQComboBox

from data_sql import Connect
import re


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.con = Connect()
        # self.user = user
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Start StudentWindow
        self.studentWindow = QMainWindow()
        self.studentUi = Ui_StudentWindow()

        self.studentUi.setupUi(self.studentWindow)

        self.studentWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.studentWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        self.studentWindow.setWindowFlags(Qt.FramelessWindowHint)

        self.studentUi.cancelButton.clicked.connect(self.closeStudentWindow)
        # End StudentWindow

        # Start TeacherWindow
        self.teacherWindow = QMainWindow()
        self.teacherUi = Ui_TeacherWindow()

        self.teacherUi.setupUi(self.teacherWindow)

        self.teacherWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.teacherWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        self.teacherWindow.setWindowFlags(Qt.FramelessWindowHint)

        self.teacherUi.cancelButton.clicked.connect(self.closeTeacherWindow)
        # End TeacherWindow

        self.check = False
        self.items = []
        self.cellCheck = False

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.studentButton.setChecked(True)
        self.ui.teacherButton.setChecked(True)
        self.ui.adminButton.setChecked(True)

        self.adminButtonGroup = QButtonGroup()
        self.adminButtonGroup.setExclusive(True)

        self.adminButtonGroup.addButton(self.ui.adminShedulesButton, 0)
        self.adminButtonGroup.addButton(self.ui.adminTeachersButton, 1)
        self.adminButtonGroup.addButton(self.ui.adminStudentsButton, 2)
        self.adminButtonGroup.addButton(self.ui.adminGroupsButton, 3)
        self.adminButtonGroup.addButton(self.ui.adminLessonsButton, 4)

        self.adminButtonGroup.buttonClicked.connect(self.adminButtons)

        self.ui.addStudentButton.clicked.connect(self.addStudentWindowOpen)

        self.ui.minimizeButton.clicked.connect(self.showMinMaxWindow)

        self.ui.lessonBox.currentIndexChanged.connect(self.load_groups)
        self.ui.groupBox.currentTextChanged.connect(self.load_group_teacher)

        self.ui.ratingWidget.cellChanged.connect(self.changedCell)

        self.ui.calendarWidget.clicked.connect(self.schedulesFrame)

        self.ui.exitButton.clicked.connect(self.close)

        self.ui.topMenu.mouseMoveEvent = self.moveWindow

        # self.load()

    def adminButtons(self, button):
        id: int = self.adminButtonGroup.id(button)
        self.ui.adminStackedWidget.setCurrentIndex(id)
        match self.adminButtonGroup.button(id).text():
            case 'shedules':
                self.loadSchedulesFrame()
            case 'teachers':
                self.loadTeachersTable()
            case 'students':
                self.loadStudentsTable()

    def addButtonClicked(self):
        print('addButtonClicked')
        fullName = self.studentUi.fullNameInput.text()
        email = self.studentUi.emailInput.text()
        group = self.studentUi.groupBox.currentText()

        fullName_ = fullName.split(' ')
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_ = pattern.search(email)

        if any([False if 2 <= len(fullName_) <= 3 else True, False if email_ else True]):
            print('Неправильно введено ФИО или почта')
            return
        if self.con.get_user(email):
            print('Уже есть пользователь с такой почтой')
            return

        row = self.ui.studentTableWidget.rowCount()
        self.ui.studentTableWidget.setRowCount(row + 1)

        self.loadStudentTableItems(row, fullName, email, group)

        self.con.insert_student(fullName, email, group)
        self.closeStudentWindow()

    def closeTeacherWindow(self):
        self.teacherWindow.close()
        self.teacherUi.addButton.clicked.disconnect()

    def closeStudentWindow(self):
        self.studentWindow.close()
        self.studentUi.addButton.clicked.disconnect()

    def addStudentWindowOpen(self):
        self.studentUi.groupBox.clear()
        self.studentUi.fullNameInput.setText('')
        self.studentUi.emailInput.setText('')
        self.studentUi.addButton.setText('Добавить')

        self.studentUi.groupBox.addItems(self.con.get_groups())

        self.studentUi.addButton.clicked.connect(self.addButtonClicked)
        self.studentWindow.show()

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
        child = self.childAt(event.pos())

        if not child:
            return

        if child.objectName() != 'topMenu':
            return
        self.move(event.globalPos() - self.dragStartPos)

    def showMinMaxWindow(self):
        if MainWindow.isMaximized(self):
            MainWindow.showNormal(self)
        else:
            MainWindow.showMaximized(self)

    # LOAD FUNCTIONS

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
        lessonList = [self.ui.ratingWidget.verticalHeaderItem(i).text() for i in
                      range(self.ui.ratingWidget.rowCount())
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
                scheduleComboBox = TableQComboBox(column, row, self.con, self.ui)
                scheduleComboBox.addItem('Нет занятий')
                scheduleComboBox.addItems(lessons_)
                scheduleComboBox.currentTextChanged.connect(scheduleComboBox.updateSQLDate)
                self.ui.adminSheduleTable.setCellWidget(row, column, scheduleComboBox)
        self.schedulesFrame()

    def loadStudentsTable(self):
        students = self.con.get_students_all()
        rowCount = len(students)
        self.ui.studentTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            id, sName, sFirstname, sSecondName, email, group, index = students[row]
            sFullName = f'{sFirstname} {sName} {sSecondName}'
            self.loadStudentTableItems(row, sFullName, email, group)

    def loadStudentTableItems(self, row, name, email, group):

        itemFIO = QTableWidgetItem(name)
        self.ui.studentTableWidget.setItem(row, 0, itemFIO)

        itemEmail = QTableWidgetItem(email)
        self.ui.studentTableWidget.setItem(row, 1, itemEmail)

        itemGroup = QTableWidgetItem(group)
        self.ui.studentTableWidget.setItem(row, 2, itemGroup)

        qWidget = QWidget()
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        itemEdit.setStyleSheet(u"QPushButton {\n"
                               "	border-top-right-radius: 12px;\n"
                               "}\n"
                               "QPushButton::hover {\n"
                               "	background-color: rgb(36, 58, 72);\n"
                               "}\n"
                               "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditStudentWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        itemDelete.setStyleSheet(u"QPushButton {\n"
                                 "	border-top-right-radius: 12px;\n"
                                 "}\n"
                                 "QPushButton::hover {\n"
                                 "	background-color: rgb(36, 58, 72);\n"
                                 "}\n"
                                 "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteStudent)
        qHLayout.addWidget(itemDelete)

        self.ui.studentTableWidget.setCellWidget(row, 3, qWidget)

    def loadTeachersTable(self):
        teachers = self.con.get_teachers()
        rowCount = len(teachers)
        self.ui.teacherTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            id, sName, sFirstname, sSecondName, email, index = teachers[row]
            lessons = [' '.join([lesson[0], lesson[1]]) for lesson in self.con.get_lessons_teacher(email)]
            lessons_ = '\n'.join(lessons)
            sFullName = f'{sFirstname} {sName} {sSecondName}'
            self.loadTeachersTableItems(row, sFullName, email, lessons_)

    def loadTeachersTableItems(self, row, name, email, lessons):

        itemFIO = QTableWidgetItem(name)
        self.ui.teacherTableWidget.setItem(row, 0, itemFIO)

        itemEmail = QTableWidgetItem(email)
        self.ui.teacherTableWidget.setItem(row, 1, itemEmail)

        itemGroup = QTableWidgetItem(lessons)
        self.ui.teacherTableWidget.setItem(row, 2, itemGroup)

        qWidget = QWidget()
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        itemEdit.setStyleSheet(u"QPushButton {\n"
                               "	border-top-right-radius: 12px;\n"
                               "}\n"
                               "QPushButton::hover {\n"
                               "	background-color: rgb(36, 58, 72);\n"
                               "}\n"
                               "")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditTeacherWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        itemDelete.setStyleSheet(u"QPushButton {\n"
                                 "	border-top-right-radius: 12px;\n"
                                 "}\n"
                                 "QPushButton::hover {\n"
                                 "	background-color: rgb(36, 58, 72);\n"
                                 "}\n"
                                 "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteTeacher)
        qHLayout.addWidget(itemDelete)

        self.ui.teacherTableWidget.setCellWidget(row, 3, qWidget)
