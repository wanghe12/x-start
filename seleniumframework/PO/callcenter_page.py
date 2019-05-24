from PO import base_page
from selenium.webdriver.common.by import By
import time
from commons import get_driver
from PO import login_page,realhome_page
from selenium.webdriver.common.action_chains import ActionChains

class CallCenterPage(base_page.Action):
    call_center=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/ul/li[4]/div/span") #云对讲平台
    call_yezhu=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[1]/div[3]/i[1]") #呼叫业主

    call_num=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span[2]") #电话搜索
                             #(//*[@id="app"]/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div/input)
    input_phonenum=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div/input") #电话号码输入框
    buttton_search=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div/div/button") #搜索按钮
    call_icon=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[3]") #电话图标

    call_sucess=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div/p[2]") #连接中...
    call_guaduan=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div/img") #挂断图标
    bad_phnum=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]") #输入错的手机号码
    null_phnum=(By.CLASS_NAME,"el-form-item__error") #输入空的手机号码
    def call_user(self,value1):
        #time.sleep(2)
        self.find_element(*self.call_center).click() #点击呼叫中心
        time.sleep(3)
        self.find_element(*self.call_yezhu).click() #点击呼叫业主按钮
        time.sleep(5)
        self.find_element(*self.call_yezhu).click()  # 点击呼叫业主按钮
        time.sleep(3)
        self.find_element(*self.call_num).click() #点击电话搜索
        time.sleep(2)
        self.find_element(*self.input_phonenum).send_keys(value1) #输入电话号码
        self.find_element(*self.buttton_search).click() #点击搜索
        time.sleep(2)

    def dcall_user(self,driver,value1):
        #self.mouse_bclick(driver,*self.call_num,value1)
        action = ActionChains(driver)   #引入鼠标事件
        element1=self.find_element(*self.input_phonenum)
        action.move_to_element(element1).double_click(element1).perform()
        element1.send_keys(value1)    #鼠标双击输入电话号码
        self.find_element(*self.buttton_search).click()  # 点击搜索


    def call_smag(self):
        self.find_element(*self.call_icon).click()  # 拨号
        time.sleep(5)
        return self.find_element(*self.call_sucess).text #返回call成功断言连接中
    def guaduan(self):
        self.find_element(*self.call_guaduan).click()  # 挂断

    def bad_phonenum(self):
        return self.find_element(*self.bad_phnum).text  #电话号码输入有误
    def null_phonenum(self):
        return self.find_element(*self.null_phnum).text #电话号码不能为空



'''if __name__=="__main__":
    url = "https://xymind.net:3000/#/login"
    driver = get_driver.getDriver()
    driver.implicitly_wait(20)
    sp = login_page.LoginPage(driver)
    sp.open(url)
    sp.mouse_click(driver,"gly002", "123456")
    rhg=realhome_page.RealHomePage(driver)
    rhg.to_gardenmap()
    ccp=CallCenterPage(driver)
    ccp.call_user("18620385321")'''



    #sp.clearInput()'''





