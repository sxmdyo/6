import time
from selenium import webdriver

class GetSubString():

    def get_search_result(self):

        driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")

        driver.get("https://www.baidu.com")

        driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")

        time.sleep(1)

        driver.find_element_by_xpath("//*[@id='su']").click()

        time.sleep(2)

        string = driver.find_element_by_xpath("//*/div[@class='nums']").text
        print(string)
        #切割字符串
        string_right = string.split("约")[1] #展示字符串右边
        print(string_right)
        string_left = string.split("约")[0] #展示字符串左边
        print(string_left)

t = GetSubString()
t.get_search_result()
