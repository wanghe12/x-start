from PO import base_page
from selenium.webdriver.common.by import By
import time
class RealHomePage(base_page.Action):
    msg_logins=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div/span") #登陆成功断言
    button_loginout=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[2]") #登陆成功后退出按钮
    button_wljk=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/p")  #物联监控按钮

    def run_signout(self):
        '''登录成功后退出'''
        self.find_element(*self.msg_logins).click() #点击管理员02图标
        time.sleep(1)
        self.find_element(*self.button_loginout).click() #点击退出登录图标
        time.sleep(2)

    def to_gardenmap(self):
        """进入园区报事管理电子地图界面"""
        self.find_element(*self.button_wljk).click() #点击物联监控图标
        time.sleep(2)

