#获取浏览器版本号
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.get("https://www.baidu.com")

time.sleep(2)


driver.maximize_window()
driver.implicitly_wait(6)


driver.execute_script("window.alert('这是一个测试Alert弹窗');")
time.sleep(2)
driver.switch_to_alert().accept()  # 点击弹出里面的确定按钮
# driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮
#找到页面上的全部图片，之后遍历
element = driver.find_elements_by_tag_name("img")
for i in element:
    print(i.text)
    print(i.size)
    print(i.tag_name)
element1 = driver.find_elements_by_xpath("//*[@href]")
for e in element:
    print(i.get_attribute("href"))
driver.get_screenshot_as_file(r'/Users/sougxueming/Downloads/baidu.png')

time.sleep(2)
print(driver.capabilities['browserVersion'])
driver.quit()