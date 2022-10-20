import os


class GetFile:
    def __init__(self, base_path):
        self.path = base_path

    def get_all_files(self):
        if os.path.exists(self.path):
            for root, folders, files in os.walk(self.path):
                for file in files:
                    # print(os.path.join(self.path, name))
                    print(file)

                    # 查看文件的修改时间
                    file_info = os.stat(os.path.join(self.path, file))
                    print(file_info.st_ctime)
            pass

        else:
            print("请输入合法的目录")




