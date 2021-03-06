from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
'''
这个类主要是完成所有页面的一些公共方法的封装
'''

class Action(object):
    #初始化
    def __init__(self,selef_driver):
        self.driver = selef_driver

    #定义open方法
    def open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    #重写元素定位方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,20).until(lambda driver:driver.find_element(*loc).is_displayed())#判断元素存在否
            return self.driver.find_element(*loc)
        except Exception as e:
            print("未找到%s"%loc)

    def driver_quit(self):
        self.driver.quit()

    #重写send_keys 方法
    def send_keys(self,*loc,value,clear_first=True,click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("未找到%s"%(self,loc))

    def mouse_bclick(self,driver,a,value1):
        '''鼠标双击输入框输入用户名密码,引入鼠标双击事件，防止clear()方法失效'''
        action = ActionChains(driver)   #引入鼠标事件
        action.move_to_element(self.find_element(a)).double_click(self.find_element(a)).perform()
        self.find_element(a).send_keys(value1)  # 输入用户名



