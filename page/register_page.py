#注册
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from page.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.url = "http://localhost/upload/user.php?act=register"
        time.sleep(3)
        #定位器
        self.locator_username = (By.XPATH, '//input[@id="username"]')
        self.locator_email = (By.XPATH, '//input[@id="email"]')
        self.locator_password = (By.XPATH, '//input[@id="password1"]')
        self.locator_repossword = (By.XPATH, '//input[@id="conform_password"]')
        self.locator_MSN = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[6]/td[2]/input')
        self.locator_QQ = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[7]/td[2]/input')
        self.locator_banphone = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[8]/td[2]/input')
        self.locator_jiaphone = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[9]/td[2]/input')
        self.locator_telephone = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[10]/td[2]/input')
        self.locator_mibaotishi = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[11]/td[2]/select')
        self.locator_mibaodaan = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[12]/td[2]/input')
        self.locator_denglu = (By.XPATH, '/html/body/div[5]/div[3]/div[1]/form/table/tbody/tr[14]/td[2]/input[3]')
        self.locator_rasser = (By.XPATH, '/html/body/div[7]/div[2]/div/div/div/font/b')
    def username(self,usernamekeys):
        self.driver.find_element(*self.locator_username).send_keys(usernamekeys)
        time.sleep(1)
    def email(self,emailkeys):
        self.driver.find_element(*self.locator_email).send_keys(emailkeys)
        time.sleep(1)
    def password(self,passwordkeys):
        self.driver.find_element(*self.locator_password).send_keys(passwordkeys)
        time.sleep(1)
    def repassword(self,repasswordkeys):
        self.driver.find_element(*self.locator_repossword).send_keys(repasswordkeys)
        time.sleep(1)
    def MSN(self,MSNkeys):
        self.driver.find_element(*self.locator_MSN).send_keys(MSNkeys)
        time.sleep(1)
    def QQ(self,QQkeys):
        self.driver.find_element(*self.locator_QQ).send_keys(QQkeys)
        time.sleep(1)
    def banphone(self,banphongkeys):
        self.driver.find_element(*self.locator_banphone).send_keys(banphongkeys)
        time.sleep(1)
    def jiaphone(self,jiaphonekeys):
        self.driver.find_element(*self.locator_jiaphone).send_keys(jiaphonekeys)
        time.sleep(1)
    def telephone(self,telephonekeys):
        self.driver.find_element(*self.locator_telephone).send_keys(telephonekeys)
        time.sleep(1)
    def mibaotishi(self):
        ele = self.driver.find_element(*self.locator_mibaotishi)
        sele =  Select(ele)
        sele.select_by_index(3)
        time.sleep(1)
    def mibaodaan(self,mibaodaankeys):
        self.driver.find_element(*self.locator_mibaodaan).send_keys(mibaodaankeys)
        time.sleep(1)
    def denglu(self):
        self.driver.find_element(*self.locator_denglu).click()
        time.sleep(1)
    def rasser(self):
        result = self.driver.find_element(*self.locator_rasser).text
        return result



    def register(self,usernamekeys,emailkeys,passwordkeys,repasswordkeys,MSNkeys,
                 QQkeys,banphongkeys,jiaphonekeys,telephonekeys,mibaodaankeys):
        self.open()
        self.username(usernamekeys)
        self.email(emailkeys)
        self.password(passwordkeys)
        self.repassword(repasswordkeys)
        self.MSN(MSNkeys)
        self.QQ(QQkeys)
        self.banphone(banphongkeys)
        self.jiaphone(jiaphonekeys)
        self.telephone(telephonekeys)
        self.mibaotishi()
        self.mibaodaan(mibaodaankeys)
        self.denglu()
        rasser_result = self.rasser()
        return rasser_result


class  GoShopping(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.url = "http://localhost/upload/index.php"
        time.sleep(3)
        self.locator_search = By.XPATH, '//input[@id="keyword"]'
        self.locator_addproduct = By.XPATH,'//form[@id="compareForm"]/div/div[1]/a/img'
        self.locator_buyproduct = By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img'
        self.locator_accounts = By.XPATH,'/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img'
        self.locator_asser = By.XPATH,'//form[@id="theForm"]/div[3]/h6/span'
        self.locator_gouwuliucheng = By.XPATH, '//li[@id="ECS_CARTINFO"]/a'
        self.locator_jiesuanzhongx = By.XPATH, '/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img'
        self.locator_search = By.XPATH, '//input[@id="keyword"]'
        self.locator_search = By.XPATH, '//input[@id="keyword"]'

    def search(self,searchkeys):
        self.driver.find_element(*self.locator_search).send_keys(searchkeys)
        self.driver.find_element(*self.locator_search).send_keys(Keys.ENTER)
        time.sleep(1)
    def addproduct(self):#点击商品
        self.driver.find_element(*self.locator_addproduct).click()
        time.sleep(1)
    def buyproduct(self):#点击购买
        self.driver.find_element(*self.locator_buyproduct).click()
        time.sleep(1)
    def accounts(self):#点击结算中心
        self.driver.find_element(*self.locator_accounts).click()
        time.sleep(1)
    def asser(self):
        result = self.driver.find_element(*self.locator_asser).text
        return result

    def login(self):#cookie登录
        self.driver.add_cookie({"name": "ECS[user_id]", "value": "1"})
        self.driver.add_cookie({"name": "ECS[password]", "value": "bf246186ac50c2043b1775dcaa4f3194"})
        cookie = self.driver.get_cookies()
        self.driver.get("http://localhost/upload/user.php")
        time.sleep(1)
    def gouwuliucheng(self):
        self.driver.find_element(*self.locator_gouwuliucheng).click()
        time.sleep(1)
    def jiesuanzhongxin(self):
        self.driver.find_element(*self.locator_jiesuanzhongx).click()
        time.sleep(1)

    def shopping(self,searchkeys):
        self.open()
        self.search(searchkeys)
        self.addproduct()
        self.buyproduct()
        self.accounts()
        self.login()
        self.gouwuliucheng()
        self.jiesuanzhongxin()
        asser_result = self.asser()
        return asser_result







