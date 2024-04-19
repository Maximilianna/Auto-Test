from ERP_PO.Website.test_case.page_object.BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    input_username = [By.ID, "username"]
    input_password = [By.ID, "password"]
    input_butt = [By.TAG_NAME, "button"]

    def type_user(self, username):
        self.input_element(self.input_username[0],
                           self.input_username[1],
                           username)

    def type_pass(self, password):
        self.input_element(self.input_password[0],
                           self.input_password[1],
                           password)

    def type_butt(self):
        self.click_element(self.input_butt[0],
                           self.input_butt[1])


def login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_user(username)
    login_page.type_pass(password)
    login_page.type_butt()
