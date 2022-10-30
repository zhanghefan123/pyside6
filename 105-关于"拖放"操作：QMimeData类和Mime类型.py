# QMimeData -- 用于保存与MIME类型相关联的数据
# 官方文档：QMimeData类用于描述存储在剪贴板中，并能通过拖放机制进行传输的信息（在剪贴板中，或者被拖动时的数据均以mime类型保存）

# 默认提供了5种mime类型用于存放对应的数据
"""
常用api：
1、setText() -- 将纯文本保存成mime类型
2、setHtml() -- 将富文本保存成mime类型
3、setUrls() -- 将url列表保存成mime类型
4、setImageData() -- 将图片保存成mime类型
5、setColorData() -- 将颜色保存成mime类型

6、hasText() -- 检查mimeData对象中是否有纯文本数据
7、hasHtml() -- 检查mimeData对象中是否有富文本数据
8、hasUrls() -- 检查mimeData对象中是否有url列表数据
9、hasImage() -- 检查mimeData对象中是否有图片数据
10、hasColor() -- 检查mimeData对象中是否有颜色数据

11、text() -- 获取mimeData对象中的纯文本数据
12、html() -- 获取mimeData对象中的富文本数据
13、urls() -- 获取mimeData对象中的url列表数据
14、imageData() -- 获取mimeData对象中的图片数据
15、colorData() -- 获取mimeData对象中的颜色数据
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
        pixmap = QPixmap('./photo/go.png')
        pixmap.scaled(40, 60, Qt.KeepAspectRatio)
        mime_data.setText('hello world')
        mime_data.setHtml('<h1>hello world</h1>')
        mime_data.setImageData(pixmap)

        dg.setPixmap(pixmap)

        dg.setMimeData(mime_data)
        dg.exec()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        # self.setText(event.mimeData().text())
        self.setText(event.mimeData().html())
        # self.setPixmap(event.mimeData().imageData())


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

        label2.setAcceptDrops(True)
        self.setStyleSheet(qss_read('test_qss.css'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
