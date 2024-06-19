from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableWidgetItem
import re


class TableQPushButton(QPushButton):
    def __init__(self, row: int, ui):
        super(TableQPushButton, self).__init__()
        self.row = row
        self.text = None
        self.ui = ui

    def deleteStudent(self):
        email = self.ui.ui.studentTableWidget.item(self.row, 1).text()
        self.ui.con.delete_student(email)
        self.ui.ui.studentTableWidget.removeRow(self.row)

        rows = self.ui.ui.studentTableWidget.rowCount()
        for row in range(self.row, rows):
            item = self.ui.ui.studentTableWidget.cellWidget(row, 3).children()
            editItem = item[1]
            deleteItem = item[2]
            editItem.row -= 1
            deleteItem.row -= 1

    def openEditStudentWindow(self):
        sName = self.ui.ui.studentTableWidget.item(self.row, 0).text()
        email = self.ui.ui.studentTableWidget.item(self.row, 1).text()
        group = self.ui.ui.studentTableWidget.item(self.row, 2).text()

        self.ui.studentUi.fullNameInput.setText(sName)
        self.ui.studentUi.emailInput.setText(email)
        self.ui.studentUi.addButton.setText('Сохранить')

        self.ui.studentUi.groupBox.clear()
        groupList = [''] + self.ui.con.get_all_groups()
        self.ui.studentUi.groupBox.addItems(groupList)
        self.ui.studentUi.groupBox.setCurrentIndex(groupList.index(group))

        self.ui.studentUi.addButton.clicked.connect(self.editStudentButtonClicked)
        self.ui.studentWindow.show()

    def editStudentButtonClicked(self):
        prevName = self.ui.ui.studentTableWidget.item(self.row, 0)
        prevEmail = self.ui.ui.studentTableWidget.item(self.row, 1)
        prevGroup = self.ui.ui.studentTableWidget.item(self.row, 2)

        fullName = self.ui.studentUi.fullNameInput.text()
        email = self.ui.studentUi.emailInput.text()
        group = self.ui.studentUi.groupBox.currentText()

        fullName_ = fullName.split(' ')
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_ = pattern.search(email)

        self.ui.studentUi.fioErrorLabel.setText('')
        self.ui.studentUi.emailErrorLabel.setText('')
        self.ui.studentUi.groupErrorLabel.setText('')

        check = False
        if not 2 <= len(fullName_) <= 3:
            self.ui.studentUi.fioErrorLabel.setText('Ошибка! Введите как минимум имя и фамилию.')
            check = True

        if not fullName:
            self.ui.studentUi.fioErrorLabel.setText('Поле не должно быть пустым.')

        if not email_:
            self.ui.studentUi.emailErrorLabel.setText('Ошибка! Не правильно введена почта.')
            check = True

        if self.ui.con.get_user(email) and prevEmail.text() != email:
            self.ui.studentUi.emailErrorLabel.setText('Пользователь с такой почтой уже существует.')
            check = True

        if not email:
            self.ui.studentUi.emailErrorLabel.setText('Поле не должно быть пустым.')

        if check:
            return

        self.ui.con.update_student(fullName, email, group, prevName.text(), prevEmail.text(), prevGroup.text())
        prevName.setText(fullName)
        prevEmail.setText(email)
        prevGroup.setText(group)
        self.ui.closeStudentWindow()

    def deleteTeacher(self):
        email = self.ui.ui.teacherTableWidget.item(self.row, 1).text()
        if not email:
            return
        self.ui.con.delete_teacher(email)
        self.ui.ui.teacherTableWidget.removeRow(self.row)

        rows = self.ui.ui.teacherTableWidget.rowCount()
        for row in range(self.row, rows):
            item = self.ui.ui.teacherTableWidget.cellWidget(row, 4).children()
            editItem = item[1]
            deleteItem = item[2]
            editItem.row -= 1
            deleteItem.row -= 1

    def openEditTeacherWindow(self):
        sName = self.ui.ui.teacherTableWidget.item(self.row, 0).text()
        email = self.ui.ui.teacherTableWidget.item(self.row, 1).text()
        lessons = self.ui.ui.teacherTableWidget.item(self.row, 2).text()
        group = self.ui.ui.teacherTableWidget.item(self.row, 3).text()
        groupList = [''] + self.ui.con.get_all_groups()
        lessons = lessons.split('\n')
        if len(lessons) == 1:
            lessons.append('')
        lessonList = [''] + [' '.join(lesson) for lesson in self.ui.con.get_all_lessons()]

        self.ui.teacherUi.fullNameInput.setText(sName)
        self.ui.teacherUi.emailInput.setText(email)
        self.ui.teacherUi.addButton.setText('Сохранить')

        self.ui.teacherUi.groupBox.clear()
        self.ui.teacherUi.groupBox.addItems(groupList)
        self.ui.teacherUi.groupBox.setCurrentIndex(groupList.index(group))

        self.ui.teacherUi.lessonBox1.clear()
        self.ui.teacherUi.lessonBox1.addItems(lessonList)
        self.ui.teacherUi.lessonBox1.setCurrentIndex(lessonList.index(lessons[0]))

        self.ui.teacherUi.lessonBox2.clear()
        self.ui.teacherUi.lessonBox2.addItems(lessonList)
        self.ui.teacherUi.lessonBox2.setCurrentIndex(lessonList.index(lessons[1]))

        self.ui.teacherUi.addButton.clicked.connect(self.editTeacherButtonClicked)
        self.ui.teacherWindow.show()

    def editTeacherButtonClicked(self):
        prevName = self.ui.ui.teacherTableWidget.item(self.row, 0)
        prevEmail = self.ui.ui.teacherTableWidget.item(self.row, 1)
        prevLessons = self.ui.ui.teacherTableWidget.item(self.row, 2)
        prevGroup = self.ui.ui.teacherTableWidget.item(self.row, 3)

        fullName = self.ui.teacherUi.fullNameInput.text()
        email = self.ui.teacherUi.emailInput.text()
        lesson1 = self.ui.teacherUi.lessonBox1.currentText()
        lesson2 = self.ui.teacherUi.lessonBox2.currentText()
        group = self.ui.teacherUi.groupBox.currentText()

        fullName_ = fullName.split(' ')
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email_ = pattern.search(email)

        check = False

        self.ui.teacherUi.FullNameErrorLabel.setText('')
        self.ui.teacherUi.emailErrorLabel.setText('')
        self.ui.teacherUi.teacherErrorLabel.setText('')
        self.ui.teacherUi.lessonErrorLabel1.setText('')

        if not 2 <= len(fullName_) <= 3:
            self.ui.teacherUi.FullNameErrorLabel.setText('Ошибка! Введите как минимум имя и фамилию.')
            check = True

        if not fullName:
            self.ui.teacherUi.FullNameErrorLabel.setText('Поле не должно быть пустым.')

        if not email_:
            self.ui.teacherUi.emailErrorLabel.setText('Ошибка! Не правильно введена почта.')
            check = True

        if self.ui.con.get_user(email) and prevEmail.text() != email:
            self.ui.teacherUi.emailErrorLabel.setText('Пользователь с такой почтой уже существует.')
            check = True

        if not email:
            self.ui.teacherUi.emailErrorLabel.setText('Поле не должно быть пустым.')

        if lesson1 == lesson2 == '':
            self.ui.teacherUi.lessonErrorLabel1.setText('Ошибка! Выберите как минимум 1 предмет.')
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

        self.ui.con.update_teacher(fullName, email, lessons, group, prevEmail.text())
        prevName.setText(fullName)
        prevEmail.setText(email)
        prevLessons.setText(lessons_)
        prevGroup.setText(group)
        self.ui.closeTeacherWindow()

    def deleteGroup(self):
        group = self.ui.ui.groupTableWidget.item(self.row, 0).text()

        self.ui.con.delete_group(group)
        self.ui.ui.groupTableWidget.removeRow(self.row)

        rows = self.ui.ui.groupTableWidget.rowCount()
        for row in range(self.row, rows):
            item = self.ui.ui.groupTableWidget.cellWidget(row, 2).children()
            editItem = item[1]
            deleteItem = item[2]
            editItem.row -= 1
            deleteItem.row -= 1

    def openEditGroupWindow(self):
        group = self.ui.ui.groupTableWidget.item(self.row, 0).text()

        self.ui.groupUi.addButton.setText('Сохранить')

        self.ui.groupUi.groupInput.setText(group)

        self.ui.groupUi.groupLessonTableWidget.clear()
        lessons = self.ui.ui.groupTableWidget.item(self.row, 1).text()
        lessons_ = lessons.split('\n')
        l: int = 0 if lessons_ == [''] else len(lessons_)
        self.ui.groupUi.groupLessonTableWidget.setRowCount(l)
        for row in range(len(lessons_)):
            itemLesson = QTableWidgetItem(lessons_[row])
            self.ui.groupUi.groupLessonTableWidget.setItem(row, 0, itemLesson)

        lessonList = self.ui.con.get_all_lessons()
        lessonList_ = [' '.join(lesson) for lesson in lessonList]
        if lessons:
            for lesson in lessons_:
                lessonIndex = lessonList_.index(lesson)
                lessonList_.pop(lessonIndex)

        self.ui.groupUi.lessonBox.clear()
        self.ui.groupUi.lessonBox.addItems(lessonList_)

        self.ui.groupUi.deleteLesson.clicked.connect(self.ui.deleteGroupLessonButtonClicked)
        self.ui.groupUi.addLesson.clicked.connect(self.ui.addGroupLessonButtonClicked)
        self.ui.groupUi.addButton.clicked.connect(self.editGroupButtonClicked)
        self.ui.groupWindow.show()

    def editGroupButtonClicked(self):
        prevGroup = self.ui.ui.groupTableWidget.item(self.row, 0)
        prevLessons = self.ui.ui.groupTableWidget.item(self.row, 1)

        group = self.ui.groupUi.groupInput.text()
        lessons = [self.ui.groupUi.groupLessonTableWidget.item(i, 0).text() for i in
                   range(self.ui.groupUi.groupLessonTableWidget.rowCount())]
        lessons_ = '\n'.join(lessons)

        pattern = re.compile(r'^[А-Я]+[-]+[0-4]+[-]+\d{2}+$')
        group_ = pattern.search(group)

        self.ui.groupUi.groupErrorLabel.setText('')

        check = False
        if not group_:
            self.ui.groupUi.groupErrorLabel.setText('Неправильно введена группа')
            check = True

        if self.ui.con.get_user(group) or prevGroup.text() != group:
            self.ui.groupUi.groupErrorLabel.setText('Такая группа уже существует')
            check = True

        if check:
            return

        self.ui.con.update_group(group, lessons, prevGroup.text())
        prevLessons.setText(lessons_)
        prevGroup.setText(group)
        self.ui.closeGroupWindow()

    def deleteLesson(self):
        lesson = self.ui.ui.lessonTableWidget.item(self.row, 0).text()
        index = self.ui.ui.lessonTableWidget.item(self.row, 1).text()

        self.ui.con.delete_lesson(lesson, index)
        self.ui.ui.lessonTableWidget.removeRow(self.row)

        rows = self.ui.ui.lessonTableWidget.rowCount()
        for row in range(self.row, rows):
            item = self.ui.ui.lessonTableWidget.cellWidget(row, 2).children()
            editItem = item[1]
            deleteItem = item[2]
            editItem.row -= 1
            deleteItem.row -= 1

    def openEditLessonWindow(self):
        lesson = self.ui.ui.lessonTableWidget.item(self.row, 0).text()
        index = self.ui.ui.lessonTableWidget.item(self.row, 1).text()

        self.ui.lessonUi.addButton.setText('Сохранить')
        self.ui.lessonUi.lessonInput.setText(lesson)
        self.ui.lessonUi.indexInput.setText(index)

        self.ui.lessonUi.addButton.clicked.connect(self.editLessonButtonClicked)
        self.ui.lessonWindow.show()

    def editLessonButtonClicked(self):
        prevLesson = self.ui.ui.lessonTableWidget.item(self.row, 0)
        prevIndex = self.ui.ui.lessonTableWidget.item(self.row, 1)

        lesson = self.ui.lessonUi.lessonInput.text()
        index = self.ui.lessonUi.indexInput.text()

        self.ui.lessonUi.lessonErrorLabel.setText('')
        self.ui.lessonUi.indexErrorLabel.setText('')

        check = False

        if self.ui.con.get_lesson_id(lesson) and prevLesson.text() != lesson:
            self.ui.lessonUi.lessonErrorLabel.setText('Такой предмет уже существует.')
            check = True

        if not lesson:
            self.ui.lessonUi.lessonErrorLabel.setText('Поле не должно быть пустым.')
            check = True

        if self.ui.con.get_index_lesson(index) and prevIndex.text() != index:
            self.ui.lessonUi.indexErrorLabel.setText('Такой код уже существует.')
            check = True

        if not index:
            self.ui.lessonUi.indexErrorLabel.setText('Поле не должно быть пустым.')
            check = True

        if check:
            return

        self.ui.con.update_lesson(lesson, index, prevLesson.text(), prevIndex.text())
        prevLesson.setText(lesson)
        prevIndex.setText(index)
        self.ui.closeLessonWindow()
