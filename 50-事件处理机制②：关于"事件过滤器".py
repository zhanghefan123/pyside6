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

        return super(my_lineedit, self).keyPressEvent(event)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        line_edit = QLineEdit()
        spin_box = QSpinBox()
        combox = QComboBox()
        combox.setEditable(True)
        box = QVBoxLayout()
        box.addWidget(line_edit)
        box.addWidget(spin_box)
        box.addWidget(combox)
        self.setLayout(box)

        line_edit.installEventFilter(self)
        spin_box.installEventFilter(self)
        combox.installEventFilter(self)

    # def eventFilter(self, watched, event):
    #     super(Window, self).eventFilter(watched, event)
    #     if event.type() == QKeyEvent.KeyPress:
    #         if event.key() == 32:
    #             print('hello world')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
