# 特定用途的对话框
# 4. QColorDialog -- 颜色对话框
"""
静态方法：
getColor -- 快速创建颜色对话框，返回值是QColor对象

1、setOption()、setOptions() -- 设置"选项"，一定程度上改变外观、为对话框添加一些设置项：

    QColorDialog.NoButtons：在对话框中不显示OK和Cancel按钮
    QColorDialog.DontUseNativeDialog：使用Qt的标准颜色对话框而不是操作系统的颜色对话框
    QColorDialog.ShowAlphaChannel：允许用户选择颜色的透明度

2、setCurrentColor() -- 通过QColor对象设置对话框中的默认颜色
3、exec() -- 显示对话框，返回值是按钮的序号（ok为1，cancel为0）
3、currentColor() -- 获取当前选择的颜色；返回值是一个QColor对象
4、selectedColor() -- 获取当前选定的颜色；返回值是一个QColor对象
5、customCount() -- 返回可设置的"快捷颜色"的数量，最多是16个
6、setCustomColor() -- 设置"快捷颜色"
7、customColor() -- 返回指定的"快捷颜色"

常用信号：
1、currentColorChanged -- 当前颜色发生变化时会触发
2、colorSelected -- 当选中颜色之后会触发
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
        button = QPushButton('Color')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)

        button.clicked.connect(self.window_event)

    def window_event(self, col):
        color_dialog = QColorDialog()
        color_dialog.setOption(QColorDialog.ShowAlphaChannel)
        # color_dialog.setCustomColor(3, QColor(146, 56, 79))

        color_dialog.colorSelected.connect(self.do_something)
        color_dialog.exec()


    def do_something(self, color):
        print(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
