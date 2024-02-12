# 数据驱动
from selenium import webdriver
from selenium.webdriver.common.by import By
import ddt
import unittest
from test15 import readcsv
from time import sleep

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
    stream_info = readcsv()

    @ddt.data(*stream_info)
    def test_denglu(self, list):
        # 在输入框输入文件中的数据
        self.driver.find_element(By.NAME, "searchKey").send_keys(list[0])
        # 点击查询按钮
        self.driver.find_element(By.CLASS_NAME, "search_btn").click()
        sleep(2)
