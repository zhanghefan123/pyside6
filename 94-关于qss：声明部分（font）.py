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
        self.resize(500, 400)
        label = QLabel(self)
        label.move(100, 30)
        label.setText('Python Java C/C++')

        self.setStyleSheet(qss_read('font.qss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
