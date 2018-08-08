from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.get("https://tieba.baidu.com/index.html")

try:
    driver.find_element_by_name("wd")
    print("name found")
except Exception as e:
    print("name not found",format(e))
# driver.execute_script("window.alert('这是一个alert弹框.');")
time.sleep(2)
target = driver.find_element_by_link_text("地区")
driver.execute_script("return arguments[0].scrollIntoView()",target)
time.sleep(2)
driver.quit()