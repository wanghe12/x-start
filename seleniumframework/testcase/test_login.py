import unittest
from selenium import webdriver
from PO.login_page import LoginPage
import time
from commons.get_driver import getDriver
from commons.read_excel import readExcel
from PO import realhome_page
import warnings


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
       warnings.simplefilter("ignore",ResourceWarning)
       self.url="https://xymind.net:3000/#/login"
       self.driver=getDriver()
       self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        lp.driver_quit()


    def test1(self):  #用户名为空
        global lp
        lp=LoginPage(self.driver)
        lp.open(self.url)
        username = readExcel("name", 1, 0)
        password = int(readExcel("name", 1, 1))
        lp.mouse_click(self.driver,username, password)
        self.assertEqual(lp.get_loginfmsg(),u"账号和密码不能为空",msg="验证失败！")


    def test2(self):  #正确的用户名密码
        username = readExcel("name", 2, 0)
        password = int(readExcel("name", 2, 1))
        lp.mouse_click(self.driver,username, password)
        self.assertEqual(lp.get_loginsmsg(),u"管理员02",msg="验证失败！")
        rhp=realhome_page.RealHomePage(self.driver)
        rhp.run_signout() #登陆成功后退出
        #lp.run_signout() #登陆成功推出

    #@unittest.skip("111")
    def test3(self):  #空的密码
        username = readExcel("name", 3, 0)
        password = readExcel("name", 3, 1)
        lp.mouse_click(self.driver,username, password)
        self.assertEqual(lp.get_loginfmsg(),u"账号和密码不能为空",msg="验证失败！")

    #@unittest.skip("222")
    def test4(self): #用户名密码错误
        username = readExcel("name", 4, 0)
        password = int(readExcel("name", 4, 1))
        lp.mouse_click(self.driver,username, password)
        self.assertEqual(lp.get_loginfmsg(),u"账号或密码错误",msg="验证失败！")


