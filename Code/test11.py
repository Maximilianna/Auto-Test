# 上传文件
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1.获取浏览器驱动
driver = webdriver.Chrome()
# 2.打开网页
driver.get("https://layui.dev/2.7/demo/upload.html")
# 3.进行智能等待
driver.implicitly_wait(20)
# 4.上传图片
driver.find_element(By.CLASS_NAME,"layui-upload-file").send_keys(r"C:\Users\zxpaz\Pictures\jj_5.jpg")
sleep(5)