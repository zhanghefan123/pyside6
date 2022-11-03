from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class LinksTableWidget(QTableWidget):

    # def __init__(self):
    #     super().__init__()
    #     self.setHorizontalHeaderLabels(["Index", "链路类型", "链路信息"])

    def __init__(self, row, column=3):
        super(LinksTableWidget, self).__init__(row, column)
        self.setHorizontalHeaderLabels(["Index", "链路类型", "链路信息"])
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 550)


class ConnectionSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeComponents()
        self.layOutSetting()

    def initializeComponents(self):
        self.label1 = QLabel('生成星间链路')
        self.linkTableWidget = LinksTableWidget()
        self.button1 = QPushButton('生成哈密顿链路')

    def layOutSetting(self):
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.label1)
        self.vlayout.addWidget(self.linkTableWidget)
        self.vlayout.addWidget(self.button1)
        self.setLayout(self.vlayout)
