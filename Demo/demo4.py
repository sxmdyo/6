from selenium import webdriver
#通过tag-name定位元素
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")

driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
try:
    driver.find_element_by_tag_name("form")
    print("tag name found")
except Exception as e:
    print("tag name not found",format(e))
driver.quit()