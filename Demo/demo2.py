from selenium import webdriver
import time
#浏览器的前进后退
driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
driver.get("http://www.baidu.com")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
#方法一
try:
    error_massage=driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").is_displayed()
    print("test pass，弹出提示正确")
except Exception as e:
    print("test fail,，弹出提示错误")
#方法二
error_mass=driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text
try:
    error_mass=="请您填写手机/邮箱/用户名"
    print("test pass")
except Exception as e :
    print("test failed")



driver.quit()