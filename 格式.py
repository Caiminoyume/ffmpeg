import ffmpy3
import os


class geshi:
    def __init__(self, infile):
        if '& ' in infile:  # 解决包含空格的文件路径出现的错误
            infile = infile[3:-1]
        if os.path.exists(infile) == False:  # 判断文件是否存在
            print('文件打开失败')
        self.infile = infile

    def getname(self):
        return os.path.splitext()[0]

    def getext(self):
        return os.path.splitext(self.infile)[1]

    def getpath(self):
        return os.path.dirname(self.infile)+'\\'

    def __str__(self):
        return os.path.basename(self.infile)


def main():
    inp = input("请将文件拖入窗口：")
    ins = geshi(inp)
    print(ins)
    print(ins.getname())
    print(ins.getpath())
    print(ins.getext())
    pass


if __name__ == '__main__':
    main()
