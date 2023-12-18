import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel('Hello, PyQt5!', self)
        label.setGeometry(100, 100, 200, 30)

        button = QPushButton('Click me', self)
        button.setGeometry(100, 150, 200, 30)
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print('Button clicked!')

app = QApplication(sys.argv)
main_window = MyMainWindow()
main_window.show()
sys.exit(app.exec_())
