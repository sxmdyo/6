from test1.BrowserEngine import BrowserEngine

class TestBrowserEngine(object):
    def open_browser(self):
        brower = BrowserEngine()
        driver = brower.get_Browser()
ta = TestBrowserEngine()
ta.open_browser()
