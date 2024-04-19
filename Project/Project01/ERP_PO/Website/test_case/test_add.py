from ERP_PO.Website.test_case.model import function, myunit
from ERP_PO.Website.test_case.page_object.AddPage import add
from ddt import ddt, data, unpack
import unittest

@ddt
class TestAdd(myunit.TestMyUnit):


    @data(*function.get_csv_data())
    @unpack
    def test_add(self,name,value):
        text = add(self.driver, name, value)
        function.get_screenshot(self.driver, name)
        self.assertEqual(value, text, msg='与预期结果不一致')
