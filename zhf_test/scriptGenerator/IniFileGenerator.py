from ..scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import IniFilePre, ENTER


class IniFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        final_str = ""
        final_str += IniFilePre
        # 遍历所有的地面站
        for ground_station in self.data.allGroundStations:
            final_str += f"OsgEarthNet.{ground_station.groundStationName}.mobility.latitude = {ground_station.latitude}"
            final_str += ENTER
            final_str += f"OsgEarthNet.{ground_station.groundStationName}.mobility.latitude = {ground_station.latitude}"
            final_str += ENTER
        # 遍历所有的卫星
        for satellite in self.data.allConstellations[0].nodes:
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.orbitNormal = '{satellite.orbit_normal}'"
            final_str += ENTER
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.startingPhase = '{satellite.starting_phase}'"
            final_str += ENTER
            final_str += f"OsgEarthNet.{satellite.sat_name}.mobility.altitude = {satellite.altitude}km"
        return final_str

    def writeIntoConfigFile(self, generate_file_path):
        generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "omnetpp.ini"
        super(IniFileGenerator, self).writeIntoConfigFile(generate_file_path)
