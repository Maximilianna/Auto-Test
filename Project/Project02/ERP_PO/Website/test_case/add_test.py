import unittest
from ddt import ddt, data, unpack
from ERP_PO.Website.test_case.model import function,myunit
from ERP_PO.Website.test_case.page_object.LoginPage import login
from ERP_PO.Website.test_case.page_object.AddPage import add


@ddt
class Add_test(myunit.TestMyUnit):

    @data(*function.get_csv_data())
    @unpack
    def test_add(self, name, value):
        login(self.driver, "XTGLY", "123456")
        text = add(self.driver, name, value)
        function.get_screenshot(self.driver, name + value)
        self.assertEqual(text, value, msg="与预期结果不一致")