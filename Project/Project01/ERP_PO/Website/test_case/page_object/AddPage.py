import time

from ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class AddPage(BasePage):
    a_text = [By.LINK_TEXT, "商品品牌"]
    xin = [By.XPATH, "/html/body/div/div/div[2]/section/div/div[2]/div[3]"]
    name = [By.XPATH, "/html/body/div[2]/div/div[2]/form/div/div/div/div/input"]
    bao = [By.CSS_SELECTOR,
           "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium"]

    # 点击商品品牌按钮
    def type_a(self):
        self.click_element(self.a_text[0], self.a_text[1])

    # 点击新增按钮
    def type_xin(self):
        self.click_element(self.xin[0], self.xin[1])

    # 输入商品名
    def type_name(self, name):
        self.input_element(self.name[0], self.name[1], name)

    # 点击保存按钮
    def type_bao(self):
        self.click_element(self.bao[0], self.bao[1])


def add(driver, name, value):
    add_page = AddPage(driver)
    time.sleep(2)
    add_page.type_a()
    time.sleep(2)
    add_page.type_xin()
    time.sleep(2)
    add_page.type_name(name)
    add_page.type_bao()
    time.sleep(2)
    if value == "新增成功":
        text = add_page.find_element(By.XPATH,"/html/body/div[3]/p").text
        add_page.click_element(By.XPATH, "/html/body/div[3]/i[2]")
    elif value == "商品品牌名称重复，请重新输入。":
        text = add_page.find_element(By.XPATH, "/html/body/div[3]/p").text
        add_page.click_element(By.XPATH, "/html/body/div[3]/i[2]")
    else:
        text = add_page.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/form/div/div/div[2]").text
    return text
