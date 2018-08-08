from selenium import  webdriver
import time

driver=webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
#进入12306购票页面
driver.get("https://kyfw.12306.cn/otn/index/init")

fromElt=driver.find_element_by_id("fromStationText")
fromElt.click()

fromElt.send_keys("北京\n")

toElt=driver.find_element_by_id("toStationText")
toElt.click()

toElt.send_keys("上海\n")

selectElt=driver.find_element_by_id("a_search_ticket")
selectElt.click()

dateElt=driver.find_element_by_xpath("//*[@id='date_range']/ul/li[4]/span[1]")
dateElt.click()



driver.quit()