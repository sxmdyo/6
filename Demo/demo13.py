from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#设置不同分辨率
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
driver.get("http://www.baidu.com")
time.sleep(2)
print(driver.get_window_size())

driver.set_window_size(1280,800)
time.sleep(1)
print(driver.get_window_size())

print(driver.title)

#方法一
try:
    assert u'百度一下'in driver.title
    print("assertion success")
except Exception as e:
    print("assertion failed",format(e))

#方法二
if "百度一下，你就知道" ==  driver.title:
    print("assertion success")
else:
    print("assertion failed")
time.sleep(3)
element = driver.find_element_by_xpath("//*[@id='kw']")
element.send_keys("selenium test")
time.sleep(1)
element.send_keys(Keys.CONTROL + 'a')
element.send_keys(Keys.BACKSPACE)

driver.quit()