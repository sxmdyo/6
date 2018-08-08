import re
from selenium import webdriver

driver=webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')

driver.implicitly_wait(5)
driver.get("http://home.baidu.com/contact.html")

#查看页面的源代码，在Selenium中有driver.page_source 这个方法得到
#Python中利用正则，需要导入re模块
doc = driver.page_source
emails=re.findall(r'[\w]+@[\w\.-]+',doc)
for email in emails:
    print(email)

driver.quit()