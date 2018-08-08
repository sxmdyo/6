import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.maximize_window()
driver.implicitly_wait(8)


driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)


driver.quit()

