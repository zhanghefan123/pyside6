"""
窗口控件（QWidget）主要api：
最大、最小尺寸和页面边距相关：
1、minimumWidth()、minimumHeight() -- 最小宽度和最小高度
2、maximumWidth()、maximumHeight() -- 最大宽度和最大高度
3、minimumSize()、maximumSize() -- 最小尺寸、最大尺寸
4、setMaximumWidth() -- 设置最大宽度
5、setMaximumHeight() -- 设置最大高度
6、setMinimumWidth() -- 设置最小宽度
7、setMinimumHeight() -- 设置最小高度
8、setMinimumSize() -- 设置最小尺寸
9、setMaximumSize() -- 设置最大尺寸
10、setFixedWidth() -- 设置固定的宽度
11、setFixedHeight() -- 设置固定的高度

10、setContentsMargins(左, 上, 右, 下) -- 设置内边距
11、contentsMargins() -- 返回内边距的值
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.window_ui()

    def window_ui(self):
        button1 = QPushButton('Open')
        button2 = QPushButton('Cannel')
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        self.setLayout(hbox)
        button1.clicked.connect(self.window_event)

    def window_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
