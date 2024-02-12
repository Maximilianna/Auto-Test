# CSV文件读取
import csv

def readcsv():
    # 打开文件
    strean = open(r"..\..\Text\testData.csv")
    # 读取文件内容
    reader = csv.reader(strean)
    # 新建一个空列表，用于保存数据
    list = []
    # 使用for循环遍历文件，将文件数据保存到列表
    for row in reader:
        list.append(row)
    return list
# 判断我们当前文件是否不被引用
# 如果不被引用，则执行一下代码
if __name__ == "__main__":
    data = readcsv()
    for row in data:
        print(row)