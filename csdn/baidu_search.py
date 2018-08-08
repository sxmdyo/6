from selenium import webdriver
import time
from test1.basepage import BasePage

class testBaidu(object):
    driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
    driver.implicitly_wait(3)
    basepage=BasePage(driver)
    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(2)
    def serch_baidu(self):
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
        time.sleep(2)
        self.basepage.back()
        time.sleep(2)
        self.basepage.foward()
        time.sleep(2)
        self.basepage.quit()
baidu = testBaidu()
baidu.open_baidu()
baidu.serch_baidu()