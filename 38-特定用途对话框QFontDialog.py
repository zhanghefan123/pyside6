# 特定用途的对话框
# 3. QFontDialog -- 字体对话框
"""
静态方法：
getFont -- 快速创建字体对话框，返回值是由按钮布尔值和QFont对象组成的列表

1、setOption()、setOptions() -- 设置"选项"，一定程度上改变外观和可选择的字体：

    QFontDialog.NoButtons：在对话框中不显示OK和Cancel按钮
    QFontDialog.DontUseNativeDialog：在Mac上使用Qt的标准字体对话框，而不是Apple的本机字体面板
    QFontDialog.ScalableFonts：显示可缩放字体
    QFontDialog.NonScalableFonts：显示不可缩放的字体
    QFontDialog.MonospacedFonts：显示等宽字体
    QFontDialog.ProportionalFonts：显示比例字体

2、setCurrentFont() -- 通过QFont对象设置对话框中的默认字体
3、exec() -- 显示对话框，返回值是按钮的序号（ok为1，cancel为0）
3、currentFont() -- 获取当前选择的字体；返回值是一个QFont对象
4、selectedFont() -- 获取当前选定的字体；返回值是一个QFont对象

常用信号：
1、currentFontChanged -- 当前字体发生变化时会触发
2、fontSelected -- 当选中字体之后会触发
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
        button = QPushButton('Font')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)
        button.clicked.connect(self.window_event)

    def window_event(self):
        self.font_dialog = QFontDialog()
        # font_dialog.setOption(QFontDialog.DontUseNativeDialog)
        self.font_dialog.setCurrentFont(QFont('STFfangsong', 16, 1, False))

        # self.font_dialog.currentFontChanged.connect(self.do_something)
        result = self.font_dialog.exec()
        # if not result:
        #     print(self.font_dialog.selectedFont())
        # else:
        #     print(self.font_dialog.selectedFont())

    def do_something(self):
        print(self.font_dialog.currentFont())
        print(self.font_dialog.selectedFont())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
