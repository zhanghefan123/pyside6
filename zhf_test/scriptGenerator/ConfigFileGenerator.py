import os


class ConfigFileGenerator:
    def generate(self):
        return ""

    def writeIntoConfigFile(self, generate_file_path):
        # 首先进行逐个级别的目录的递归的生成
        dir_path = os.path.dirname(generate_file_path)
        os.makedirs(dir_path, exist_ok=True)
        # 当前的相对路径如下 /Users/huangaoan/Desktop/zhf projects/pythonGUITutorial/zhf_test
        try:
            with open(generate_file_path, "w") as f:
                f.write(self.generate())
        except FileNotFoundError as e:
            print(e)
