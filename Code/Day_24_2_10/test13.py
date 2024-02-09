# alert弹出框处理
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://192.168.9.3:10002")
# 3.网页全屏
driver.maximize_window()
# 4.输入用户名
driver.find_element(By.NAME,'username').send_keys("XTGLY")
# 5.输入密码
driver.find_element(By.CLASS_NAME,'password').send_keys("123456")
# 6.点击登录按钮
driver.find_element(By.ID,"signIn").click()
sleep(3)
# 7.点击仓库信息
driver.find_element(By.LINK_TEXT,'仓库信息').click()
sleep(3)
# 8.点击禁用按钮
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[9]/div/button[2]').click()
# 9.确定禁用
driver.switch_to.alert.accept()
