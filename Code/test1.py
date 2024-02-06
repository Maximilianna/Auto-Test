from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取Chrome浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进入登录页
driver.find_element(By.CLASS_NAME, "mr15").click()
# 4.输入手机号
driver.find_element(By.NAME, "txtUName").send_keys("15142113182")
# 5.输入密码
driver.find_element(By.NAME, "txtPassword").send_keys("zxp3033705358")
# 6.点击下次自动登录
driver.find_element(By.ID, "autoLogin").click()
# 7.登录
driver.find_element(By.CLASS_NAME, "btn_red").click()
sleep(3)
# 8.点击书名
driver.find_element(By.LINK_TEXT, "开局得到如来舍利").click()
# 9.开始阅读
driver.find_element(By.CLASS_NAME, "btn_ora").click()
sleep(3)
