# 窗口间的数据传递；方法② -- 使用全局变量
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Win2(QDialog):
    def __init__(self):
        super(Win2, self).__init__()
        self.setWindowTitle('Window2')
        self.setWindowModality(Qt.ApplicationModal)
        box = QHBoxLayout()
        spin_box = QSpinBox()
        button = QPushButton('Ok')
        box.addWidget(spin_box)
        box.addWidget(button)
        self.setLayout(box)
        spin_box.setRange(0, 100)

        def window_event():
            global var
            var = str(spin_box.value())

        button.clicked.connect(window_event)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Window1')
        box = QVBoxLayout()
        self.line_edit = QLineEdit()
        button = QPushButton('Open')
        box.addWidget(self.line_edit)
        box.addWidget(button)
        self.setLayout(box)

        win2 = Win2()

        def window_event():
            win2.show()
            win2.exec()
            self.line_edit.setText(var)

        button.clicked.connect(window_event)


if __name__ == '__main__':
    var = ''
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
