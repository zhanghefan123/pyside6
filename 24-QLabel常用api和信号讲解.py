# 标签 -- QLabel；能承载的东西种类比较丰富：文本、图片、动画
"""
QLabel常用api：
1、setText() -- 设置标签上的文本，可以传递"纯文本"和"富文本"
2、setPixmap() -- 可以将图片设置在标签上，标签尺寸会被拉伸成图片的尺寸
3、setMovie() -- 可让标签接收一个小动画
4、setNum() -- 可将int或float类型的数字转成文本，int类型只支持最大10位的整数，而float类型会以科学计数法展示
5、setIndent() -- 设置标签上文本的缩进
6、setMargin() -- 设置标签的内边距
7、setAlignment() -- 设置标签中文本的对齐方式；其值都在Qt模块中
8、setWordpWrap() -- 设置自动换行，此属性的值默认是False
9、selectedText() -- 返回用户选中的文本
10、setScaledContents() -- 让图片在标签中完整显示
11、text() -- 返回标签上的文本
12、setStyleSheet() -- 可以引入qss（样式表）属性对标签进行设置
13、setOpenExternalLinks() -- 可让标签中包含的链接被点击时，调用浏览器打开


QLabel常用信号：
1、linkHovered -- 当标签上的文本为富文本并且包含链接，鼠标滑过标签时触发
2、linkActivated -- 当标签上的文本为富文本并且包含链接，鼠标单击标签时触发
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
        self.label = QLabel('此标签用于测试，此标签用于测试..')
        # self.label.setFixedWidth(200)
        # self.label.setFixedHeight(200)
        button1 = QPushButton('Save')
        box = QHBoxLayout()
        box.addWidget(self.label)
        box.addWidget(button1)
        self.setLayout(box)
        self.label.setFrameShape(QFrame.Box)
        # button1.clicked.connect(self.window_event)
        # self.label.linkHovered.connect(self.do_something)

        self.label.setText('<a href="https://www.baidu.com">百度一下，你就知道</a>')
        # self.label.setText('<h1>这是一个标题</h1>')
        self.label.setOpenExternalLinks(True)
        # self.label.setIndent(30)
        # self.label.setMargin(30)
        # self.label.setFixedSize(QSize(200, 200))
        # self.label.setAlignment(Qt.AlignRight)
        # self.label.setWordWrap(True)
        # self.label.setPixmap(QPixmap('./photo/go.png'))
        # self.label.setScaledContents(True)
        # self.label.setStyleSheet('color: red;background-color: green;')
        # self.label.setPicture()

    def window_event(self):
        print(self.label.selectedText())

    def do_something(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
