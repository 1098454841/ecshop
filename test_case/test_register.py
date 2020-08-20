#注册

import unittest
import time

from driver.broswer import chrome_broswer
from lib.utils import read_excel

from page.register_page import RegisterPage#引入page.py文件的RegisterPage类
from page.register_page import GoShopping#引入page.py文件的Goshopping类
class registerTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_broswer()
    def tearDown(self):
        self.driver.quit()
    def test_register(self): #注册流程
        rp = RegisterPage(self.driver)
        content = read_excel()
        print("读取成功", content[3])

        username = content[3][0]
        email = content[3][1]
        password = content[3][2]
        repassword = content[3][3]
        MSN = content[3][4]
        QQ = content[3][5]
        officephone = content[3][6]
        homephone = content[3][7]
        telephone = content[3][8]
        mibaodaan = content[3][9]

        result = rp.register(username,email,password,repassword,MSN,
                             QQ,officephone,homephone,telephone,mibaodaan)
        time.sleep(3)
        print("实际结果",result)
        print("预期结果","sihu")
        self.assertEqual("sihu",result)
    def test_shopping(self): #购物流程
        gs = GoShopping(self.driver)
        result = gs.shopping("衣")
        time.sleep(3)
        print("结果",result)
        self.assertEqual("收货人信息",result)





if __name__ == '__main__':
    unittest.main()





