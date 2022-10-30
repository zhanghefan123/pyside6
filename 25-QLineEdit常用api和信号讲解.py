# 表单 -- QLineEdit
"""
QLineEdit常用api：
1、setText() -- 设置表单中的文本
2、setMaxLength() -- 设置最大输入字符数
3、setPlaceholderText() -- 设置"底部"文本
4、setEchoMode() -- 设置
5、setAlignment() -- 设置对齐方式
6、setReadOnly() -- 设置"只读"模式
7、selectAll() -- 全选表单中的所有文本
8、selectedText() -- 返回表单中被选定的文本
9、cut()、copy()、del_()、paste() -- 分别为：剪切、复制、删除、粘贴
10、setClearButtonEnabled() -- 设置"一键清除"的按钮是否可用
11、setEchoMode() -- 设置表单的"回显"模式
    QLineEdit.Normal：正常形式
    QLineEdit.NoEcho：不显示输入的内容
    QLineEdit.Password：会以"*"来显示表单中的内容
    QLineEdit.PasswordEchoOnEdit：当表单失去焦点时，以password方式显示表单中的内容

12、text() -- 返回表单中的所有文本
13、addAction() -- 在表单中添加"操作动作"或图片；排列方式有两种：QLineEdit.LeadingPosition、QLineEdit.TrailingPosition

QLineEdit常用信号：
1、textChanged -- 当表单中的文本发生改变时，或者调用setText方法改变表单内容时会触发
2、textEdited -- 当表单中的文本发生改变时会触发
3、selectionChanged -- 当在表单中选择的文本发生改变时触发
4、returnPressed -- 点击返回或者单击回车键时会触发
5、editingFinished -- 当点击返回、单击回车键或者表单失去焦点时会触发
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
        self.line_edit = QLineEdit()
        line_edit2 = QLineEdit()
        button1 = QPushButton('test')
        box = QHBoxLayout()
        box.addWidget(self.line_edit)
        box.addWidget(button1)
        box.addWidget(line_edit2)
        self.setLayout(box)

        button1.clicked.connect(self.window_event)
        self.line_edit.selectionChanged.connect(self.do_something)
        # self.line_edit.returnPressed.connect(self.event1)
        # self.line_edit.editingFinished.connect(self.event2)

        # self.line_edit.setMaxLength(5)
        # self.line_edit.setClearButtonEnabled(True)
        # self.line_edit.setText('hello')
        # self.line_edit.setAlignment(Qt.AlignRight)
        # self.line_edit.setReadOnly(True)
        # file = self.line_edit.addAction(QIcon('./photo/file_open.png'), QLineEdit.TrailingPosition)
        # file.triggered.connect(self.do_something)
        # self.line_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # self.line_edit.setPlaceholderText('姓名、昵称：')

    def window_event(self):
        # self.line_edit.selectAll()
        # print(self.line_edit.selectedText())
        print(self.line_edit.text())

    def do_something(self):
        global num
        num += 1
        print(num)

    def event1(self):
        print('hello world')

    def event2(self):
        print('hello python')

if __name__ == '__main__':
    num = 0
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
