class Satellite:
    def __init__(self, sat_id: int, orbit_id: int, sat_id_in_orbit: int, orbit_normal: list, starting_phase: float,
                 altitude: float, sat_name: str):
        self.sat_name = sat_name
        self.sat_id = sat_id
        self.orbit_id = orbit_id
        self.sat_id_in_orbit = sat_id_in_orbit
        self.orbit_normal = orbit_normal
        self.starting_phase = starting_phase
        self.altitude = altitude
        self.info = ""
        self.ethNum = -1
        self.generateInfo()

    def generateInfo(self):
        self.info = "轨道序号: {:d}, 轨道平面法向量: ({:.2f}, {:.2f}, {:.2f}), 轨道内结点序号: {:d} 相位偏移:{:.2f} deg". \
            format(self.orbit_id, self.orbit_normal[0], self.orbit_normal[1], self.orbit_normal[2],
                   self.sat_id_in_orbit, self.starting_phase)
