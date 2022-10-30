# 特定用途的对话框
# 1. QMessageBox -- 消息对话框
"""
QMessageBox静态方法快速构建简单的对话框：
1、about() -- 创建"关于"对话框
2、information() -- 创建"提示"对话框
3、question() -- 创建"疑问"对话框
4、warning() -- 创建"警告"对话框
5、critical() -- 创建"错误"对话框
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
        button = QPushButton('MessageBox')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)

        button.clicked.connect(self.window_event)

    def window_event(self):
        message_box = QMessageBox.information(self, 'test..', '你需要提示吗？', QMessageBox.Cancel | QMessageBox.Ok)
        print(message_box)
        QMessageBox.critical()


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
