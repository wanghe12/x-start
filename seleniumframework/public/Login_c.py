# coding=utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#from GetVerifyCode import get_code
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置中文

def is_element_visible(self, element):
    driver = self.driver
    try:
        the_element = EC.visibility_of_element_located(element)
        assert the_element(driver)
        flag = True
    except:
        flag = False
    return flag

def login(driver, username, password):
    driver.find_element_by_id("txt_username").clear()
    driver.find_element_by_id("txt_username").send_keys(username)
    driver.find_element_by_id("txt_password").clear()
    driver.find_element_by_id("txt_password").send_keys(password)
    driver.find_element_by_id("verifycode").clear()
    #driver.find_element_by_id("verifycode").send_keys(CodeText)
    driver.find_element_by_class_name("button").click()
    time.sleep(2)
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    url = "http://192.168.10.110:8080/WebGis/login"
    driver.get(url)
    #CodeText = get_code(driver)
    login(driver, 'baoyong123', 'asdf1234')
