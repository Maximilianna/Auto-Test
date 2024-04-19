import unittest
from ERP_PO.Website.test_case.page_object.LoginPage import login
from ERP_PO.driver.driver import Driver


class TestMyUnit(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        login(self.driver,"XTGLY","123456")

    def tearDown(self) -> None:
        self.driver.quit()
