import time

from ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    input_username = [By.CLASS_NAME, "username"]
    input_password = [By.NAME, "password"]
    input_button = [By.ID, "signIn"]

    def type_username(self, User):
        self.input_element(self.input_username[0],
                           self.input_username[1],
                           User)

    def type_password(self, Pass):
        self.input_element(self.input_password[0],
                           self.input_password[1],
                           Pass)

    def click_login(self):
        self.click_element(self.input_button[0],
                           self.input_button[1])

    input_link = [By.PARTIAL_LINK_TEXT, "分类"]
    def type_link(self):
        self.click_element(self.input_link[0],self.input_link[1])

def login(driver, User, Pass):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(User)
    login_page.type_password(Pass)
    login_page.click_login()
