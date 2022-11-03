# 核心导入
import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pages.NodeSettingPage import NodeSetting
from pages.ConnectionSettingPage import ConnectionSettings
from pages.ApplicationSettingPage import ApplicationSettings


class IntegratedSatelliteTerrestrialNetwork(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeComponents()
        self.layOutSetting()
        self.bindFunctions()
        self.currentIndex = 0

    def initializeComponents(self):
        self.setWindowTitle("Integrated Satellite Terrestrial Network")
        self.resize(900, 600)
        self.tabWidget = QTabWidget()
        self.tabWidget.setFixedWidth(800)
        self.tabWidget.setFixedHeight(500)
        self.nodeSettingWidget = NodeSetting()
        self.connectionSettingsWidget = ConnectionSettings()
        self.applicationSettingsWidget = ApplicationSettings()
        self.tabWidget.addTab(self.nodeSettingWidget, "结点设置")
        self.tabWidget.addTab(self.connectionSettingsWidget, "连接设置")
        self.tabWidget.addTab(self.applicationSettingsWidget, "应用设置")
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
        点击下一步按钮触发的事件
        """
        if self.currentIndex < 3:
            self.currentIndex += 1
        else:
            pass
        self.tabWidget.setCurrentIndex(self.currentIndex)

    def lastStep(self) -> None:
        """
        点击上一步按钮触发的事件
        """
        if self.currentIndex > 0:
            self.currentIndex -= 1
        else:
            pass
        self.tabWidget.setCurrentIndex(self.currentIndex)


# 启动方法
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = IntegratedSatelliteTerrestrialNetwork()
    mainWindow.show()
    sys.exit(app.exec())
