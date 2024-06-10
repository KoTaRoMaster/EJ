import sys
from ui.regUI import RegWindow
from ui.mainUI import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow('admin@mail.ru')
    window.show()
    sys.exit(app.exec())
