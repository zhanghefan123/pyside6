from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from zhf_test.pojo.Client import Client
from zhf_test.pojo.Server import Server


class ApplicationSettingWidget(QTableWidget):
    def __init__(self, row=0, column=4):
        super(ApplicationSettingWidget, self).__init__(row, column)
        self.setHorizontalHeaderLabels(["功能", "服务器/客户端", "结点名称", "目的结点"])
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 300)
        self.setColumnWidth(2, 150)
        self.setColumnWidth(3, 150)


class ApplicationSettings(QWidget):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.initializeComponents()
        self.layoutSetting()
        self.bindFunctions()

    def initializeComponents(self) -> None:
        """
        初始化组件
        """
        self.label1 = QLabel('应用层服务器-客户端配置预览')
        self.applicationSettingWidget = ApplicationSettingWidget()
        self.label2 = QLabel('服务器结点')
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("请输入服务器结点名称")
        self.button1 = QPushButton("添加")
        self.label3 = QLabel('客户端结点')
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("请输入客户端结点名称")
        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setPlaceholderText("请输入目的结点的名称")
        self.button2 = QPushButton("添加")

    def layoutSetting(self) -> None:
        """
        布局设置
        """
        # -------总体的布局---------
        self.vlayout = QVBoxLayout()
        # -------------应用层服务器-客户端对的配置预览-----------
        self.vlayout.addWidget(self.label1)
        self.vlayout.addWidget(self.applicationSettingWidget)
        self.setLayout(self.vlayout)
        # --------水平布局1-进行按钮的放置---------
        self.hlayout1 = QHBoxLayout()
        self.hlayout1.addWidget(self.label2)
        self.hlayout1.addWidget(self.lineEdit1)
        self.hlayout1.addWidget(self.button1)
        self.vlayout.addLayout(self.hlayout1)
        # --------水平布局2-进行按钮的放置---------
        self.hlayout2 = QHBoxLayout()
        self.hlayout2.addWidget(self.label3)
        self.hlayout2.addWidget(self.lineEdit2)
        self.hlayout2.addWidget(self.lineEdit3)
        self.hlayout2.addWidget(self.button2)
        self.vlayout.addLayout(self.hlayout2)

    def bindFunctions(self):
        """
        绑定函数
        :return:
        """
        self.button1.clicked.connect(self.addServer)
        self.button2.clicked.connect(self.addClient)

    def serverHasNullInput(self):
        """
        判断服务器的输入是否为空
        """
        if self.lineEdit1.text() == "":
            return True
        else:
            return False

    def clientHasNullInput(self):
        """
        判断客户端的输入是否为空
        """
        if self.lineEdit2.text() == "" or self.lineEdit3.text() == "":
            return True
        else:
            return False

    def addServer(self):
        """
        添加服务器
        """
        # 首先进行获取
        server_name = self.lineEdit1.text()
        # 判断是已经存在同名的server
        if server_name == "":
            QMessageBox.critical(self, "提示", "服务器名称不能为空")
            return
        elif server_name in self.data.serverList:
            QMessageBox.critical(self, "提示", "已经存在同名的服务器")
            return
        # 首先进行server的创建
        server_function = ""
        server = Server(server_name, server_function)
        self.data.serverList.append(server)

    def addClient(self):
        """
        添加客户端
        """
        # 首先进行获取
        client_name = self.lineEdit2.text()
        client_destination_server = self.lineEdit3.text()
        # 判断是否已经出现过了client
        if client_name == "" or client_destination_server == "":
            QMessageBox.critical(self, "提示", "客户端以及目的结点不能为空")
            return
        elif client_name not in self.data.allconstellations[0][6]:
            QMessageBox.critical(self, "提示", "结点不存在")
            return
        elif client_name in self.data.clientList:
            QMessageBox.critical(self, "提示", "客户端已经存在")
            return
        elif client_destination_server not in self.data.serverList:
            QMessageBox.critical(self, "提示", "目的结点不是服务器")
            return
        # 首先进行client的创建
        client = Client(client_name, client_destination_server)
        self.data.clientList.append(client)
        self.data.clientNames.add(client_name)

    def updateServerList(self):
        """
        更新服务器列表
        """
        self.applicationSettingWidget.clearContents()
        row_count = len(self.data.serverList) + len(self.data.clientList)
        self.applicationSettingWidget.setRowCount(row_count)
        index = 0
        for server in self.data.serverList:
            self.applicationSettingWidget.setItem(index, 0, QTableWidgetItem(str(index)))
            self.applicationSettingWidget.setItem(index, 1, QTableWidgetItem("服务器"))
            self.applicationSettingWidget.setItem(index, 2, QTableWidgetItem(server.name))
            index += 1
        for client in self.data.clientList:
            self.applicationSettingWidget.setItem(index, 0, QTableWidgetItem(str(index)))
            self.applicationSettingWidget.setItem(index, 1, QTableWidgetItem("客户端"))
            self.applicationSettingWidget.setItem(index, 2, QTableWidgetItem(client.name))
            self.applicationSettingWidget.setItem(index, 3, QTableWidgetItem(client.object_dest_server_name))
            index += 1
