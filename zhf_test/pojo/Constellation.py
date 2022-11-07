class Constellation:
    def __init__(self, consName: str, orbitNum: int, satPerOrbit: int, inclination: float, startingPhase: float,
                 altitude: float, nodes: list):
        """
        :param consName: 星座名称
        :param orbitNum: 轨道数量
        :param satPerOrbit: 每根轨道的卫星数量
        :param inclination: 轨道倾角
        :param startingPhase: 初始相位
        :param altitude: 高度
        :param nodes: 结点列表
        """
        self.consName = consName
        self.orbitNum = orbitNum
        self.satPerOrbit = satPerOrbit
        self.inclination = inclination
        self.startingPhase = startingPhase
        self.altitude = altitude
        self.nodes = nodes
        self.satelliteNames = set()
        self.generateSatelliteNames()

    def generateSatelliteNames(self):
        for satellite in self.nodes:
            self.satelliteNames.add(self.consName + "_SAT_" + str(satellite.sat_id))
