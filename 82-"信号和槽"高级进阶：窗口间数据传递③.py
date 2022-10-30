# 窗口间的数据传递；方法③ -- 使用自定义的信号
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Win2(QDialog):
    getText = Signal(int)

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
            value = spin_box.value()
            self.getText.emit(value)

        button.clicked.connect(window_event)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        # self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle('Window1')
        box = QVBoxLayout()
        self.line_edit = QLineEdit()
        button = QPushButton('Open')
        box.addWidget(self.line_edit)
        box.addWidget(button)
        # w = QWidget()
        self.setLayout(box)

        # self.setCentralWidget(w)
        win2 = Win2()
        def window_event():
            # win2.setWindowModality(Qt.WindowModal)
            win2.show()
            win2.exec()

        def do_something(var):
            self.line_edit.setText(str(var))

        button.clicked.connect(window_event)
        win2.getText.connect(do_something)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
