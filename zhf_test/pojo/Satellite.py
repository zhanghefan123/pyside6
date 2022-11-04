# sat[0] 是卫星的编号, sat[1] 轨道编号, sat[2]是轨道内卫星的编号
# sat[3]三范数,sat[4]初始相位,sat[5]卫星的高度
class Satellite:
    def __init__(self, sat_id: int, orbit_id: int, sat_id_in_orbit: int, orbit_normal: list, starting_phase: float,
                 altitude: float):
        self.sat_id = sat_id
        self.orbit_id = orbit_id
        self.sat_id_in_orbit = sat_id_in_orbit
        self.orbit_normal = orbit_normal
        self.starting_phase = starting_phase
        self.altitude = altitude
        self.info = ""
        self.generateInfo()

    def generateInfo(self):
        self.info = "轨道序号: {:d}, 轨道平面法向量: ({:.2f}, {:.2f}, {:.2f}), 轨道内结点序号: {:d} 相位偏移:{:.2f} deg". \
            format(self.orbit_id, self.orbit_normal[0], self.orbit_normal[1], self.orbit_normal[2],
                   self.sat_id_in_orbit, self.starting_phase)
