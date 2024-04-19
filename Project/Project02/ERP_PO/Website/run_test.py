from HTMLTestRunner import HTMLTestRunner
import unittest
import time

#报告文件存放位置
report_dir = './test_report'
#测试文件位置
test_dir = './test_case'

print("start run test case")
discover = unittest.defaultTestLoader.discover(test_dir,"add_test.py")
now = time.strftime("%Y-%m-%d-%H-%M-%S")
report_name = report_dir + '/' + now + 'result.html'
print("start write report..")
with open(report_name,"wb") as f:
    runner = HTMLTestRunner(stream=f,title="Test Report",description="erp test")
    runner.run(discover)
    f.close()
print("test end")
