from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path='/Users/sougxueming/Downloads/geckodriver')
driver.get("https://news.baidu.com")
time.sleep(2)
new_link=driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a")
pagetitle = new_link.text
print("当前页面的标题为"+pagetitle)
new_link.click()
handls = driver.window_handles


for handl in handls:
    if handl !=driver.current_window_handle:
        print("切换到第二个窗口",handl)
        #driver.close()
        driver.switch_to_window(handl)

print(driver.title)
try:
    assert pagetitle in driver
    print("test pass")
except Exception as e:
    print("test fail")

driver.quit()