from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
driver.get("https://www.baidu.com")

try:
    driver.find_element_by_css_selector("#su")
    print("css found")
except Exception as e:
    print("css not found",format(e))
time.sleep(3)
driver.quit()