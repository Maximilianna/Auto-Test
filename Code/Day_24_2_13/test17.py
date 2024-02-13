# 数据断言
import csv
import unittest

import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By


def read_file():
    # 打开文件
    stream = open(r"../../Text/test.csv")
    # 读取文件内容
    reader = csv.reader(stream)
    # 新建一个空列表，用于保存数据
    list = []
    # 使用for循环遍历文件，将文件数据保存到列表
    for row in reader:
        list.append(row)
    return list


@ddt.ddt
# 创建测试类
class denglu(unittest.TestCase):
    # 在所有测试方法前执行
    def setUp(self):
        # 获取浏览器驱动
        self.driver = webdriver.Chrome()
        # 打开网页
        self.driver.get("http://novel.hctestedu.com/")
        # 进行智能等待
        self.driver.implicitly_wait(20)

    # 在所有测试方法后执行
    def tearDown(self):
        # 关闭网页
        self.driver.quit()

    # 去读取文件数据
    stream = read_file()

    @ddt.data(stream)
    def test_denglu(self, list):
        try:
            # 进入登录页
            self.driver.find_element(By.CLASS_NAME, "mr15").click()
            # 输入手机号
            self.driver.find_elements(By.TAG_NAME, "input")[1].send_keys(list[0])
            # 输入密码
            self.driver.find_elements(By.TAG_NAME, "input")[2].send_keys(list[1])
            # 点击登录按钮
            self.driver.find_elements(By.TAG_NAME, "input")[4].click()
            # 获取提示信息位置
            s = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/form/ul/li[1]/span").text
            # 打印提示信息
            print(s)
            # 断言
            self.assertEqual(s, list[2][0])
            print("用例执行成功")
        except:
            # 截图
            self.driver.get_screenshot_as_file(r"C:\Users\zxpaz\Desktop\jietu.png")
            print("用例执行失败")
