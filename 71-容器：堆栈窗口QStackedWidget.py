# QStackedWidget -- 堆栈窗口；可将窗口绑定给不同的控件触发显示
"""
QStackedWidget常用api：
1、addWidget() -- 添加窗口
2、insertWidget() -- 在指定索引处添加窗口
3、count() -- 返回堆栈中的窗口数量
4、currentIndex() -- 返回当前窗口索引
5、currentWidget() -- 返回当前窗口
6、removeWidget() -- 从堆栈中移除窗口
7、setCurrentIndex() -- 设置当前呈现的窗口（接收索引）
8、setCurrentWidget() -- 设置当前呈现的窗口（接收窗口）

QStackedWidget信号：
1、currentChanged -- 当前窗口改变时会触发
2、widgetRemoved -- 移除窗口时会触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class test_widge(QWidget):
    def __init__(self, text):
        super(test_widge, self).__init__()
        button = QPushButton(f'{text}')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(QSize(300, 200))
        self.sw = QStackedWidget()
        self.list_widget = QListWidget()
        self.list_widget.addItems(['window1', 'window2', 'window3'])
        box = QHBoxLayout()
        box.addWidget(self.list_widget)
        box.addWidget(self.sw)
        self.setLayout(box)

        test1 = test_widge('welcome!')
        test2 = test_widge('green')
        test3 = test_widge('blue')
        test4 = test_widge('red')
        self.sw.addWidget(test1)
        self.sw.addWidget(test2)
        self.sw.addWidget(test3)
        self.sw.addWidget(test4)
        # print(self.sw.count())

        self.list_widget.itemClicked.connect(self.window_event)

    def window_event(self):
        self.sw.setCurrentIndex(self.list_widget.currentRow() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
