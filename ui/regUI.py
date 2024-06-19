from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtSvg import QSvgRenderer

from ui.mainUI import MainWindow
from data_sql import Connect

from Windows.RegistrationWindow import Ui_RegistrationWindow


class RegWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_RegistrationWindow()
        self.ui.setupUi(self)

        self.con = Connect()

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.passwortFrame.setVisible(False)

        self.ui.enterButton.clicked.connect(self.enterButtonClicked)
        self.ui.passwordButton.clicked.connect(self.swapPassword)

    def enterButtonClicked(self):
        email = self.ui.emailEdit.text()
        user = self.con.get_user(email)

        self.ui.errorEmailLabel.setText('')
        self.ui.errorLabel.setText('')

        if not email:
            self.ui.errorEmailLabel.setText('Поле не должно быть пустым, введите почту.')
            return

        if not user:
            self.ui.errorEmailLabel.setText('Ошибка! Не правильно введёна почта.')
            return

        self.ui.errorEmailLabel.setText('')
        if not user[2]:
            self.ui.passwortFrame.setVisible(True)
            self.ui.enterButton.setText('Зарегестрироваться')
            self.ui.enterButton.clicked.disconnect()
            self.ui.emailEdit.setReadOnly(True)
            self.ui.enterButton.clicked.connect(self.registrationButtonClicked)
            return

        if not self.ui.passwortFrame.isVisible():
            self.ui.passwortFrame.setVisible(True)
            return

        password = self.ui.passwordEdit.text()
        if user[2] != password:
            self.ui.errorLabel.setText('Ошибка! Не правильно введён пароль.')
            return

        self.hide()
        self.MainWindow = MainWindow(user, self.con, self)
        self.MainWindow.show()

        self.ui.errorEmailLabel.setText('')
        self.ui.errorLabel.setText('')
        self.ui.emailEdit.setText('')
        self.ui.passwordEdit.setText('')
        self.ui.passwortFrame.setVisible(False)

    def swapPassword(self, state):
        if state:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Password)

    def registrationButtonClicked(self):
        email = self.ui.emailEdit.text()
        user = self.con.get_user(email)
        password = self.ui.passwordEdit.text()

        self.ui.errorLabel.setText('')
        self.ui.errorEmailLabel.setText('')

        check = False
        if not email:
            self.ui.errorEmailLabel.setText('Поле не должно быть пустым, введите почту.')
            check = True

        if not user:
            self.ui.errorEmailLabel.setText('Ошибка! Не правильно введёна почта.')
            check = True

        if len(password) < 8:
            self.ui.errorLabel.setText('Ошибка! Пароль должен быть не мменее 8 символов.')
            check = True

        if not password:
            self.ui.errorLabel.setText('Поле не должно быть пустым, введите пароль.')
            check = True

        if check:
            return
        self.con.registration_user(email, password)

        self.ui.emailEdit.setReadOnly(False)
        self.ui.emailEdit.setText('')
        self.ui.passwordEdit.setText('')
        self.ui.enterButton.setText('Войти')

        self.ui.enterButton.clicked.disconnect()
        self.ui.enterButton.clicked.connect(self.enterButtonClicked)
