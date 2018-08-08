#利用ID定位元素
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
try:
    driver.find_element_by_id("kw").clear()
    print(" clear success")
except Exception as e:
    print("clear failed",format(e))
time.sleep(3)
driver.quit()