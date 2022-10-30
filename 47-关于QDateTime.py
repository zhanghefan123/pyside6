# QDateTime -- 时间日期对象
"""
常用api：
* 该类实现了QDate和QTime的所有方法

1、toSecsSinceEpoch() -- 返回QDateTime对应的时间戳（秒）
2、toMSecsSinceEpoch() -- 返回QDateTime对应的时间戳（毫秒）
3、toString() -- 将QDateTime转换成字符串
4、toUTC() -- 返回QDateTime对应的utc
5、setSecsSinceEpoch() -- 通过传递时间戳（秒）来修改QDateTime
6、setMSecsSinceEpoch() -- 通过传递时间戳（毫秒）来修改QDateTime


静态函数：
1、currentDateTime() -- 返回当前的QDateTime
2、currentDateTimeUtc() -- 返回当前的QDateTime的utc（"格林尼治"时间）
3、currentSecsSinceEpoch() -- 返回当前QDateTime的时间戳（秒）
4、currentMSecsSinceEpoch() -- 返回当前QDateTime的时间戳（毫秒）
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

        datetime = QDateTime(2020, 4, 23, 21, 35, 57)
        datetime.setSecsSinceEpoch(134566)
        print(datetime)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
