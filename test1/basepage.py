from selenium import webdriver

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
    def back(self):
        self.driver.back()
    def foward(self):
        self.driver.forward()

    def open_url(self,url):
        self.driver.get(url)
    def quit(self):
        self.driver.quit()
