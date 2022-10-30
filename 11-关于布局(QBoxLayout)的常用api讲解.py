# 布局 -- QBoxLayout；是QHBoxLayout（水平布局）和QVBoxLayout（垂直布局）的父类
"""
QBoxLayout常用api：
1、addWidget -- 往布局中添加控件
2、insertWidget -- 往布局中指定的索引处插入控件
3、addLayout -- 往布局中添加子布局
4、insertLayout -- 往布局中指定的索引处插入子布局
5、removeWidget -- 从布局中移除控件（另一个方法hide()）
6、replaceWidget -- 替换控件
7、addSpacing -- 添加空白
8、insertSpacing -- 往布局中指定的索引处插入空白
9、setSpacing -- 设置布局中的控件间的间距
10、setDirection -- 设置布局中控件排列方式
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
        self.button1 = QPushButton('Open')
        self.button2 = QPushButton('Save')
        self.button3 = QPushButton('Cannel')
        self.button4 = QPushButton('Yes')
        self.box = QBoxLayout(QBoxLayout.LeftToRight)

        self.box.addWidget(self.button1)
        self.box.addWidget(self.button2)
        self.box.addWidget(self.button3)
        # self.box.removeWidget(self.button2)

        self.setLayout(self.box)

        self.button1.clicked.connect(self.window_event)

    def window_event(self):
        # self.box.replaceWidget(self.button2, self.button3)
        # self.box.replaceWidget(self.button1, self.button3)
        self.button2.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
