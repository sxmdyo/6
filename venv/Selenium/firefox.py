# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path = '/Users/sougxueming/Downloads/geckodriver')
driver.get("http://10.12.2.175:8844/bamh5/login/;JSESSIONID=272a9672-6850-46c0-9be1-0b9beb70472e")
driver.find_element_by_id("username").send_keys("zhb")
driver.find_element_by_id("password").send_keys("123")
print(driver.find_element_by_id("ehong-code").text)
aa=driver.find_element_by_id("ehong-code").text
driver.find_element_by_id("Txtidcode").send_keys(aa)
driver.find_element_by_id("loginBtn").click()






time.sleep(5)



driver.quit()

