# 下拉滚动条
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("http://novel.hctestedu.com/")
# 3.进行智能等待
driver.implicitly_wait(20)
# 4.进入登录页
driver.find_element(By.CLASS_NAME,"mr15").click()
# 5.向下拖动滚动条-通过鼠标和键盘操作
#ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
# 5.向下拖动滚动条-通过注入script语句
driver.execute_script("window.scrollTo(0,100)")
# 6.点击网站首页
#driver.find_element(By.XPATH,"/html/body/div[3]/div/div/ul/li[1]/a[2]").click()
sleep(3)