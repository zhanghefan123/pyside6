# 为控件设置什么样儿的效果呢 -- qss声明（属性和值）
"""
属性包括以下这些分类（和css共通）：
1. 背景 -- background
2. 边框 -- border
3. 字体-- font
4. 宽高 -- min-width、min-height、max-width、max-height
5. 外边距 -- margin
6. 内边距 -- padding
7. 定位 -- position、left、right、top、bottom
8. 对齐、下划线、透明度 -- text-align、text-decoration、opacity
9. 轮廓 -- outline
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
        text_edit = QTextEdit()
        button = QPushButton('Test')
        box = QVBoxLayout(self)
        box.addWidget(text_edit)
        box.addWidget(button)

        self.setStyleSheet(qss_read('width-height.qss'))

        def window_event():
            print(text_edit.size())

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
