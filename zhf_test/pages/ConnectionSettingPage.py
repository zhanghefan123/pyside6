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
        self.setHorizontalHeaderLabels(["索引", "链路类型", "链路信息"])
        self.setColumnWidth(0, 40)
        self.setColumnWidth(1, 90)
        self.setColumnWidth(2, 340)


class ConnectionSettings(QWidget):

    def __init__(self, data):
        super().__init__()
        # 进行公共数据的获取
        self.data = data
        self.initializeComponents()
        self.layOutSetting()
        self.bindFunctions()

    def initializeComponents(self):
        self.label0 = QLabel("链路通信参数配置")
        self.label1 = QLabel('生成星间链路')
        self.linkTableWidget = LinksTableWidget()
        self.button1 = QPushButton('生成哈密顿链路')
        self.button2 = QPushButton('清空所有链路')
        self.label2 = QLabel('卫星结点<-->卫星结点')
        self.label3 = QLabel('卫星结点<-->地面结点')
        self.comboBox1 = QComboBox()
        self.comboBox1.addItems(["1Mbps", "10Mbps", "1Gbps"])
        self.comboBox1.setCurrentIndex(1)
        self.comboBox2 = QComboBox()
        self.comboBox2.addItems(["1Mbps", "10Mbps", "1Gbps"])
        self.comboBox2.setCurrentIndex(1)

    def bindFunctions(self):
        self.button1.clicked.connect(self.generateHamiltonianLink)
        self.button2.clicked.connect(self.clearAllLinks)

    def layOutSetting(self):
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout1.addWidget(self.label1)
        self.vlayout1.addWidget(self.linkTableWidget)
        self.vlayout2 = QVBoxLayout()
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(5)
        self.formLayout = QFormLayout()
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.addRow(self.label2, self.comboBox1)
        self.formLayout.addRow(self.label3, self.comboBox2)
        self.vlayout2.addWidget(self.label0)
        self.vlayout2.addLayout(self.formLayout)
        self.frame.setLayout(self.vlayout2)
        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addWidget(self.frame)
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addWidget(self.button1)
        self.vlayout.addWidget(self.button2)
        self.setLayout(self.vlayout)

    def generateHamiltonianLink(self):
        # 我们这里仅仅考虑一个星座的情况
        orbit_num = self.data.allConstellations[0].orbitNum
        sat_per_orbit = self.data.allConstellations[0].satPerOrbit
        nodes = self.data.allConstellations[0].nodes
        cons_name = self.data.allConstellations[0].consName
        for nodeCurIndex in range(0, len(nodes)):
            # 进行同轨道内的星间链路的建立
            src_orbit_index = int(nodeCurIndex / sat_per_orbit)
            src_offset = nodeCurIndex % sat_per_orbit
            src_index = src_orbit_index * sat_per_orbit + src_offset
            # 通过源索引找到源卫星
            source_satellite = self.data.allConstellations[0].nodes[src_index]
            dest_orbit_index = int(nodeCurIndex / sat_per_orbit)
            dest_offset = (nodeCurIndex + 1) % sat_per_orbit
            dest_index = dest_orbit_index * sat_per_orbit + dest_offset
            # 通过目的索引找到目的卫星
            dest_satellite = self.data.allConstellations[0].nodes[dest_index]
            # 更新接口的索引
            source_satellite.ethNum += 1
            dest_satellite.ethNum += 1
            self.data.allLinks.addLink(NODE_TYPE_SATELLITE, source_satellite, NODE_TYPE_SATELLITE, dest_satellite,
                                       self.comboBox1.currentText(), cons_name,
                                       source_satellite.ethNum, dest_satellite.ethNum)
            # 下面进行相邻的轨道的星间链路的建立
            dest_orbit_index = src_orbit_index + 1
            dest_offset = src_offset
            if dest_orbit_index < orbit_num:
                dest_index = dest_orbit_index * sat_per_orbit + dest_offset
                dest_satellite = self.data.allConstellations[0].nodes[dest_index]
                # 更新接口的索引
                source_satellite.ethNum += 1
                dest_satellite.ethNum += 1
                self.data.allLinks.addLink(NODE_TYPE_SATELLITE, source_satellite, NODE_TYPE_SATELLITE, dest_satellite,
                                           self.comboBox1.currentText(), cons_name,
                                           source_satellite.ethNum, dest_satellite.ethNum)
        # 下面进行星地链路的建立
        # 首先进行每一颗卫星的遍历
        for satellite in nodes:
            # 进行卫星的遍历
            for ground in self.data.allGroundStations:
                # 进行卫星和地面的链路的建立
                satellite.ethNum += 1
                ground.ethNum += 1
                self.data.allLinks.addLink(NODE_TYPE_SATELLITE, satellite, NODE_TYPE_GROUNDSTATION, ground,
                                           self.comboBox2.currentText(), cons_name, satellite.ethNum,
                                           ground.ethNum, ground.groundStationName)
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

    def clearAllLinks(self):
        """
        清除所有的链路,并且将所有的卫星和地面站的eth全部置为0
        """
        self.data.allLinks.linkSet.clear()
        self.updateLinksTableWidget()
        for satellite in self.data.allConstellations[0].nodes:
            satellite.ethNum = -1
        for ground in self.data.allGroundStations:
            ground.ethNum = -1

