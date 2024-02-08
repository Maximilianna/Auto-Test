# 切换窗口
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进行智能等待
driver.implicitly_wait(20)
# 4.点击作家专区
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/ul/li[5]/a").click()
# 5.切换页面
driver.switch_to.window(driver.window_handles[1])
# 6.进行智能等待
driver.implicitly_wait(20)
# 7.输入手机号
driver.find_elements(By.TAG_NAME,"input")[1].send_keys("15142113182")
# 8.输入密码
driver.find_elements(By.TAG_NAME,"input")[2].send_keys("zxp3033705358")
# 9.点击登录按钮
driver.find_elements(By.TAG_NAME,"input")[4].click()
sleep(3)