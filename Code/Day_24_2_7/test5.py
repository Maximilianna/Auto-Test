# 键盘操作
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.往输入框中输入内容
driver.find_element(By.CLASS_NAME, "s_int").send_keys("开局获得")
# 4.全选输入框中内容
driver.find_element(By.CLASS_NAME, "s_int").send_keys(Keys.CONTROL, "a")
# 5.剪切输入框中内容
driver.find_element(By.CLASS_NAME, "s_int").send_keys(Keys.CONTROL, "x")
# 6.往输入框中粘贴内容
driver.find_element(By.CLASS_NAME, "s_int").send_keys(Keys.CONTROL, "v")
driver.find_element(By.CLASS_NAME, "s_int").send_keys(Keys.CONTROL, "v")
sleep(5)
