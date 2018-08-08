from selenium import webdriver

driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.implicitly_wait(3)
driver.get("https://www.baidu.com")

try:
    driver.find_element_by_link_text("新闻")
    print("link texxt found")
except Exception as e:
    print("link text not found",format(e))

try:
    driver.find_element_by_xpath("//*/div[@id='u1']/a[text()='新闻']")
    print("xpath found")
except Exception as e:
    print("xpath not found",format(e))


driver.quit()