# 特定用途的对话框
# 5. QFileDialog -- 文件对话框
"""
静态方法：
* 以下静态方法都涉及的参数：caption(对话框标题)、dir(初始目录)、filter(过滤器，哪些文件类型可被选择)、options(选项，一些细节的设置)

1、getOpenFileName -- 只能选择单个文件
2、getOpenFileNames -- 可选择多个文件
3、getOpenFileUrl -- 可选择单个远端计算机的文件
4、getOpenFileUrls -- 可选择多个远端计算机的文件
5、getExistingDirectory -- 只能选择单个目录
6、getExistingDirectoryUrl -- 可选择多个目录
7、getSaveFileName -- 将文件保存在本地（dir为默认保存路径，filter为默认扩展名）
8、getSaveFileUrl -- 将文件保存在远端计算机
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
        button = QPushButton('File')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)
        button.clicked.connect(self.window_event)

    def window_event(self):
        # print(QFileDialog.getExistingDirectory(self, '打开', '/Users/kai'))
        print(QFileDialog.getSaveFileName(self, '保存', '/Users/kai', '*.py'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
