from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from zhf_test.gen.ConsGeneration import ConsGeneration
from zhf_test.pojo.Constellation import Constellation
from zhf_test.pojo.GroundStation import GroundStation


class NodesTreeWidget(QTreeWidget):
    def __init__(self):
        super(NodesTreeWidget, self).__init__()
        self.setHeaderLabels(["结点类型", "主结点名称", "结点摘要"])
        self.constellations = QTreeWidgetItem(["星座网络"])
        self.groundStations = QTreeWidgetItem(["地面结点"])
        self.addTopLevelItems([self.constellations, self.groundStations])
        self.consGen = None


class NodeSetting(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.validation()
        self.initializeComponents()
        self.layoutSetting()
        self.bindFunction()
        # ------星座参数----------
        self.projectName = ""
        self.consName = ""
        self.orbitNum = 0
        self.satPerOrbit = 0
        self.inclination = 0
        self.startingPhase = 0
        self.altitude = 0
        # -----------------------
        # -------地面结点参数------
        self.groundStationName = ""
        self.latitude = 0
        self.longitude = 0
        # ------------------------

    def validation(self):
        self.intValidator1 = QIntValidator()
        self.intValidator1.setRange(1, 99)

        # 验证器3用来进行高度的验证
        self.intValidator3 = QIntValidator()
        self.intValidator3.setRange(1, 35768)

        # 验证器1用来进行轨道链路切换纬度的验证和轨道倾角的验证
        self.doubleValidator1 = QDoubleValidator()
        self.doubleValidator1.setNotation(QDoubleValidator.StandardNotation)
        self.doubleValidator1.setRange(0, 90)
        self.doubleValidator1.setDecimals(2)

        # 验证器2用来进行相位的验证
        self.doubleValidator2 = QDoubleValidator()
        self.doubleValidator2.setNotation(QDoubleValidator.StandardNotation)
        self.doubleValidator2.setRange(0, 360)
        self.doubleValidator2.setDecimals(2)

        # 验证器3用来进行经度的验证
        self.doubleValidator3 = QDoubleValidator()
        self.doubleValidator3.setNotation(QDoubleValidator.StandardNotation)
        self.doubleValidator3.setRange(0, 180)
        self.doubleValidator3.setDecimals(2)

        # 验证器4用来进行纬度的验证
        self.doubleValidator4 = QDoubleValidator()
        self.doubleValidator4.setNotation(QDoubleValidator.StandardNotation)
        self.doubleValidator4.setRange(-90, 90)
        self.doubleValidator4.setDecimals(2)

    def initializeComponents(self):
        self.textProjectName = QLabel("项目名称:")
        self.lineEditProjectName = QLineEdit()
        self.lineEditProjectName.setPlaceholderText("请输入项目名称:")
        # 这里我们要创建的是表单布局
        self.text0 = "星座名称:"
        self.lineEdit0 = QLineEdit()
        self.lineEdit0.setFixedWidth(100)
        self.lineEdit0.setPlaceholderText("请输入星座名称")
        self.text1 = "链路切换纬度(度):"
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("66.32")
        self.lineEdit1.setFixedWidth(100)
        self.lineEdit1.setValidator(self.doubleValidator1)
        self.text2 = QLabel("轨道的数量(根):")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("12")
        self.lineEdit2.setValidator(self.intValidator1)
        self.lineEdit2.setFixedWidth(100)
        self.text3 = QLabel("单个轨道的卫星数量(个):")
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText("24")
        self.lineEdit3.setValidator(self.intValidator1)
        self.lineEdit3.setFixedWidth(100)
        self.text4 = QLabel("轨道倾角(度):")
        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setValidator(self.doubleValidator1)
        self.lineEdit4.setPlaceholderText("90")
        self.lineEdit4.setFixedWidth(100)
        self.text5 = QLabel("初始相位(度):")
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setPlaceholderText("0")
        self.lineEdit5.setFixedWidth(100)
        self.lineEdit5.setValidator(self.doubleValidator2)
        self.text6 = QLabel("星座高度(km):")
        self.lineEdit6 = QLineEdit()
        self.lineEdit6.setPlaceholderText("780")
        self.lineEdit6.setFixedWidth(100)
        self.lineEdit6.setValidator(self.intValidator3)
        self.text7 = QLabel("地面站名称")
        self.lineEdit7 = QLineEdit()
        self.lineEdit7.setPlaceholderText("GND0")
        self.lineEdit7.setFixedWidth(100)
        self.text8 = QLabel("经度")
        self.lineEdit8 = QLineEdit()
        self.lineEdit8.setPlaceholderText("0")
        self.lineEdit8.setFixedWidth(100)
        self.lineEdit8.setValidator(self.doubleValidator3)
        self.text9 = QLabel("纬度")
        self.lineEdit9 = QLineEdit()
        self.lineEdit9.setPlaceholderText("0")
        self.lineEdit9.setFixedWidth(100)
        self.lineEdit9.setValidator(self.doubleValidator4)
        self.button1 = QPushButton("生成星座")
        self.button2 = QPushButton("生成地面站")
        self.button1.setFixedWidth(100)
        self.button2.setFixedWidth(100)
        self.frameLabel1 = QLabel("当前星座参数配置")
        self.frameLabel2 = QLabel("当前结点配置预览")
        self.frameLabel3 = QLabel("地面站的参数配置")

        # 进行右键弹出菜单的设置
        self.rightClickMenu = QMenu()
        self.modifyAction = self.rightClickMenu.addAction("修改结点")
        self.deleteAction = self.rightClickMenu.addAction("删除结点")

    def layoutSetting(self):
        # -----总体的最大布局--------
        self.vlayout = QVBoxLayout()
        # -------------------------

        # --------------------添加项目名称的输入------------------------
        self.hlayoutForProjectName = QHBoxLayout()
        self.hlayoutForProjectName.addWidget(self.textProjectName)
        self.hlayoutForProjectName.addWidget(self.lineEditProjectName)
        self.frameProjectName = QFrame()
        self.frameProjectName.setFrameShape(QFrame.Box)
        self.frameProjectName.setLineWidth(5)
        self.frameProjectName.setLayout(self.hlayoutForProjectName)
        self.vlayout.addWidget(self.frameProjectName)
        # ------------------------------------------------------------

        self.hlayout = QHBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.frame1 = QFrame()
        # 下面是表单的布局的设置
        self.formLayout1 = QFormLayout()
        self.formLayout1.setVerticalSpacing(5)
        self.formLayout1.setHorizontalSpacing(20)
        self.frame1.setLayout(self.formLayout1)
        self.frame1.setFixedWidth(370)
        self.frame1.setFixedHeight(200)
        self.frame1.setFrameShape(QFrame.Box)
        self.frame1.setLineWidth(5)
        # self.frame1.setFixedWidth(400)
        # self.frame1.setFixedHeight(250)
        self.vlayout1.addWidget(self.frameLabel1)
        self.vlayout1.addWidget(self.frame1)
        self.formLayout1.addRow(self.text0, self.lineEdit0)
        self.formLayout1.addRow(self.text1, self.lineEdit1)
        self.formLayout1.addRow(self.text2, self.lineEdit2)
        self.formLayout1.addRow(self.text3, self.lineEdit3)
        self.formLayout1.addRow(self.text4, self.lineEdit4)
        self.formLayout1.addRow(self.text5, self.lineEdit5)
        self.formLayout1.addRow(self.text6, self.lineEdit6)
        self.vlayout1.addWidget(self.button1)

        self.formLayout3 = QFormLayout()
        self.formLayout3.setVerticalSpacing(50)
        self.formLayout3.setHorizontalSpacing(20)
        self.formLayout3.addRow(self.text7, self.lineEdit7)
        self.formLayout3.addRow(self.text8, self.lineEdit8)
        self.formLayout3.addRow(self.text9, self.lineEdit9)
        self.frame3 = QFrame()
        self.frame3.setFixedWidth(370)
        self.frame3.setFixedHeight(200)
        self.frame3.setFrameShape(QFrame.Box)
        self.frame3.setLineWidth(5)
        self.frame3.setLayout(self.formLayout3)
        self.vlayout2.addWidget(self.frameLabel3)
        self.vlayout2.addWidget(self.frame3)
        self.vlayout2.addWidget(self.button2)

        self.hlayout.addLayout(self.vlayout1)
        self.hlayout.addLayout(self.vlayout2)
        self.vlayout.addLayout(self.hlayout)

        # 下面是当前结点配置的预览
        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setLineWidth(5)

        # 进行model and view 的配置
        self.vlayoutForTreeWidget = QVBoxLayout()
        self.nodesTreeWidget = NodesTreeWidget()
        self.nodesTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.nodesTreeWidget.setColumnWidth(0, 150)
        self.nodesTreeWidget.setColumnWidth(1, 150)
        self.vlayoutForTreeWidget.addWidget(self.nodesTreeWidget)

        self.frame2.setLayout(self.vlayoutForTreeWidget)
        self.vlayout.addWidget(self.frameLabel2)
        self.vlayout.addWidget(self.frame2)
        self.setLayout(self.vlayout)

    def bindFunction(self):
        self.button1.clicked.connect(self.generateConstellation)
        self.button2.clicked.connect(self.generateGroundStation)
        self.nodesTreeWidget.customContextMenuRequested.connect(self.rightMenuShowUp)

    def consParamHasNullInput(self) -> bool:
        """
        判断星座参数是否有的没有填
        :return:
        """
        self.consName = self.lineEdit0.text()
        self.orbitNum = self.lineEdit2.text()
        self.satPerOrbit = self.lineEdit3.text()
        self.inclination = self.lineEdit4.text()
        self.startingPhase = self.lineEdit5.text()
        self.altitude = self.lineEdit6.text()
        if self.consName == "" or self.orbitNum == "" or self.satPerOrbit == "" or self.inclination == "" or self.startingPhase == "" or \
                self.altitude == "":
            return True
        else:
            return False

    def groundStationParamHasNullInput(self) -> bool:
        """
        判断地面站参数是否有的没有填写
        :return:
        """
        self.groundStationName = self.lineEdit7.text()
        self.latitude = self.lineEdit8.text()
        self.longitude = self.lineEdit9.text()
        if self.groundStationName == "" or self.latitude == "" or self.longitude == "":
            return True
        else:
            return False

    def generateGroundStation(self) -> None:
        """
        点击生成地面站的时候触发的函数
        """
        if self.groundStationParamHasNullInput():
            result = QMessageBox.critical(self, 'test..', '字段不能够为空', QMessageBox.Ok)
            print(result)
        elif self.groundStationName in self.data.allGroundStationNames:
            result = QMessageBox.critical(self, 'test..', '地面站名字不能够重复', QMessageBox.Ok)
            print(self.data.allGroundStationNames)
        else:
            self.latitude = float(self.latitude)
            self.longitude = float(self.longitude)
            # 在这里我们创建我们的地面站对象并添加到我们的list之中进行存储
            groundStation = GroundStation(self.groundStationName, self.latitude, self.longitude)
            self.data.allGroundStationNames.add(self.groundStationName)
            self.addGroundStationIntoTreeWidget(self.groundStationName, self.latitude, self.longitude)
            self.data.allGroundStations.append(groundStation)

    # 与信号相互绑定的槽
    def generateConstellation(self) -> None:
        """
        点击添加星座的时候触发的函数
        """
        if self.consParamHasNullInput():
            result = QMessageBox.critical(self, 'test..', '字段不能够为空', QMessageBox.Ok)
            print(result)
        elif self.consName in self.data.allConstellationNames:
            result = QMessageBox.critical(self, 'test..', '星座名字不能够重复', QMessageBox.Ok)
            print(result)
        else:
            self.orbitNum = int(self.orbitNum)
            self.satPerOrbit = int(self.satPerOrbit)
            self.inclination = float(self.inclination)
            self.startingPhase = float(self.startingPhase)
            self.altitude = float(self.altitude)
            self.consGen = ConsGeneration(orbitNum=self.orbitNum, satPerOrbit=self.satPerOrbit,
                                          inclination=self.inclination, startingPhase=self.startingPhase,
                                          altitude=self.altitude)
            self.satellites = self.consGen.satellite_nodes_generation()
            self.addConsIntoTreeWidget(self.consName, self.satellites, len(self.data.allConstellationNames))
            # 在这里我们创建我们的星座对象并将其添加到我们的list之中进行存储
            currentCons = Constellation(self.consName, self.orbitNum, self.satPerOrbit, self.inclination,
                                        self.startingPhase, self.altitude, self.satellites)
            self.data.allConstellations.append(currentCons)
            self.data.allConstellationNames.add(self.consName)

    def rightMenuShowUp(self) -> None:
        """
        右键点击treeWidget的时候弹出的菜单
        """
        if len(self.nodesTreeWidget.selectedItems()) == 0:
            return
        self.rightClickMenu.popup(QCursor.pos())
        self.rightClickMenu.show()

    def addConsIntoTreeWidget(self, consName: str, nodes: list, index: int):
        """
        将我们的星座添加到我们的树形控件之中
        :param consName: 星座的名称
        :param nodes: 星座中的卫星结点列表
        :param index: 星座索引(当前是第几个星座)
        :return:
        """
        consRootItem = self.nodesTreeWidget.findItems("星座网络", Qt.MatchExactly, 0)[0]
        currentConsItem = QTreeWidgetItem(consRootItem)
        currentConsItem.setText(0, str(index))
        currentConsItem.setText(1, consName)
        consInfo = "轨道数量:{:d}, 每轨道卫星数量:{:d},轨道倾角:{:.2f}, 起始相位:{:.2f}, 轨道高度:{:.2f}". \
            format(self.orbitNum, self.satPerOrbit, self.inclination, self.startingPhase, self.altitude)
        currentConsItem.setText(2, consInfo)
        sat_index = 0
        for node in nodes:
            # 每次这样进行创建都是以我们传入的结点作为父结点在其内部进行子结点的创建
            item = QTreeWidgetItem(currentConsItem)
            item.setText(0, str(sat_index))  # 进行卫星的编号的设置
            item.setText(1, consName + "_SAT_" + str(node.sat_id))
            # info = "轨道序号: {:d}, 轨道平面法向量: ({:.2f}, {:.2f}, {:.2f}), 轨道内结点序号: {:d} 相位偏移:{:.2f} deg". \
            #     format(node[1], node[3][0], node[3][1], node[3][2], node[2], node[4])
            info = node.info
            item.setText(2, info)
            sat_index += 1
        self.nodesTreeWidget.expandAll()

    def addGroundStationIntoTreeWidget(self, groundStationName: str, latitude: float, longitude: float):
        """
        :param groundStationName: 地面站的名称
        :param latitude: 地面站的纬度
        :param longitude: 地面站的经度
        :return:
        """
        # 首先寻找到我们的根结点
        groundStationRootItem = self.nodesTreeWidget.findItems("地面结点", Qt.MatchExactly, 0)[0]
        # 以根结点作为父结点创建我们的地面站结点
        currentGroundStationItem = QTreeWidgetItem(groundStationRootItem)
        # 设置当前是第几个地面站
        currentGroundStationItem.setText(0, str(len(self.data.allGroundStations)))
        # 设置地面站的名称
        currentGroundStationItem.setText(1, groundStationName)
        # 设置地面站的信息
        info = "纬度:{:.2f}, 经度:{:.2f}".format(latitude, longitude)
        currentGroundStationItem.setText(2, info)
