import time

from ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class AddPage(BasePage):
    input_link = [By.PARTIAL_LINK_TEXT, "分类"]
    input_new = [By.CSS_SELECTOR, "#app > div > div.main-container.hasTagsView > section > div > div.mb8.el-row > div:nth-child(3) > button"]
    input_name = [By.XPATH, "/html/body/div[2]/div/div[2]/form/div/div/div/div/input"]
    input_button = [By.CSS_SELECTOR, "body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium"]

    def type_link(self):
        self.click_element(self.input_link[0],self.input_link[1])

    def type_new(self):
        self.click_element(self.input_new[0],self.input_new[1])

    def type_name(self,name):
        self.input_element(self.input_name[0],self.input_name[1],name)

    def type_button(self):
        self.click_element(self.input_button[0],self.input_button[1])

    def get_prompt_test(self,value):
        if value == "新增成功":
            return self.find_element(By.XPATH,"/html/body/div[3]/p").text
        else:
            return self.find_element(By.CLASS_NAME,"el-form-item__error").text

def add(driver,name,value):
    add_page = AddPage(driver)
    time.sleep(2)
    add_page.type_link()
    time.sleep(2)
    add_page.type_new()
    time.sleep(2)
    add_page.type_name(name)
    add_page.type_button()
    time.sleep(2)
    return add_page.get_prompt_test(value)