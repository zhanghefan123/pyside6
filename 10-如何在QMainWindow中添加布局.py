# 在QMainWindow中添加布局 -- centralWidget()和setCentralWidget()


import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        button1 = QPushButton('Open')
        button2 = QPushButton('Cannel')
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        central_widget = QWidget()
        central_widget.setLayout(hbox)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
