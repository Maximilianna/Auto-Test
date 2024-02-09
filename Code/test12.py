# 截图操作
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进行智能等待
driver.implicitly_wait(20)
# 4.进行截图
driver.get_screenshot_as_file(r"C:\Users\zxpaz\Desktop\jietu.png")