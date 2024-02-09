from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.直接打开登录页面
driver.get("http://novel.hctestedu.com/user/login.html")
# 3.输入手机号
driver.find_elements(By.TAG_NAME, "input")[1].send_keys("15142113182")
# 4.输入密码
driver.find_elements(By.TAG_NAME, "input")[2].send_keys("zxp3033705358")
# 5.点击下次自动登录
driver.find_elements(By.TAG_NAME, "input")[3].click()
# 6.点击登录
driver.find_elements(By.TAG_NAME, "input")[4].click()
sleep(5)
