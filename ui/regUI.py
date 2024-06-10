from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtSvg import QSvgRenderer

from ui import mainUI
from data_sql import Connect


from Windows.RegistrationWindow import Ui_RegistrationWindow

class RegWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)

        self.con = Connect()

        for user in self.con.get_users():
            print(user)
        print('-'*30)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.passwortFrame.setHidden(True)

        self.ui.enterButton.clicked.connect(self.enterButtonClicked)
        self.ui.passwordButton.clicked.connect(self.swapPassword)

    def enterButtonClicked(self):
        email = self.ui.emailEdit.text()
        user = self.con.get_user(email)

        if not user:
            print('Ошибка, неправильно введена почта.')
            return

        self.ui.passwortFrame.setHidden(False)
        if not user[2]:
            self.ui.enterButton.setText('Зарегестрироваться')
            self.ui.enterButton.clicked.disconnect()
            self.ui.emailEdit.setReadOnly(True)
            self.ui.enterButton.clicked.connect(self.registrationButtonClicked)
            return

        password = self.ui.passwordEdit.text()
        if user[2] != password:
            return

        self.close()
        self.MainWindow = mainUI.MainWindow(user, self.con)
        self.MainWindow.show()

    def swapPassword(self, state):
        if state:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Password)

    def registrationButtonClicked(self):
        email = self.ui.emailEdit.text()
        password = self.ui.passwordEdit.text()

        self.con.registration_user(email, password)

        self.ui.emailEdit.setReadOnly(False)
        self.ui.emailEdit.setText('')
        self.ui.passwordEdit.setText('')
        self.ui.enterButton.setText('Войти')

        self.ui.enterButton.clicked.disconnect()
        self.ui.enterButton.clicked.connect(self.enterButtonClicked)

