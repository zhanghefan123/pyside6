class Constellation:
    def __init__(self, consName: str, orbitNum: int, satPerOrbit: int, inclination: float, startingPhase: float,
                 altitude: float):
        self.consName = consName
        self.orbitNum = orbitNum
        self.satPerOrbit = satPerOrbit
        self.inclination = inclination
        self.startingPhase = startingPhase
        self.altitude = altitude
