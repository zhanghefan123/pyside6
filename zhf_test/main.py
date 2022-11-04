# 核心导入
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pages.NodeSettingPage import NodeSetting
from pages.ConnectionSettingPage import ConnectionSettings
from pages.ApplicationSettingPage import ApplicationSettings
from zhf_test.pojo.Data import Data


class IntegratedSatelliteTerrestrialNetwork(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializePublicData()
        self.initializeComponents()
        self.layOutSetting()
        self.bindFunctions()
        self.currentIndex = 0

    def initializePublicData(self):
        self.data = Data()

    def initializeComponents(self):
        self.setWindowTitle("Integrated Satellite Terrestrial Network")
        self.resize(900, 600)
        self.tabWidget = QTabWidget()
        self.tabWidget.setFixedWidth(800)
        self.tabWidget.setFixedHeight(600)
        self.nodeSettingWidget = NodeSetting(self.data)
        self.connectionSettingsWidget = ConnectionSettings(self.data)
        self.applicationSettingsWidget = ApplicationSettings(self.data)
        self.tabWidget.addTab(self.nodeSettingWidget, "结点设置")
        self.tabWidget.addTab(self.connectionSettingsWidget, "连接设置")
        self.tabWidget.addTab(self.applicationSettingsWidget, "应用设置")
        self.nodeSettingWidget.setEnabled(True)
        self.connectionSettingsWidget.setEnabled(False)
        self.applicationSettingsWidget.setEnabled(False)
        # 初始情况下三个tab是否可以进行点击
        self.tabWidget.setTabEnabled(0, True)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.nextStepButton = QPushButton('下一步')
        self.lastStepButton = QPushButton('上一步')

    def layOutSetting(self) -> None:
        """
        布局设置
        """
        # 如果我们希望我们的布局是有边框的我们应该将其放在QFrame之中
        self.totalLayout = QVBoxLayout()
        self.hlayout1Frame = QFrame()
        self.hlayout1Frame.setFrameShape(QFrame.Box)
        self.hlayout1Frame.setLineWidth(5)
        self.hlayout1 = QHBoxLayout()
        self.hlayout1.addWidget(self.tabWidget)
        self.hlayout1Frame.setLayout(self.hlayout1)
        self.totalLayout.addWidget(self.hlayout1Frame)
        self.hlayout2Frame = QFrame()
        self.hlayout2Frame.setFrameShape(QFrame.Box)
        self.hlayout2Frame.setLineWidth(5)
        self.hlayout2 = QHBoxLayout()
        self.hlayout2.addWidget(self.lastStepButton)
        self.hlayout2.addWidget(self.nextStepButton)
        self.hlayout2Frame.setLayout(self.hlayout2)
        self.totalLayout.addWidget(self.hlayout2Frame)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.totalLayout)
        self.setCentralWidget(self.central_widget)

    def bindFunctions(self) -> None:
        """
        绑定事件
        """
        self.nextStepButton.clicked.connect(self.nextStep)
        self.lastStepButton.clicked.connect(self.lastStep)

    def nextStep(self) -> None:
        """
        点击下一步按钮触发的事件,并且检查该有的东西是否进行了配置
        """
        # 检查是否有项目名称
        project_name = self.nodeSettingWidget.lineEditProjectName.text()
        has_cons = True if len(self.data.allConstellationNames) > 0 else False
        error_message = ""
        if project_name == "":
            error_message += "项目名称不能为空 "
        if not has_cons:
            error_message += "至少需要一个星座 "
        if error_message != "":
            QMessageBox.critical(self, 'test..', error_message, QMessageBox.Ok)
            return
        if self.currentIndex < 3:
            self.currentIndex += 1
        else:
            pass
        self.tabWidget.setCurrentIndex(self.currentIndex)
        self.changeTabEnabled(self.currentIndex)

    def lastStep(self) -> None:
        """
        点击上一步按钮触发的事件
        """
        if self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            pass
        self.tabWidget.setCurrentIndex(self.currentIndex)
        self.changeTabEnabled(self.currentIndex)

    def changeTabEnabled(self, currentIndex) -> None:
        """
        根据
        :param currentIndex: 当前位于哪一个索引的位置处
        """
        if currentIndex == 0:
            self.tabWidget.setTabEnabled(0, True)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
        elif currentIndex == 1:
            self.tabWidget.setTabEnabled(0, True)
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, False)
        else:
            self.tabWidget.setTabEnabled(0, True)
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, True)


# 启动方法
if __name__ == '__main__':
    app = QApplication()
    # 这里输入的路径是从main.py所在的位置开始的
    app.setWindowIcon(QIcon('./icons/satellite.png'))
    mainWindow = IntegratedSatelliteTerrestrialNetwork()
    mainWindow.show()

    sys.exit(app.exec())
