# 如何设置控件在布局中的比例
"""
setSizePolicy() -- 设置布局中的控件的"小大策略"；其值有以下几种：

    QSizePolicy.Fixed -- 固定值；代表不能进行拉伸
    QSizePolicy.Minimum -- 最小值；拉伸范围是：控件的最小值~无限
    QSizePolicy.Maximum -- 最大值；拉伸范围是：控件的最小值~控件的最大值
    QSizePolicy.Preferred -- 可任意拉伸，但拉伸范围仍在合理范围内；拉伸范围是：控件的最小值~无限
    QSizePolicy.Expanding -- 可任意拉伸，但拉伸范围仍在合理范围内，享有优先拉伸权；拉伸范围是：控件的最小值~无限
    QSizePolicy.Ignored -- 忽略控件固有的最大值和最小值进行拉伸，可将控件压缩至消失

setStretchFactor() -- 设置拉伸比例
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
        # self.resize(500, 60)
        self.button1 = QPushButton('Open')
        self.button2 = QPushButton('Save')
        self.button3 = QPushButton('Cannel')
        box = QBoxLayout(QBoxLayout.LeftToRight)
        box.addWidget(self.button1)
        box.addWidget(self.button2)
        box.addWidget(self.button3)
        # self.button1.setMinimumWidth(200)
        # self.button1.setMaximumWidth(400)
        # self.button1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        # self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # box.setStretchFactor(self.button1, 3)
        # box.setStretchFactor(self.button2, 1)
        # box.setStretchFactor(self.button3, 1)

        self.setLayout(box)
        self.button1.clicked.connect(self.window_event)

    def window_event(self):
        print(self.button1.width())
        print(self.button2.width())
        print(self.button3.width())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
