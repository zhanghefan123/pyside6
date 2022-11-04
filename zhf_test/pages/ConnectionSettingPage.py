from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from zhf_test.common.ConstVariable import *


class LinksTableWidget(QTableWidget):

    # def __init__(self):
    #     super().__init__()
    #     self.setHorizontalHeaderLabels(["Index", "链路类型", "链路信息"])

    def __init__(self, row=0, column=3):
        super(LinksTableWidget, self).__init__(row, column)
        self.setHorizontalHeaderLabels(["Index", "链路类型", "链路信息"])
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 550)


class ConnectionSettings(QWidget):

    def __init__(self, data):
        super().__init__()
        # 进行公共数据的获取
        self.data = data
        self.initializeComponents()
        self.layOutSetting()
        self.bindFunctions()

    def initializeComponents(self):
        self.label1 = QLabel('生成星间链路')
        self.linkTableWidget = LinksTableWidget()
        self.button1 = QPushButton('生成哈密顿链路')

    def bindFunctions(self):
        self.button1.clicked.connect(self.generateHamiltonianLink)

    def layOutSetting(self):
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.label1)
        self.vlayout.addWidget(self.linkTableWidget)
        self.vlayout.addWidget(self.button1)
        self.setLayout(self.vlayout)

    def generateHamiltonianLink(self):
        # 我们这里仅仅考虑一个星座的情况
        orbit_num = self.data.allConstellations[0].orbitNum
        sat_per_orbit = self.data.allConstellations[0].satPerOrbit
        nodes = self.data.allConstellations[0].nodes
        for nodeCurIndex in range(0, len(nodes)):
            # 进行同轨道内的星间链路的建立
            src_orbit_index = int(nodeCurIndex / sat_per_orbit)
            src_offset = nodeCurIndex % sat_per_orbit
            src_index = src_orbit_index * sat_per_orbit + src_offset
            dest_orbit_index = int(nodeCurIndex / sat_per_orbit)
            dest_offset = (nodeCurIndex + 1) % sat_per_orbit
            dest_index = dest_orbit_index * sat_per_orbit + dest_offset
            self.data.allLinks.addLink(NODE_TYPE_SATELLITE, src_index, NODE_TYPE_SATELLITE, dest_index, 100)
            # 下面进行相邻的轨道的星间链路的建立
            dest_orbit_index = src_orbit_index + 1
            dest_offset = src_offset
            if dest_orbit_index < orbit_num:
                dest_index = dest_orbit_index * sat_per_orbit + dest_offset
                self.data.allLinks.addLink(NODE_TYPE_SATELLITE, src_index, NODE_TYPE_SATELLITE, dest_index, 100)
            # 然后我们需要将data之中的内容放到我们的tabWidget之中
            self.updateLinksTableWidget()

    def updateLinksTableWidget(self) -> None:
        """
        这里我们需要将我们的链路信息放到我们的表格之中
        :return:
        """
        self.linkTableWidget.setRowCount(len(self.data.allLinks.linkSet))
        for index in range(0, len(self.data.allLinks.linkSet)):
            self.linkTableWidget.setItem(index, 0, QTableWidgetItem(str(index)))
            self.linkTableWidget.setItem(index, 1, QTableWidgetItem(str(self.data.allLinks.linkSet[index].linkType)))
            self.linkTableWidget.setItem(index, 2, QTableWidgetItem(str(self.data.allLinks.linkSet[index].linkInfo)))
