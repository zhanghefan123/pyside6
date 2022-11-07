from zhf_test.pojo.LinkSet import LinkSet


class Data:
    """
    一个公共的数据集用来在三个tabWidget之间传递数据
    """

    def __init__(self):
        # 用来存储我们的项目名称
        self.projectName = ""
        # 用来存储所有我们创建的星座
        self.allConstellations = []
        # 用来存储所有我们创建的地面站
        self.allGroundStations = []
        # 用来存储所有我们创建的地面站的名称
        self.allGroundStationNames = set()
        # 用来存储所有我们创建的星座的名称
        self.allConstellationNames = set()
        # 用来存储所有我们创建的链路
        self.allLinks = LinkSet()
        # 用来存储所有的服务器列表
        self.serverList = []
        # 用来存储所有的客户端列表
        self.clientList = []
        # 用来存储所有的服务器的名称
        self.serverNames = set()
        # 用来存储所有的客户端的名称
        self.clientNames = set()
