# 下拉框操作
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("https://layui.dev/docs/2/form/select.html#search")
# 3.进行智能等待
driver.implicitly_wait(20)
# 4.定位下拉框
sss = driver.find_elements(By.TAG_NAME,"select")[0]
# 5.选择下拉框选项
Select(sss).select_by_index(0)
sleep(3)