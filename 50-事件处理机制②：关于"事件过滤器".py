# 关于"事件过滤器" -- 在事件到达目标控件之前进行拦截，提前处理事件
"""
要实现事件过滤有两个步骤：
1、在目标控件上调用installEventFilter()，注册负责监视的控件
2、在监视对象的eventFilter（事件过滤器）中处理目标控件的事件
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_lineedit(QLineEdit):
    def keyPressEvent(self, event):
        if event.key() == 32:     # 当敲击空格时打印出"hello world"
            print('hello world')
        # 下面这行代码是实现原有的功能
        return super(my_lineedit, self).keyPressEvent(event)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        line_edit = my_lineedit()
        spin_box = QSpinBox()
        combox = QComboBox()
        combox.setEditable(True)
        box = QVBoxLayout()
        box.addWidget(line_edit)
        box.addWidget(spin_box)
        box.addWidget(combox)
        self.setLayout(box)

        # 在目标控件上调用installEventFilter()，传入的参数是负责监视的控件
        line_edit.installEventFilter(self)
        spin_box.installEventFilter(self)
        combox.installEventFilter(self)

    # 思想：如果不同的控件需要响应同样的一个事件，那么我们就可以在这个事件过滤器中进行汇总
    # 而不要重复的继承很多类并且进行重写的操作

    # 下面的代码就是事件过滤器
    # 在监视器对象上面重写eventFilter()方法
    def eventFilter(self, watched, event):
        super(Window, self).eventFilter(watched, event)
        if event.type() == QKeyEvent.KeyPress:
            print(event.key())
            if event.key() == 49:     # 这样当任意的一个组建当敲击1时打印出"hello world"
                print('hello world')
        # 如果返回的是True,那么事件就不会再传递给目标控件，而我们一般需要控件完成原有的功能
        # 如果返回的是False,类似于没有拦截到事件，事件会继续传递给目标控件
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
