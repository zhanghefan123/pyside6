from ..scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import OSPFConfigPre, OSPFConfigEnd, ENTER, ENTER_AND_TAB, TAB


class OspfConfigFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        final_str = ""
        final_str += OSPFConfigPre
        for satellite in self.data.allConstellations[0].nodes:
            final_str += TAB
            final_str += f"""<Router name="{satellite.sat_name}" RFC1583Compatible="true">""" + ENTER_AND_TAB + TAB
            for index in range(satellite.ethNum + 1):
                final_str += \
                    f"""<PointToPointInterface ifName="eth{index}" areaID="0.0.0.0" interfaceOutputCost="1"/>"""
                if index == satellite.ethNum:
                    final_str += ENTER_AND_TAB
                else:
                    final_str += ENTER_AND_TAB + TAB
            final_str += "</Router>" + ENTER
        final_str += OSPFConfigEnd
        return final_str

    def writeIntoConfigFile(self, generate_file_path=""):
        generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "ospf_config.xml"
        super(OspfConfigFileGenerator, self).writeIntoConfigFile(generate_file_path)
