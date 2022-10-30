# 关于控件的"伪状态" -- 伪状态可以包含：特定状态、特定功能
# 可查询官方文档：https://doc.qt.io/qt-6/stylesheet-reference.html#drop-down-sub
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
        box = QVBoxLayout()
        line_edit = QLineEdit()
        com_box = QComboBox()
        com_box.addItems(['Python', 'Java'])
        box.addWidget(line_edit)
        box.addWidget(com_box)
        self.setLayout(box)

        # line_edit.setEnabled(False)
        self.setStyleSheet(qss_read('test_qss.css'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
