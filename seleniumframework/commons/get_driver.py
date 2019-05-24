from selenium import webdriver

def getDriver():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')  # 禁止浏览器正在别自动化程序控制的提示
    option.add_argument(
        "--user-data-dir=C://Users\Jack Wang\AppData\Local\Google\Chrome//User Data\Default")  # 浏览器配置文件
    driver = webdriver.Chrome(chrome_options=option)
    return driver