# 元素属性删除
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进行智能等待
driver.implicitly_wait(10)
# 4.点击登录按钮
driver.find_element(By.CLASS_NAME, "mr15").click()
# 5.输入手机号
driver.find_elements(By.TAG_NAME, "input")[1].send_keys("15142113182")
# 6.输入密码
driver.find_elements(By.TAG_NAME, "input")[2].send_keys("zxp3033705358")
# 7.点击登录
driver.find_elements(By.TAG_NAME, "input")[4].click()
# 8.定位作家专区按钮
sleep(1)
a = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/ul/li[5]/a")
# 9.删除target标签
driver.execute_script("arguments[0].removeAttribute('target')", a)
# 10.点击作家专区按钮
a.click()
sleep(5)
