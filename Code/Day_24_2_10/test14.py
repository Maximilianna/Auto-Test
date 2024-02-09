# Unittest自动化测试框架
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

# 创建测试类
class Denglu(unittest.TestCase):
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
        # 输入手机号
        self.driver.find_elements(By.TAG_NAME, "input")[1].send_keys("15142113182")
        # 输入密码
        self.driver.find_elements(By.TAG_NAME, "input")[2].send_keys("zxp3033705358")
        # 点击下次自动登录
        self.driver.find_elements(By.TAG_NAME, "input")[3].click()
        # 点击登录按钮
        self.driver.find_elements(By.TAG_NAME, "input")[4].click()
        sleep(5)
    def test_denglu1(self):
        # 进入登录页
        self.driver.find_element(By.CLASS_NAME,"mr15").click()
    def test_denglu2(self):
        # 点击作家专区按钮
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/ul/li[5]/a").click()
        # 切换页面
        self.driver.switch_to.window(self.driver.window_handles[1])