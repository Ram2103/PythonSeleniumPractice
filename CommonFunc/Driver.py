from selenium import webdriver

class Driver:
    
    
    def createDriver(self):
        self.driver = webdriver.Chrome(executable_path="/Users/ramanathan/Documents/Automation/Driver/chromedriver")
        self.driver.maximize_window()
        return self.driver

    def getDriver(self):
        return self.driver
