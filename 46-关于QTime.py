# QTime -- 时间对象
"""
常用api：
1、 addSecs()、addMSecs() -- 增加或减少秒或者毫秒
2、hour()、minute()、second() -- 返回小时、分钟、秒
3、secsTo()、msecsTo() -- 返回两个QTime之间间隔的秒数和毫秒数
4、toString() -- 将QTime转换成字符串

    hh  --- 小时
    mm  --- 分钟
    ss  --- 秒


静态函数：
1、currentTime() -- 返回当前的QTime
2、fromString() -- 将日期字符串转换成QTime
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        label = QLabel('测试用...')
        box = QHBoxLayout()
        box.addWidget(label)
        self.setLayout(box)

        time = QTime(20, 35, 46)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
