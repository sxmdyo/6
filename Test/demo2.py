import time
from selenium import webdriver
class BaiduSearch(object):
    driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")

    def Open_Baidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(2)
    def Test_Search(self):
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
        self.driver.find_element_by_xpath("//*[@id='su']").click()
        time.sleep(3)
        print(self.driver.title)
        try:
            assert "selenium" in self.driver.title
            print("test pass")
        except Exception as e:
            print("test fail")
        self.driver.quit()

baidu = BaiduSearch()
baidu.Open_Baidu()
baidu.Test_Search()
