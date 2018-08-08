from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')

driver.get("https://www.baidu.com")
driver.implicitly_wait(3)

try:
    driver.find_element_by_partial_link_text("主页").click()
    print("partial link text found")
except Exception as e:
    print("partial link text not found",format(e))
time.sleep(2)
driver.quit()