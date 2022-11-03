# 1. QMessageBox -- 消息对话框
"""
QMessageBox常用api：
1、setText() -- 设置主文本，可接收富文本
2、setInformativeText() -- 设置副文本，可接收富文本
3、setWindowTitle() -- 设置对话框标题
4、addButton() -- 设置按钮
5、setStandardButtons() -- 设置QMessageBox按钮
6、setIcon() -- 设置QMessageBox图标；有五项，分别是：QMessageBox.NoIcon、QMessageBox.Question、QMessageBox.Information、QMessageBox.Warning、QMessageBox.Critical
7、setIconPixmap() -- 设置图片
8、setCheckBox() -- 设置多选按钮
9、setDefaultButton() -- 设置"默认"按钮（按下回车时激活的按钮）
10、setEscapeButton() -- 设置"转义"按钮（按下ESC时激活的按钮）
11、setDetailedText() -- 设置带有"详细说明"文本的按钮
12、exec() -- 显示消息对话框，返回值是按钮的序号
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class My_message(QMessageBox):
    def __init__(self):
        super(My_message, self).__init__()
        self.setText('<h1>这是一个测试的消息对话框</h1>')
        self.setInformativeText('爸爸告诉我：一定要好好学习！')
        self.setWindowTitle('test...')

        # self.addButton(QMessageBox.Ok)
        # self.setStandardButtons(QMessageBox.Cancel)
        # self.setIcon(QMessageBox.Question)
        # self.setIconPixmap(QPixmap('./icons/go.png'))
        # button1 = QCheckBox('今天你学习了吗？', self)
        # self.setCheckBox(button1)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        button = QPushButton('MessageBox')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)

        button.clicked.connect(self.window_event)

    def window_event(self):
        mess_ = My_message()
        result = mess_.exec()
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
