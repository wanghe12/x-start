from unittest import TestCase
from commons.get_driver import getDriver
from PO.login_page import LoginPage
from PO import realhome_page
from PO.callcenter_page import CallCenterPage
from commons.read_excel import readExcel
import time

class TestCallCenter(TestCase):
    @classmethod
    def setUpClass(self):
        self.url = "https://xymind.net:3000/#/login"
        self.driver = getDriver()
        self.driver.implicitly_wait(20)
        global lp
        lp = LoginPage(self.driver)
        lp.open(self.url)
        username = readExcel("name", 2, 0)
        password = int(readExcel("name", 2, 1))
        lp.mouse_click(self.driver, username, password) #首页登陆
        rhg = realhome_page.RealHomePage(self.driver)
        rhg.to_gardenmap() #进入园区报事管理界面

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        lp.driver_quit()


    def test1(self):  #正确的手机号码
        global ccp
        ccp = CallCenterPage(self.driver)
        phonenumber=readExcel("phonenumber",1,0)
        ccp.call_user(phonenumber)
        self.assertEqual(ccp.null_phonenum(),u"电话号码不能为空",msg="验证失败!")
        #ccp.guaduan()

    def test2(self):  # 用户名为空
        phonenumber = int(readExcel("phonenumber",2,0))
        ccp.call_user(phonenumber)
        #self.assertEqual(ccp.call_smag(),u"连接中...",msg="验证失败!")
        self.assertEqual(ccp.call_smag(),u"连接中...",msg="验证失败!")
        ccp.guaduan()

    def test3(self):  # 用户名为空
        phonenumber = int(readExcel("phonenumber",3,0))
        ccp.call_user(phonenumber)
        #self.assertEqual(ccp.call_smag(),u"连接中...",msg="验证失败!")
        self.assertEqual(ccp.bad_phonenum(),u"电话号码输入有误",msg="验证失败!")
        #ccp.guaduan()


