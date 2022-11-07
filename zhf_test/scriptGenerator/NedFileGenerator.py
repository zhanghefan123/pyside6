from ..scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import PreImportOfNedFile, networkOfNedFile, \
    ParametersAndTypesOfNedFile, NecessarySubmodules, TAB, ENTER_AND_TAB, \
    SATELLITE_TYPE, GROUND_STATION_TYPE, ENTER, LINK_TYPE_SATELLITE_TO_SATELLITE, LINK_TYPE_SATELLITE_TO_GROUNDSTATION
import os


class NedFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        final_str = ""
        final_str += PreImportOfNedFile
        final_str += networkOfNedFile
        final_str += ParametersAndTypesOfNedFile
        final_str += NecessarySubmodules
        # 在这里我们需要遍历所有的卫星结点以及所有的地面结点
        for satellite in self.data.allConstellations[0].nodes:
            final_str += \
                """
        {}: {} {{
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[{}];
        }}""".format(satellite.sat_name, SATELLITE_TYPE, satellite.ethNum + 1)
        for groundStation in self.data.allGroundStations:
            final_str += \
                """
        {}: {} {{
            parameters:
                hasOspf = false;
            gates:
                ethg[{}];
        }}""".format(groundStation.groundStationName, GROUND_STATION_TYPE, groundStation.ethNum + 1)
        final_str += ENTER
        final_str += TAB + "connections:" + ENTER
        # 遍历所有的我们的links
        for link in self.data.allLinks.linkSet:
            if link.linkType == LINK_TYPE_SATELLITE_TO_SATELLITE:
                src_node_name = link.srcNode.sat_name
                src_eth_num = link.node1EthNum
                dest_node_name = link.destNode.sat_name
                dest_eth_num = link.node2EthNum
                final_str += TAB + TAB + \
                             f"{src_node_name}.ethg[{src_eth_num}] <--> {dest_node_name}.ethg[{dest_eth_num}]"
                final_str += ENTER
            elif link.linkType == LINK_TYPE_SATELLITE_TO_GROUNDSTATION:
                src_node_name = link.srcNode.sat_name
                src_eth_num = link.node1EthNum
                dest_node_name = link.destNode.groundStationName
                dest_eth_num = link.node2EthNum
                final_str += TAB + TAB + \
                             f"{src_node_name}.ethg[{src_eth_num}] <--> {dest_node_name}.ethg[{dest_eth_num}]"
                final_str += ENTER
        final_str += "}"
        return final_str

    def writeIntoConfigFile(self, generate_file_path=""):
        generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "OsgEarthNet.ned"
        super(NedFileGenerator, self).writeIntoConfigFile(generate_file_path)
