class GroundStation:
    def __init__(self,groundStationId, groundStationName: str, latitude: float, longitude: float):
        """
        :param groundStationName: 地面站名称
        :param latitude: 纬度
        :param longitude: 经度
        """
        self.groundStationId = groundStationId
        self.groundStationName = groundStationName
        self.latitude = latitude
        self.longitude = longitude
        self.ethNum = -1
