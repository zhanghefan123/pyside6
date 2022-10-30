# QDrag -- 控制拖放的类
"""
自定义拖放操作的步骤：
1. QDrag实例化创建对象
2. 创建mime类型对象，并将要拖放的数据存放在QDrag对象中 （涉及知识点：QMimeData）
3. 调用QDrag对象的exec()启动拖放

注意：在做以上步骤之前要先决定启动拖放的时机（在什么时候启动拖放：具体事件或者信号）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def qss_read(file):
    with open(file) as f:
        return f.read()


class Label(QLabel):
    def mousePressEvent(self, event):
        dg = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        dg.setMimeData(mime_data)
        dg.exec()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(400, 0)
        label1 = Label()
        label2 = Label()
        box = QHBoxLayout(self)
        box.addWidget(label1)
        box.addSpacing(50)
        box.addWidget(label2)
        label1.setText('这是一段测试的文本...')

        label2.setAcceptDrops(True)
        # self.setStyleSheet(qss_read('test_qss.css'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
