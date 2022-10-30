# 改变控件样式的方式有如下几种：
# 样式 -- 显示出来的效果，呈现的样子
"""
1、子类化QStyle，或者创建一个预定义的风格
2、子类化个别的控件类，并且重新实现它的绘制和鼠标事件处理器
3、Qt样式表（qss）

qss的格式：选择器{声明（属性：属性值）}

    如何在引入样式表呢 --

    ①. 内部的qss加载
    ②. 外部的qss加载
    注意：无论是内部加载还是外部加载，都使用setStyleSheet方法
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
        button = QPushButton('Python')
        line_edit = QLineEdit()
        box = QHBoxLayout(self)
        box.addWidget(button)
        box.addWidget(line_edit)

        # button.setStyleSheet('color:red;background:black;')
        self.setStyleSheet(qss_read('qss1.qss'))
        # self.setStyleSheet('''
        # QPushButton{color: red;}
        # QLineEdit{background: green;}
        # ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
