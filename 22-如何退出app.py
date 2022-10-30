# 退出应用程序 -- 调用app的quit方法

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        button1 = QPushButton('Open')
        button2 = QPushButton('Quit')
        box = QHBoxLayout()
        box.addWidget(button1)
        box.addWidget(button2)
        self.setLayout(box)

        button2.clicked.connect(self.window_event)

    def window_event(self):
        # app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
