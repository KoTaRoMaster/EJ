from PySide6.QtWidgets import QPushButton
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
        groupList = self.ui.con.get_groups()
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

        if any([False if 2 <= len(fullName_) <= 3 else True, False if email_ else True]):
            print('Неправильно введено ФИО или почта')
            return
        if self.ui.con.get_user(email):
            print('Уже есть пользователь с такой почтой')
            return

        self.ui.con.update_student(fullName, email, group, prevName.text(), prevEmail.text(), prevGroup.text())
        prevName.setText(fullName)
        prevEmail.setText(email)
        prevGroup.setText(group)
        self.ui.closeStudentWindow()

    def deleteTeacher(self):
        # email = self.ui.ui.teacherTableWidget.item(self.row, 1).text()
        # self.ui.con.delete_student(email)
        self.ui.ui.teacherTableWidget.removeRow(self.row)

        rows = self.ui.ui.teacherTableWidget.rowCount()
        for row in range(self.row, rows):
            item = self.ui.ui.teacherTableWidget.cellWidget(row, 3).children()
            editItem = item[1]
            deleteItem = item[2]
            editItem.row -= 1
            deleteItem.row -= 1

    def openEditTeacherWindow(self):
        sName = self.ui.ui.teacherTableWidget.item(self.row, 0).text()
        email = self.ui.ui.teacherTableWidget.item(self.row, 1).text()
        group = self.ui.ui.teacherTableWidget.item(self.row, 2).text()

        self.ui.teacherUi.fullNameInput.setText(sName)
        self.ui.teacherUi.emailInput.setText(email)
        self.ui.teacherUi.addButton.setText('Сохранить')

        # self.ui.teacherUi.groupBox.clear()
        # groupList = self.ui.con.get_groups()
        # self.ui.teacherUi.groupBox.addItems(groupList)
        # self.ui.teacherUi.groupBox.setCurrentIndex(groupList.index(group))

        self.ui.teacherUi.addButton.clicked.connect(self.editTeacherButtonClicked)
        self.ui.teacherWindow.show()

    def editTeacherButtonClicked(self):
        prevName = self.ui.ui.teacherTableWidget.item(self.row, 0)
        prevEmail = self.ui.ui.teacherTableWidget.item(self.row, 1)
        lessons = self.ui.ui.teacherTableWidget.item(self.row, 2)

        print(lessons)


        # fullName = self.ui.teacherUi.fullNameInput.text()
        # email = self.ui.teacherUi.emailInput.text()
        # group = self.ui.teacherUi.groupBox.currentText()
        #
        # fullName_ = fullName.split(' ')
        # pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        # email_ = pattern.search(email)
        #
        # if any([False if 2 <= len(fullName_) <= 3 else True, False if email_ else True]):
        #     print('Неправильно введено ФИО или почта')
        #     return
        # if self.ui.con.get_user(email):
        #     print('Уже есть пользователь с такой почтой')
        #     return
        #
        # self.ui.con.update_student(fullName, email, group, prevName.text(), prevEmail.text(), prevGroup.text())
        # prevName.setText(fullName)
        # prevEmail.setText(email)
        # prevGroup.setText(group)
        # self.ui.closeStudentWindow()
