# 拖放 -- 是用户在应用程序中复制或移动数据的直观方式，在许多桌面环境中用作在应用程序之间复制数据的机制；
# 拖放操作包括两个动作：拖动(drag)和放下(drop)；当被拖动时拖动的数据会被存储为MIME类型的对象，MIME类型使用QMimeData类来描述（MIME类型通常由剪贴板和拖放系统使用，以识别不同类型的数据）
"""
简单的拖放操作实现步骤：
1. 被拖动的控件设置setDragEnabled()；允许被拖动
2. 接收拖放的控件设置setAcceptDrops()；允许数据落下
3. 接收拖放的控件可以重新实现几个和拖放相关的事件处理函数，包括：

    QDragEnterEvent -- 拖动进入事件；当拖动操作进入控件范围时会触发；如果忽略该事件，将会导致后续的拖放事件不能被触发
    QDragMoveEvnet -- 拖动移动事件；当拖动操作正在进行时，以及当具有焦点时按下键盘的修饰键(比如Ctrl)时会触发（注意：要使控件能接收到该事件，则必须接受QDragEnterEvent事件）
    QDropEvent -- 放下事件；在完成拖放操作时，即当用户在控件上放下一个对象时会触发（注意：要使控件能接收到该事件，则必须接受QDragEnterEvent事件，且不能忽略QDragMoveEvnt事件）
    QLeaveEvent -- 当拖动操作离开控件时会触发（注意：要使控件能接收到该事件，必须要使拖动先进入该控件(即产生QDragEnterEvent事件)，然后再离开该控件，才会触发QLeaveEvent事件）

"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class ComBox(QComboBox):
    # def mouseMoveEvent(self, event):
    #     dg = QDrag(self)
    #     mime_data = QMimeData()

    def dragEnterEvent(self, event):
        event.accept()
        # print('hello world')

    # def dragMoveEvent(self, event):
    #     print('hello world')

    def dropEvent(self, event):
        print('hello world')

    # def leaveEvent(self, event):
    #     print('hello')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        line_edit = QLineEdit()
        com_box = ComBox()
        box = QHBoxLayout(self)
        box.addWidget(line_edit)
        box.addWidget(com_box)

        line_edit.setDragEnabled(True)
        com_box.setAcceptDrops(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
