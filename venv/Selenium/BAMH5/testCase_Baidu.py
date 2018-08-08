import unittest
from selenium import webdriver
import time


class testBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
        self.driver.get("http://baidu.com")
    def test_GetBaidu(self):
        self.title=self.driver.title
        print("进入的页面标题为："+self.title)
        self.assertEqual('百度一下，你就知道',self.title,'进入百度页面失败！')
    def test_Search(self):
        self.driver.find_element_by_id("kw").send_keys("软件测试")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.search=self.driver.title
        print("查询页面的标题为："+self.search)
        self.assertEqual('软件测试_百度搜索',self.search,"查询页面进入错误！")
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)