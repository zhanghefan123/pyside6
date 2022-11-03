import math


class ConsGeneration:
    """
    星座类型的生成
    """

    def __init__(self):
        self.orbitNum = 0
        self.satPerOrbit = 0
        self.inclination = 0
        self.startingPhase = 0
        self.altitude = 0

    def __init__(self, orbitNum: int, satPerOrbit: int, inclination: float, startingPhase: float, altitude: float):
        """
        :param orbitNum 轨道数量
        :param satPerOrbit 每根轨道的卫星的数量
        :param inclination 轨道倾斜角度
        """
        self.orbitNum = orbitNum
        self.satPerOrbit = satPerOrbit
        self.inclination = inclination
        self.startingPhase = startingPhase
        self.altitude = altitude
        # 将要生成的结点的列表
        self.nodes = []

    def satellite_nodes_generation(self):
        """
        进行卫星网络的生成
        :return: satList
        """
        sat_list = []
        total_angle = 180
        # 进行每一根轨道的遍历
        for orbitId in range(0, self.orbitNum):
            # 进行轨道内的每一颗卫星的遍历
            for satId in range(self.satPerOrbit * orbitId, self.satPerOrbit * (orbitId + 1)):
                # 轨道三范数的计算
                orbit_normal = [round(math.cos(orbitId * (total_angle / self.orbitNum) * math.pi / 180), 4),
                                round(math.sin(orbitId * (total_angle / self.orbitNum) * math.pi / 180), 4),
                                round(math.cos(self.inclination * math.pi / 180), 4)
                                ]
                # 如果当前的轨道id为偶数
                if orbitId & 1 == 0:
                    starting_phase = round((satId - self.satPerOrbit * orbitId) * (360 / self.satPerOrbit), 4)
                else:
                    starting_phase = round((satId - self.satPerOrbit * orbitId + 0.5) * (360 / self.satPerOrbit), 4)

                if orbitId * (total_angle / self.orbitNum) >= 90:
                    starting_phase += 180
                    starting_phase %= 360

                # sat[0] 是卫星的编号, sat[1] 轨道编号, sat[2]是轨道内卫星的编号
                # sat[3]三范数,sat[4]出始相位,sat[5]卫星的高度
                sat = [satId, orbitId, satId - self.satPerOrbit * orbitId, orbit_normal,
                       starting_phase, self.altitude]

                # 将sat放到satList之中
                sat_list.append(sat)
        return sat_list


if __name__ == "__main__":
    consGen = ConsGeneration(6, 11, 90, 0, 780)
    for item in consGen.satellite_nodes_generation():
        print(item)

