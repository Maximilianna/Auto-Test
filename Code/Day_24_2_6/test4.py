from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.保存按钮位置
a = driver.find_element(By.CLASS_NAME, "mr15")
# 4.右击按钮
ActionChains(driver).context_click(a).perform()
sleep(5)
# 5.双击按钮
ActionChains(driver).double_click(a).perform()
sleep(5)
