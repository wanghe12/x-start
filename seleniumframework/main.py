from unittest import TestSuite
from testcase.test_login import TestLogin
from testcase.test_callcenter import TestCallCenter
import unittest
from HTMLTestRunner import HTMLTestRunner
from public.Send_mail import new_file,sendMail
import time
# a = TestSuite()  # 构建用例集
# a.addTest(makeSuite(TestCallCenter, "test"))  #
# b = open('./report/result_login.html', 'wb')
# c = HTMLTestRunner(b, 1, u"自动化测试报告", u"本次测试情况如下")
# c.run(a)
# b.close()

def createsuit():
    testcase = unittest.TestSuite()
    # discover方法定义
    # discover方法筛选出来的用例，循环添加到测试套件中
    test_dir = 'D:\\seleniumframework\\testcase\\'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    # 判断是否为测试用例，自动加载测试用例到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            # print(test_case)
            testcase.addTest(test_case)
    return testcase

if __name__ == "__main__":
    a=createsuit()
    nowtime=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    #print(nowtime)
    report_html="D:\\seleniumframework\\report\\"+nowtime+"report.html"
    #print(report_html)
    b=open(report_html,'wb')
    c=HTMLTestRunner(b,1,u"自动化测试报告",u"本次测试情况如下")
    c.run(a)
    b.close()
    report_path = "D:\\seleniumframework\\report"
    attachment = new_file(report_path)
    print(attachment)
    sendMail(attachment)

