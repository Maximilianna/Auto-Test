from selenium import webdriver


# 获取浏览器驱动
def Driver():
    driver = webdriver.Chrome()
    return driver
