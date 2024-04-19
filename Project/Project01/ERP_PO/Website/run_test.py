import unittest
from HTMLTestRunner import HTMLTestRunner
from ERP_PO.Website.test_case.model.function import *
import time

report_dir = './test_report'
test_dir = './test_case'

print("start run test case")
discover = unittest.defaultTestLoader.discover(test_dir,"test_add.py")
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'result.html'
print("start write report..")
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="Test Report", description="erp test")
    runner.run(discover)
    f.close()

print("Test end")
