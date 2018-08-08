from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path='/Users/sougxueming/Downloads/chromedriver')
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("test")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()