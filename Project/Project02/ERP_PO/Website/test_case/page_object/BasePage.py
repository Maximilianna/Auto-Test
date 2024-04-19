class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://10.255.4.105:14753/login")

    def find_element(self, type, value):
        return self.driver.find_element(type, value)

    def click_element(self,type,locator):
        self.find_element(type,locator).click()

    def input_element(self,type,locator,data):
        self.find_element(type,locator).send_keys(data)
