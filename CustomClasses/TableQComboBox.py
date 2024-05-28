from PySide6.QtWidgets import QComboBox


class TableQComboBox(QComboBox):
    def __init__(self, column: int, row: int, con, ui):
        super(TableQComboBox, self).__init__()
        self.column = column
        self.row = row
        self.text = None
        self.con = con
        self.ui = ui

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