# QTimer -- 定时器；可设置持续触发或单次触发
# QTimer类为计时器提供了一个高级编程接口；要使用它，请创建一个QTimer，将其timeout信号连接到适当的插槽，然后调用start()；从那时起，它将以恒定的间隔发出timeout信号。
"""
QTimer常用api：
1、setTimerType() -- 设置精度，有三项枚举值可用：
    Qt.PreciseTimer：毫秒级精度，最精准
    Qt.CoarseTimer：一般精度，误差范围在5%以内（默认精度）
    Qt.VeryCoarseTimer：粗略精度，计时器基本上精度在1秒左右，对精度要求不高的地方用这个，可节省cpu资源

2、setInterval() -- 设置时间间隔，单位是毫秒
3、setSingleShot() -- 设置单次触发
4、start() -- 启动
5、stop() -- 停止

QTimer静态函数：
1、singleShot -- 设置单次触发（可以不用创建QTimer对象，比较方便）

QTimer信号：
1、timeout -- 当定时器start后触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel()
        button = QPushButton('Cancel')
        box = QHBoxLayout(self)
        box.addWidget(self.label)
        box.addWidget(button)
        self.label.setStyleSheet('font-size:20px')
        self.label.setText('请稍等..')
        # QTimer.singleShot(2000, self.window_event)

        self.time = QTimer(self)
        self.time.setInterval(2000)
        # time.setTimerType(Qt.PreciseTimer)
        # self.time.setSingleShot(True)
        self.time.timeout.connect(self.window_event)
        button.clicked.connect(self.do_something)
        self.time.start()

    def window_event(self):
        now = QTime.currentTime().toString()
        self.label.setText(now)

    def do_something(self):
        self.time.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
