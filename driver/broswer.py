#封装浏览器驱动
from selenium import webdriver
def chrome_broswer():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver