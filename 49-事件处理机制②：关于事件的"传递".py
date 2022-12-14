# 关于事件的"传递" -- 事件被传递到控件的事件处理函数后，如果事件处理函数忽略事件，那么事件会被一直向上传递给它的父级控件，直到事件被处理
"""
1、事件被传递给产生事件的控件的对应事件处理函数
2、事件被传递给控件的父级控件的对应事件处理函数
3、事件被传递给控件父级的父级控件的对应事件处理函数
4、事件被传递给QObject的对应事件处理函数


QEvent的api：
1、accept -- 接受事件
2、ignore -- 拒绝事件
3、isAccepted -- 判断事件是否被接受，接受返回True，拒绝返回False
4、spontaneous -- 判断事件是否由应用程序以外的操作引发，如果事件由用户交互引发，返回True，否则返回False
5、type -- 返回事件类型
"""
import sys

import PySide6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_line_edit(QLineEdit):
    def mousePressEvent(self, event):
        event.ignore()
        # 除了接受事件，我们还可以进行事件的拒绝，这个事件还没有解决
        # 因为他下面没有了，所以需要开始向上进行传递
        # 所以这里的代码之中会输出的结果是 this is window 以及 this is line_edit
        print('this is line_edit')

    def keyPressEvent(self, arg__1: PySide6.QtGui.QKeyEvent) -> None:
        # 我们需要执行其原本的功能，所以需要调用父类的方法
        super(my_line_edit, self).keyPressEvent(arg__1)
        # 下面是我们自己的附加的方法
        print('this is line_edit')

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        line_edit = my_line_edit()
        box = QHBoxLayout()
        box.addWidget(line_edit)
        self.setLayout(box)

    def mousePressEvent(self, event):
        print('this is window')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
