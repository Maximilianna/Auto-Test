from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://10.255.4.105:14753/login")

    def find_element(self, type, value):
        return self.driver.find_element(type, value)

    def click_element(self, type, value):
        self.find_element(type, value).click()

    def input_element(self, type, value, data):
        self.find_element(type, value).send_keys(data)
