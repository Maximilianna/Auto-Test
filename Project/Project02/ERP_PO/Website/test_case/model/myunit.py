from ERP_PO.driver.driver import Driver
import unittest


class TestMyUnit(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()


