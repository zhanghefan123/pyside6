# 多行文本输入框 -- QTextEdit，可以处理纯文本(做为编辑器)和富文本(做为显示部件)，能够呈现的内容十分丰富
# 1. 作为编辑器使用
"""
1、copy()、clear()、cut()、paste()、selectAll()、redo() -- 依次是：复制、清除内容、剪切、粘贴、全选、撤销
2、setAlignment() -- 设置对齐方式
3、setCurrentFont() -- 通过传递QFont对象来对文字进行设置
4、setFontFamily() -- 设置字体
5、setFontItalic() -- 设置倾斜
6、setFontPointSize() -- 设置字号；默认字号是13
7、setFontUnderline() -- 设置下划线
8、setFontWeight() -- 设置加粗，数值介于1~1000
9、setPlaceholderText() -- 设置文本框的底层文本
10、setTextBackgroundColor() -- 设置背景颜色
11、setTextColor() -- 设置字体颜色
12、setReadOnly() -- 设置只读
13、find() -- 通过正则表达式查找到指定内容
14、setCurrentCharFormat() -- 通过传递QTextCharFormat对象来设置字符格式
15、textCursor() -- 返回当前文档中的QTextCursor对象（游标）
16、document() -- 返回当前文档的QTextDocument对象（整个文档）

QTextEdit常用信号：
1、textChanged -- 当文本框中的文本发生改变时会触发
2、selectionChanged -- 在文本框中选择文本时会触发
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def load():
    with open('test.txt') as file:
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
        self.text_edit.setText(str1)

        button1.clicked.connect(self.window_event)
        # self.text_edit.selectionChanged.connect(self.window_event)

    def window_event(self):
        # print('hello world')
        # self.text_edit.setFontItalic(True)
        # self.text_edit.setFontFamily('Monaco')
        # self.text_edit.setTextColor(Qt.GlobalColor.red)
        # self.text_edit.setAlignment(Qt.AlignCenter)
        # self.text_edit.setFontItalic(True)
        # self.text_edit.setTextColor(QColor('red'))
        self.text_edit.find('武汉')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
