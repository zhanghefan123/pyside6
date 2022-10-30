# 为控件设置什么样儿的效果呢 -- qss声明（属性和值）
"""
qss独有属性：
1. gridline-color -- 设置QTableView网格线的颜色
2. icon-size -- 设置部分控件上的图标的尺寸
3. lineedit-password-mask-delay -- 设置表单上输入密码时回显延时，单位是毫秒
4. selection-color -- 设置"前景"色
5. selection-background-color -- 设置"背景"色
6. spacing -- 设置控件内部间距
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def qss_read(file):
    with open(file) as f:
        return f.read()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        # self.resize(500, 400)
        box = QVBoxLayout(self)
        line_edit = QLineEdit()
        button = QPushButton('Ok')
        box.addWidget(line_edit)
        box.addWidget(button)
        # line_edit.setEchoMode(QLineEdit.Password)

        self.setStyleSheet(qss_read('qss1.qss'))

        def window_event():
            pass

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
