from PySide6.QtWidgets import QMainWindow
from ui import mainUI
from data_sql import Connect


class RegWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = reg_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = Connect()

        self.ui.enterButton.clicked.connect(self.enterButtonClicked)

    def enterButtonClicked(self):
        email = self.ui.emailEdit.text()
        password = self.ui.passwordEdit.text()

        user = self.con.get_user(email)

        if not user:
            print('Ошибка, неправильно введена почта.')
            return

        if not user[2]:
            print('У вас отсутствует пароль, хотите зарегестрироваться?')
            return

        if user[2] != password:
            print('Ошибка, неправильно введён пароль.')
            return

        self.close()
        self.MainWindow = mainUI.MainWindow(user)
        self.MainWindow.show()
