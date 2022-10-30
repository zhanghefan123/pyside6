# QSpinBox -- 计数器
"""
QSpinBox常用api：
1、setMinimum()、setMaximum()、setRange() -- 设置计数器最小值、最大值、计数范围
2、maximum()、minimum() -- 返回当前设置的最大值和最小值
3、setPrefix()、setSuffix() -- 设置前缀和后缀
4、prefix()、suffix() -- 返回前缀和后缀
5、setValue() -- 设置计数器上显示的值
6、value() -- 返回计数器当前的值
7、setSingleStep() -- 设置步长值
8、setAlignment() -- 设置对齐方式；其值由Qt模块提供
9、setAccelerated() -- 设置计数器可加速

QSpinBox常用信号：
1、valueChanged -- 当计数器上的值发生改变时会触发
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
        self.spinbox = QSpinBox()
        button = QPushButton('Test')
        box = QHBoxLayout()
        box.addWidget(self.spinbox)
        box.addWidget(button)
        self.setLayout(box)

        self.spinbox.setFixedWidth(70)
        self.spinbox.setRange(0, 99)
        # self.spinbox.setSingleStep(3)
        # self.spinbox.setValue(50)
        # self.spinbox.setPrefix('$')
        self.spinbox.setAlignment(Qt.AlignRight)
        self.spinbox.setAccelerated(True)
        # self.spinbox.setSingleStep(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
