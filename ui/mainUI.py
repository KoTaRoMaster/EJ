from PySide6.QtWidgets import QMainWindow, QButtonGroup, QTableWidgetItem, QAbstractItemView, QWidget, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtSvg import QSvgRenderer

from Windows.MainWindow import Ui_MainWindow
from Windows.StudentWindow import Ui_StudentWindow
from Windows.TeacherWindow import Ui_TeacherWindow
from Windows.LessonWiindow import Ui_LessonWindow
from Windows.GroupWindow import Ui_GroupWindow

from CustomClasses.TableQPushButton import TableQPushButton
from CustomClasses.TableQComboBox import TableQComboBox

from data_sql import Connect
import re


class MainWindow(QMainWindow):
    def __init__(self, user, con: Connect, regUi: QMainWindow):
        QMainWindow.__init__(self)

        self.con = con
        self.user = user
        self.regUi = regUi

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
        self.ui.addStudentButton.clicked.connect(self.studentWindowOpen)
        # End StudentWindow

        # Start TeacherWindow
        self.teacherWindow = QMainWindow()
        self.teacherUi = Ui_TeacherWindow()

        self.teacherUi.setupUi(self.teacherWindow)

        self.teacherWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.teacherWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        self.teacherWindow.setWindowFlags(Qt.FramelessWindowHint)

        self.teacherUi.cancelButton.clicked.connect(self.closeTeacherWindow)
        self.ui.addTeacherButton.clicked.connect(self.teacherWindowOpen)
        # End TeacherWindow

        # Start LessonWindow
        self.lessonWindow = QMainWindow()
        self.lessonUi = Ui_LessonWindow()

        self.lessonUi.setupUi(self.lessonWindow)

        self.lessonWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.lessonWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        self.lessonWindow.setWindowFlags(Qt.FramelessWindowHint)

        self.lessonUi.cancelButton.clicked.connect(self.closeLessonWindow)
        self.ui.addLessonButton.clicked.connect(self.lessonWindowOpen)
        # End LessonWindow

        # Start GroupWindow
        self.groupWindow = QMainWindow()
        self.groupUi = Ui_GroupWindow()

        self.groupUi.setupUi(self.groupWindow)

        self.groupWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        self.groupWindow.setAttribute(Qt.WA_NoSystemBackground, True)
        self.groupWindow.setWindowFlags(Qt.FramelessWindowHint)

        self.groupUi.cancelButton.clicked.connect(self.closeGroupWindow)
        self.ui.addGroupButton.clicked.connect(self.groupWindowOpen)
        # End GroupWindow

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

        self.ui.minimizeButton.clicked.connect(self.showMinMaxWindow)

        self.ui.lessonBox.currentIndexChanged.connect(self.load_groups)
        self.ui.groupBox.currentTextChanged.connect(self.load_group_teacher)

        self.ui.ratingWidget.cellChanged.connect(self.changedCell)

        self.ui.calendarWidget.clicked.connect(self.schedulesFrame)

        self.ui.exitButton.clicked.connect(self.close)

        self.ui.topMenu.mouseMoveEvent = self.moveWindow

        self.ui.leaveButton.clicked.connect(self.leaveButtonClick)

        self.load()

    def adminButtons(self, button):
        id: int = self.adminButtonGroup.id(button)
        self.ui.mainWindows.setCurrentIndex(0)
        self.ui.adminStackedWidget.setCurrentIndex(id)
        match id:
            case 0:
                self.loadSchedulesFrame()
            case 1:
                self.loadTeachersTable()
            case 2:
                self.loadStudentsTable()
            case 3:
                self.loadGroupsTable()
            case 4:
                self.loadLessonsTable()

    def leaveButtonClick(self):
        self.close()
        self.regUi.show()


    # Start StudentWindow

    def closeStudentWindow(self):
        self.studentUi.fioErrorLabel.setText('')
        self.studentUi.emailErrorLabel.setText('')
        self.studentUi.groupErrorLabel.setText('')
        self.studentWindow.close()
        self.studentUi.addButton.clicked.disconnect()

    def studentWindowOpen(self):
        self.studentUi.groupBox.clear()
        self.studentUi.fullNameInput.setText('')
        self.studentUi.emailInput.setText('')
        self.studentUi.addButton.setText('Добавить')

        self.studentUi.groupBox.addItems(self.con.get_all_groups())

        self.studentUi.addButton.clicked.connect(self.addStudentButtonClicked)
        self.studentWindow.show()

    def addStudentButtonClicked(self):
        fullName = self.studentUi.fullNameInput.text()
        email = self.studentUi.emailInput.text()
        group = self.studentUi.groupBox.currentText()

        fullName_ = fullName.split(' ')
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_ = pattern.search(email)

        self.studentUi.fioErrorLabel.setText('')
        self.studentUi.emailErrorLabel.setText('')
        self.studentUi.groupErrorLabel.setText('')

        check = False
        if not 2 <= len(fullName_) <= 3:
            self.studentUi.fioErrorLabel.setText('Ошибка! Введите как минимум имя и фамилию.')
            check = True

        if not fullName:
            self.studentUi.fioErrorLabel.setText('Поле не должно быть пустым.')

        if not email_:
            self.studentUi.emailErrorLabel.setText('Ошибка! Не правильно введена почта.')
            check = True

        if self.con.get_user(email):
            self.studentUi.emailErrorLabel.setText('Пользователь с такой почтой уже существует.')
            check = True

        if not email:
            self.studentUi.emailErrorLabel.setText('Поле не должно быть пустым.')

        if check:
            return

        row = self.ui.studentTableWidget.rowCount()
        self.ui.studentTableWidget.setRowCount(row + 1)

        self.loadStudentTableItems(row, fullName, email, group)

        self.con.insert_student(fullName, email, group)
        self.closeStudentWindow()

    def loadStudentsTable(self):
        students = self.con.get_students_all()
        rowCount = len(students)
        self.ui.studentTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            id, sName, sFirstname, sSecondName, email, group_id, index = students[row]
            sFullName = f'{sFirstname} {sName} {sSecondName}'
            group = self.con.get_group(group_id)
            self.loadStudentTableItems(row, sFullName, email, group)

    def loadStudentTableItems(self, row, name, email, group):

        itemFIO = QTableWidgetItem(name)
        self.ui.studentTableWidget.setItem(row, 0, itemFIO)

        itemEmail = QTableWidgetItem(email)
        self.ui.studentTableWidget.setItem(row, 1, itemEmail)

        itemGroup = QTableWidgetItem(group)
        self.ui.studentTableWidget.setItem(row, 2, itemGroup)

        qWidget = QWidget()
        qWidget.setStyleSheet(u"QWidget {\n"
                              " background-color: rgb(30, 31, 34);\n"
                              "}\n"
                              "QPushButton {\n"
                              " margin: 5px;\n"
                              "	border-radius: 4px;\n"
                              " background-color: rgb(71, 80, 83);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(53, 54, 60);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(30, 31, 34);\n"
                              " }")
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditStudentWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteStudent)
        qHLayout.addWidget(itemDelete)

        self.ui.studentTableWidget.setCellWidget(row, 3, qWidget)

    # End StudentWindow

    # Start TeacherWindow
    def closeTeacherWindow(self):
        self.teacherUi.FullNameErrorLabel.setText('')
        self.teacherUi.emailErrorLabel.setText('')
        self.teacherUi.teacherErrorLabel.setText('')
        self.teacherUi.lessonErrorLabel1.setText('')
        self.teacherWindow.close()
        self.teacherUi.addButton.clicked.disconnect()

    def teacherWindowOpen(self):
        self.teacherUi.fullNameInput.setText('')
        self.teacherUi.emailInput.setText('')
        self.teacherUi.addButton.setText('Добавить')

        self.teacherUi.groupBox.clear()
        self.teacherUi.lessonBox1.clear()
        self.teacherUi.lessonBox2.clear()

        groups = [''] + self.con.get_all_groups()
        self.teacherUi.groupBox.addItems(groups)

        lessons = self.con.get_all_lessons()
        lessons = [' '.join(lesson) for lesson in lessons]
        lessons_ = [''] + lessons
        self.teacherUi.lessonBox1.addItems(lessons_)
        self.teacherUi.lessonBox2.addItems(lessons_)

        self.teacherUi.addButton.clicked.connect(self.addTeacherButtonClicked)
        self.teacherWindow.show()

    def addTeacherButtonClicked(self):
        fullName = self.teacherUi.fullNameInput.text()
        email = self.teacherUi.emailInput.text()
        lesson1 = self.teacherUi.lessonBox1.currentText()
        lesson2 = self.teacherUi.lessonBox2.currentText()
        group = self.teacherUi.groupBox.currentText()

        fullName_ = fullName.split(' ')
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_ = pattern.search(email)

        check = False

        self.teacherUi.FullNameErrorLabel.setText('')
        self.teacherUi.emailErrorLabel.setText('')
        self.teacherUi.teacherErrorLabel.setText('')
        self.teacherUi.lessonErrorLabel1.setText('')

        if not 2 <= len(fullName_) <= 3:
            self.teacherUi.FullNameErrorLabel.setText('Ошибка! Введите как минимум имя и фамилию.')
            check = True

        if not fullName:
            self.teacherUi.FullNameErrorLabel.setText('Поле не должно быть пустым.')

        if not email_:
            self.teacherUi.emailErrorLabel.setText('Ошибка! Не правильно введена почта.')
            check = True

        if self.con.get_user(email):
            self.teacherUi.emailErrorLabel.setText('Пользователь с такой почтой уже существует.')
            check = True

        if not email:
            self.teacherUi.emailErrorLabel.setText('Поле не должно быть пустым.')

        if lesson1 == lesson2 == '':
            self.teacherUi.lessonErrorLabel1.setText('Ошибка! Выберите как минимум 1 предмет.')
            check = True

        if check:
            return

        lessons = []
        if lesson1:
            lessons.append(lesson1)
        if lesson2:
            lessons.append(lesson2)
        lessons_ = lessons[0]
        if len(lessons) == 2:
            lessons_ = '\n'.join(lessons)

        row = self.ui.teacherTableWidget.rowCount()
        self.ui.teacherTableWidget.setRowCount(row + 1)

        self.loadTeachersTableItems(row, fullName, email, lessons_, group)
        self.con.insert_teacher(fullName, email, lessons, group)
        self.closeTeacherWindow()

    def loadTeachersTable(self):
        teachers = self.con.get_teachers()
        rowCount = len(teachers)
        self.ui.teacherTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            id, sName, sFirstname, sSecondName, email, index = teachers[row]
            lessons = [' '.join([lesson[0], lesson[1]]) for lesson in self.con.get_lessons_teacher(email)]
            lessons_ = '\n'.join(lessons)
            sFullName = f'{sFirstname} {sName} {sSecondName}'
            group = self.con.get_group_teacher(email)
            self.loadTeachersTableItems(row, sFullName, email, lessons_, group)

    def loadTeachersTableItems(self, row, name, email, lessons, group):

        itemFIO = QTableWidgetItem(name)
        self.ui.teacherTableWidget.setItem(row, 0, itemFIO)

        itemEmail = QTableWidgetItem(email)
        self.ui.teacherTableWidget.setItem(row, 1, itemEmail)

        itemLesson = QTableWidgetItem(lessons)
        self.ui.teacherTableWidget.setItem(row, 2, itemLesson)

        itemGroup = QTableWidgetItem(group)
        self.ui.teacherTableWidget.setItem(row, 3, itemGroup)

        qWidget = QWidget()
        qWidget.setStyleSheet(u"QWidget {\n"
                              " background-color: rgb(30, 31, 34);\n"
                              "}\n"
                              "QPushButton {\n"
                              " margin: 5px;\n"
                              "	border-radius: 4px;\n"
                              " background-color: rgb(71, 80, 83);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(53, 54, 60);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(30, 31, 34);\n"
                              " }")
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditTeacherWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteTeacher)
        qHLayout.addWidget(itemDelete)
        self.ui.teacherTableWidget.setCellWidget(row, 4, qWidget)

    # End TeacherWindow

    # Start GroupWindow
    def closeGroupWindow(self):
        self.groupUi.groupErrorLabel.setText('')
        self.groupWindow.close()
        self.groupUi.addButton.clicked.disconnect()
        self.groupUi.addLesson.clicked.disconnect()
        self.groupUi.deleteLesson.clicked.disconnect()

    def groupWindowOpen(self):
        self.groupUi.groupInput.setText('')
        self.groupUi.addButton.setText('Добавить')
        self.groupUi.groupLessonTableWidget.clear()
        lessonList = self.con.get_all_lessons()
        lessonList_ = [' '.join(lesson) for lesson in lessonList]

        self.groupUi.groupLessonTableWidget.setRowCount(0)

        self.groupUi.lessonBox.clear()
        self.groupUi.lessonBox.addItems(lessonList_)

        self.groupUi.deleteLesson.clicked.connect(self.deleteGroupLessonButtonClicked)
        self.groupUi.addLesson.clicked.connect(self.addGroupLessonButtonClicked)
        self.groupUi.addButton.clicked.connect(self.addGroupButtonClicked)
        self.groupWindow.show()

    def deleteGroupLessonButtonClicked(self):
        if not self.groupUi.groupLessonTableWidget.selectedIndexes():
            return
        row = self.groupUi.groupLessonTableWidget.selectedIndexes()[0].row()

        lessons = [self.groupUi.lessonBox.itemText(i) for i in range(self.groupUi.lessonBox.count())]
        if self.groupUi.groupLessonTableWidget.item(row, 0).text():
            lesson = self.groupUi.groupLessonTableWidget.item(row, 0).text()
            lessons.append(lesson)
            lessons.sort()

        self.groupUi.lessonBox.clear()
        self.groupUi.lessonBox.addItems(lessons)

        self.groupUi.groupLessonTableWidget.removeRow(row)

    def addGroupLessonButtonClicked(self):
        lesson = self.groupUi.lessonBox.currentText()
        if not lesson:
            return

        rowCount = self.groupUi.groupLessonTableWidget.rowCount()

        self.groupUi.groupLessonTableWidget.setRowCount(rowCount + 1)

        itemLesson = QTableWidgetItem(lesson)
        self.groupUi.groupLessonTableWidget.setItem(rowCount, 0, itemLesson)

        lessons = [self.groupUi.lessonBox.itemText(i) for i in range(self.groupUi.lessonBox.count())]
        lessonIndex = lessons.index(lesson)
        lessons.pop(lessonIndex)
        lessons.sort()

        lessonCount = self.groupUi.lessonBox.count()
        if lessonIndex == lessonCount - 1:
            lessonIndex -= 1

        self.groupUi.lessonBox.clear()
        self.groupUi.lessonBox.addItems(lessons)
        self.groupUi.lessonBox.setCurrentIndex(lessonIndex)

    def addGroupButtonClicked(self):
        group = self.groupUi.groupInput.text()
        lessons = [self.groupUi.groupLessonTableWidget.item(i, 0).text() for i in
                   range(self.groupUi.groupLessonTableWidget.rowCount())]

        pattern = re.compile(r'^[А-Я]+[-]+[0-4]+[-]+\d{2}+$')
        group_ = pattern.search(group)

        self.groupUi.groupErrorLabel.setText('')

        check = False

        if not group_:
            self.groupUi.groupErrorLabel.setText('Не правильно введён формат группы. Пример: ИСП-4-20')
            check = True

        if self.con.get_group_id(group):
            self.groupUi.groupErrorLabel.setText('Такая группа уже существует.')
            check = True

        if not group:
            self.groupUi.groupErrorLabel.setText('Поле не должно быть пустым.')

        if check:
            return

        lessons_ = '\n'.join(lessons)

        row = self.ui.groupTableWidget.rowCount()
        self.ui.groupTableWidget.setRowCount(row + 1)

        self.loadGroupTableItems(row, lessons_, group)

        self.con.insert_group(group, lessons_)
        self.closeGroupWindow()

    def loadGroupsTable(self):
        groups = self.con.get_all_groups()
        rowCount = len(groups)
        self.ui.groupTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            lessons = self.con.get_lessons_group(groups[row])
            lessons_ = ''
            if lessons:
                lessons = [' '.join([lesson[0], lesson[1]]) for lesson in lessons]
                lessons_ = '\n'.join(lessons)
            self.loadGroupTableItems(row, lessons_, groups[row])

    def loadGroupTableItems(self, row, lessons, group):

        itemGroup = QTableWidgetItem(group)
        self.ui.groupTableWidget.setItem(row, 0, itemGroup)

        itemLessons = QTableWidgetItem(lessons)
        self.ui.groupTableWidget.setItem(row, 1, itemLessons)

        qWidget = QWidget()
        qWidget.setStyleSheet(u"QWidget {\n"
                              " background-color: rgb(30, 31, 34);\n"
                              "}\n"
                              "QPushButton {\n"
                              " margin: 5px;\n"
                              "	border-radius: 4px;\n"
                              " background-color: rgb(71, 80, 83);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(53, 54, 60);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(30, 31, 34);\n"
                              " }")
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditGroupWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteGroup)
        qHLayout.addWidget(itemDelete)

        self.ui.groupTableWidget.setCellWidget(row, 2, qWidget)

    # End GroupWindow

    # Start LessonWindow
    def closeLessonWindow(self):
        self.lessonUi.lessonErrorLabel.setText('')
        self.lessonUi.indexErrorLabel.setText('')
        self.lessonWindow.close()
        self.lessonUi.addButton.clicked.disconnect()

    def lessonWindowOpen(self):
        self.lessonUi.addButton.setText('Добавить')
        self.lessonUi.lessonInput.setText('')
        self.lessonUi.indexInput.setText('')

        self.lessonUi.addButton.clicked.connect(self.addLessonButtonClicked)
        self.lessonWindow.show()

    def addLessonButtonClicked(self):
        lesson = self.lessonUi.lessonInput.text()
        index = self.lessonUi.indexInput.text()

        self.lessonUi.lessonErrorLabel.setText('')
        self.lessonUi.indexErrorLabel.setText('')

        check = False

        if self.con.get_lesson_id(lesson):
            self.lessonUi.lessonErrorLabel.setText('Такой предмет уже существует.')
            check = True

        if not lesson:
            self.lessonUi.lessonErrorLabel.setText('Поле не должно быть пустым.')
            check = True

        if self.con.get_index_lesson(index):
            self.lessonUi.indexErrorLabel.setText('Такой код уже существует.')
            check = True

        if not index:
            self.lessonUi.indexErrorLabel.setText('Поле не должно быть пустым.')
            check = True

        if check:
            return

        row = self.ui.lessonTableWidget.rowCount()
        self.ui.lessonTableWidget.setRowCount(row + 1)

        self.loadLessonTableItems(row, lesson, index)
        self.con.insert_lesson(lesson, index)
        self.closeLessonWindow()

    def loadLessonsTable(self):
        lessons = self.con.get_all_lessons()
        rowCount = len(lessons)
        self.ui.lessonTableWidget.setRowCount(rowCount)
        for row in range(rowCount):
            lesson, index = lessons[row]
            self.loadLessonTableItems(row, lesson, index)

    def loadLessonTableItems(self, row, lesson, index):

        itemLesson = QTableWidgetItem(lesson)
        self.ui.lessonTableWidget.setItem(row, 0, itemLesson)

        itemIndex = QTableWidgetItem(index)
        self.ui.lessonTableWidget.setItem(row, 1, itemIndex)

        qWidget = QWidget()
        qWidget.setStyleSheet(u"QWidget {\n"
                              " background-color: rgb(30, 31, 34);\n"
                              "}\n"
                              "QPushButton {\n"
                              " margin: 5px;\n"
                              "	border-radius: 4px;\n"
                              " background-color: rgb(71, 80, 83);\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "	background-color: rgb(53, 54, 60);\n"
                              "}\n"
                              "\n"
                              "QPushButton:pressed {\n"
                              "	background-color: rgb(30, 31, 34);\n"
                              " }")
        qHLayout = QHBoxLayout(qWidget)
        qHLayout.setContentsMargins(0, 0, 0, 0)
        qHLayout.setSpacing(0)
        itemEdit = TableQPushButton(row, self)
        itemEdit.setObjectName('edit-' + str(row))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemEdit.setIcon(icon1)
        itemEdit.clicked.connect(itemEdit.openEditLessonWindow)
        qHLayout.addWidget(itemEdit)

        itemDelete = TableQPushButton(row, self)
        itemDelete.setObjectName('delete-' + str(row))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        itemDelete.setIcon(icon2)
        itemDelete.clicked.connect(itemDelete.deleteLesson)
        qHLayout.addWidget(itemDelete)

        self.ui.lessonTableWidget.setCellWidget(row, 2, qWidget)

        # End LessonWindow

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

        if not date or not name:
            self.ui.ratingWidget.item(row, column).setText('')
            return

        if self.ui.ratingWidget.item(row, column).text() != rating:
            self.cellCheck = not self.cellCheck
        self.ui.ratingWidget.item(row, column).setText(rating)

        self.con.update_rating_group(assessments, date, name, group, lesson)
        self.load_group_teacher()

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

    def load(self):
        match self.user[3]:
            case 'admin':
                self.swap_to_admin(self.user[1])
            case 'student':
                self.swap_to_student(self.user[1])
            case 'teacher':
                self.swap_to_teacher(self.user[1])

    def swap_to_admin(self, email):
        user = self.con.get_admin(email)
        self.ui.leftTypeLabel.setText('Админ')
        self.ui.leftGroupLabel.setText('')
        self.ui.rightGroupLabel.setText('')
        self.ui.rightNameLabel.setText(f'{user[2]} {user[1][0]}. {user[3][0]}.')

    def swap_to_student(self, email):
        user = self.con.get_student(email)

        self.ui.mainWindows.setCurrentIndex(1)
        self.ui.teacherButton.setHidden(True)
        self.ui.adminButton.setHidden(True)

        self.ui.leftTypeLabel.setText('Студент')
        self.ui.leftGroupLabel.setText('Группа')
        self.ui.rightGroupLabel.setText(user[4])
        self.ui.comboBoxFrame.setVisible(False)
        NameFormat = f'{user[1]} {user[0][0]}. '
        if user[2]:
            NameFormat += f'{user[2][0]}.'
        self.ui.rightNameLabel.setText(NameFormat)

        self.ui.ratingWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        rows = self.con.get_lessons_student(email)
        columns = self.con.get_date_rating_student(user[4])
        items = self.con.get_assessment_rating_student(email)

        rows_ = [row[1] for row in rows]

        self.load_tale_widget(rows_, columns, items)

    def swap_to_teacher(self, email):
        user = self.con.get_teacher(email)

        self.ui.mainWindows.setCurrentIndex(1)
        self.ui.studentButton.setHidden(True)
        self.ui.adminButton.setHidden(True)

        self.ui.leftTypeLabel.setText('Учитель')
        self.ui.leftGroupLabel.setText('')
        self.ui.rightGroupLabel.setText('')
        NameFormat = f'{user[2]} {user[1][0]}. '
        if user[3]:
            NameFormat += f'{user[3][0]}.'
        self.ui.rightNameLabel.setText(NameFormat)
        self.ui.comboBoxFrame.setVisible(True)

        self.ui.ratingWidget.setEditTriggers(
            QAbstractItemView.EditTrigger.AnyKeyPressed | QAbstractItemView.EditTrigger.DoubleClicked)

        lessons = self.con.get_lessons_teacher(email)
        lessons_ = [f'{lesson[0]}, {lesson[1]}' for lesson in lessons]

        self.ui.lessonBox.clear()
        self.ui.lessonBox.addItems(lessons_)

    def load_groups(self):
        lesson = self.ui.lessonBox.currentText()

        groups = self.con.get_groups_lesson(lesson.split(',')[0])

        self.ui.groupBox.clear()
        self.ui.groupBox.addItems(groups)

    def load_group_teacher(self):
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

        for x in range(len(lessonList)):
            sum = 0
            count = 0
            for y in range(len(dateList)):
                text = self.ui.ratingWidget.item(x, y)
                if text:
                    for num in text.text().split(','):
                        sum += int(num)
                        count += 1
            average = '0'
            if count:
                average = f'{sum / count:.1f}'
            itemAVG = QTableWidgetItem(average)
            self.ui.ratingWidget.setItem(x, len(dateList) - 1, itemAVG)

        self.check = True

    def load_headers(self, rows, columns):
        rowCount = self.ui.ratingWidget.rowCount()
        columnCount = self.ui.ratingWidget.columnCount()

        self.ui.ratingWidget.verticalHeader().setMaximumWidth(250)

        if len(rows) > rowCount:
            rowCount = len(rows)
            self.ui.ratingWidget.setRowCount(rowCount)

        if len(columns) > columnCount:
            columnCount = len(columns)
            self.ui.ratingWidget.setColumnCount(columnCount + 1)

        for x in range(columnCount):
            column = QTableWidgetItem('')

            if x < len(columns):
                column.setText('.'.join(str(columns[x]).split('-')[1::]))
            self.ui.ratingWidget.setHorizontalHeaderItem(x, column)

        item = QTableWidgetItem('Ср.')
        self.ui.ratingWidget.setHorizontalHeaderItem(len(columns), item)

        for y in range(rowCount):
            row = QTableWidgetItem()

            if y < len(rows):
                row.setText(str(rows[y]))
            else:
                row.setText('')

            self.ui.ratingWidget.setVerticalHeaderItem(y, row)

    def loadSchedulesFrame(self):
        groups = self.con.get_all_groups()
        self.ui.adminSheduleTable.setColumnCount(len(groups))
        self.ui.adminSheduleTable.setHorizontalHeaderLabels(groups)
        for column in range(self.ui.adminSheduleTable.columnCount()):
            currentGroup = self.ui.adminSheduleTable.horizontalHeaderItem(column).text()
            lessons = self.con.get_lessons_and_teacher_group(currentGroup)
            lessons_ = [f'{lesson[0]} {lesson[1]}\n{lesson[3]} {lesson[2][0]}. {lesson[4]}.' for lesson in lessons]
            for row in range(self.ui.adminSheduleTable.rowCount()):
                scheduleComboBox = TableQComboBox(column, row, self.con, self.ui)
                scheduleComboBox.addItem('Нет занятий')
                scheduleComboBox.addItems(lessons_)
                scheduleComboBox.currentTextChanged.connect(scheduleComboBox.updateSQLDate)
                self.ui.adminSheduleTable.setCellWidget(row, column, scheduleComboBox)
        self.schedulesFrame()

