# 时间等待操作
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进行智能等待
driver.implicitly_wait(3)
# 4.点击登录按钮
driver.find_element(By.CLASS_NAME, "mr15").click()
sleep(5)
