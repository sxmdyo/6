from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
driver.get("http://www.baidu.com")
time.sleep(2)
#进入报读新闻页面
#driver.find_element_by_link_text("新闻").click()
#time.sleep(2)
#打印当前页面url和页面标题
print(driver.current_url)
print((driver.title))
#通过ctrl+t新打开一个子页面
#ele=driver.find_element_by_tag_name('boby').send_keys(Keys.CONTROL + 't')
time.sleep(2)
#通过xpath定位页面的radio。然后遍历进行点击操作
# eles = driver.find_elements_by_xpath("//*/input[@type='radio']")
# for i in eles:
#     i.click()
# time.sleep(3)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@title='用户名登录']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='userName']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='password']").click()

time.sleep(2)

driver.quit()