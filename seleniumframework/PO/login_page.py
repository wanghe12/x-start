#coding=utf-8
from selenium.webdriver.common.by import By
from PO import base_page
import time
from selenium.webdriver.common.action_chains import ActionChains
from commons.get_driver import getDriver
from commons.read_excel import readExcel


class LoginPage(base_page.Action):
    name_loc=(By.CLASS_NAME,"usename")
    password_loc=(By.CLASS_NAME,"password")
    submit_loc=(By.CLASS_NAME,"bttn")

    msg_loginf=(By.XPATH,"//*[@id='app']/div[1]/div[3]/div/form/div[3]/span[1]") #登陆失败断言
    msg_logins=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div/span")
    login_timeout=(By.CLASS_NAME,"login_tips")

    def mouse_click(self,driver,value1,value2):
        '''鼠标双击输入框输入用户名密码,引入鼠标双击事件，防止clear()方法失效'''
        action = ActionChains(driver)   #引入鼠标事件
        action.move_to_element(self.find_element(*self.name_loc)).double_click(self.find_element(*self.name_loc)).perform()
        self.find_element(*self.name_loc).send_keys(value1)  # 输入用户名

        action.move_to_element(self.find_element(*self.password_loc)).double_click(self.find_element(*self.password_loc)).perform()
        self.find_element(*self.password_loc).send_keys(value2)  # 输入用户名
        self.find_element(*self.submit_loc).click() #点击登陆
        time.sleep(3)
        try:
            if self.find_element(*self.login_timeout).text == u"登录超时，请重试":
                self.find_element(*self.submit_loc).click()  # 点击登陆
                time.sleep(3)
        except Exception as aa:
            #print(aa)
            print("登陆成功")





    def get_loginsmsg(self):
        return self.find_element(*self.msg_logins).text  #登陆成功获取页面信息

    def get_loginfmsg(self):
        return self.find_element(*self.msg_loginf).text  #登陆失败获取页面信息


'''if __name__=="__main__":
    url = "https://xymind.net:3000/#/login"
    driver = getDriver()
    driver.implicitly_wait(20)
    sp = LoginPage(driver)
    sp.open(url)
    username = readExcel("name", 1, 0)
    password = int(readExcel("name", 1, 1))
    sp.mouse_click(driver,username, password)

    #driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div/form/input[1]").clear()
    #driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div/form/input[2]").clear()
    username = readExcel("name", 2, 0)
    password = int(readExcel("name", 2, 1))
    sp.mouse_click(driver,username, password)

    #sp.clearInput()'''
