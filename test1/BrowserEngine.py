from selenium import webdriver
class BrowserEngine(object):
    def __init__(self,driver,type="FireFox"):
        self.driver = driver
        self.browser_type = type

    def get_Browser(self):
        if self.browser_type == "FireFox":
            driver = webdriver.Firefox(executable_path="/Users/sougxueming/Downloads/geckodriver")
        else:
            self.browser_type =="Chrome"
            driver = webdriver.Chrome(executable_path="/Users/sougxueming/Downloads/chromedriver")
        return driver



