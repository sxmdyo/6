
import unittest
from selenium import webdriver
import time

class login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path = '/Users/sougxueming/Downloads/geckodriver')
        self.driver.get("http://10.12.2.175:8844/bamh5/login/;JSESSIONID=272a9672-6850-46c0-9be1-0b9beb70472e")
        self.driver.find_element_by_id("username").send_keys("zhb")
        self.driver.find_element_by_id("password").send_keys("123")
        yanzhengma=self.driver.find_element_by_id("ehong-code").text
        self.driver.find_element_by_id("Txtidcode").send_keys(yanzhengma)
        self.driver.find_element_by_id("loginBtn").click()
    def test_enter(self):
        title=self.driver.title
        self.assertEqual("一级BAM系统",title,"登录成功")
    def test_sreenname(self):
        sreenname=self.driver.find_element_by_id("screenName").text
        assertEqual("zhanghb",sreenname,"登录页面用户名错误")
    def tearDown(self):
        self.driver.quit()
        print(" test over")



if __name__ == '__main__':
    unittest.main()