# 多行文本输入框 -- QTextEdit，可以处理纯文本(做为编辑器)和富文本(做为显示部件)，能够呈现的内容十分丰富
# 2. 作为显示部件使用
"""
1、setHtml()、insertHtml() -- 往输入框中插入富文本；注意：对html元素以及元素的属性支持较好，但是css大多数并不支持
2、setMarkdown() -- 往输入框中插入markdown文本
3、append() -- 换行插入文本
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


# 将内容读取到一个字符串中
def load():
    with open('./txtFiles/test.txt') as file:
        str1 = file.read()
    return str1


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        self.text_edit = QTextEdit()
        button1 = QPushButton('Test')
        button2 = QPushButton('Cancel')

        box = QGridLayout()
        box.addWidget(self.text_edit, 0, 0, 5, 4)
        box.addWidget(button1, 5, 2)
        box.addWidget(button2, 5, 3)
        self.setLayout(box)
        str1 = load()
        # 进行内容的设置
        self.text_edit.setHtml(str1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
