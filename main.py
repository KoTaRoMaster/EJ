import sys
from ui.regUI import RegWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegWindow()
    window.show()
    sys.exit(app.exec())
