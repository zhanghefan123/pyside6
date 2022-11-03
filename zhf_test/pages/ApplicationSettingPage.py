from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class ApplicationSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.vlayout = QVBoxLayout()
        self.hlayout1 = QHBoxLayout()
        self.setLayout(self.vlayout)
        self.hlayout1.addWidget(QLabel('Application Setting'))
        self.hlayout1.addWidget(QPushButton('Application Setting Button'))
        self.vlayout.addLayout(self.hlayout1)