from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
driver.get("https://www.baidu.com")
#打印按钮的高和宽
btnsize=driver.find_element_by_xpath("//*[@id='su']").size
print(btnsize)
time.sleep(2)
#进行浏览器页面的刷新操作
try:
    driver.refresh()
    print("refresh success")
except Exception as e:
    print("refresh failed",format(e))
time.sleep(3)
driver.find_element_by_link_text("新闻").click()
ele = driver.find_element_by_xpath("//*[@id='news']")
#校验单选框、双选框是否选中
try:
    assert ele.is_selected()==True
    print("默认选择正确")
except Exception as e:
    print("默认选择错误",format(e))
time.sleep(2)

driver.quit()