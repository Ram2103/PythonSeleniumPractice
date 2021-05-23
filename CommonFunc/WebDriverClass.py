import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from CommonFunc.Driver import Driver

class WebDriverClass(Driver):

    def __init__(self, driver):
        #self.driver = driver
        pass
    
    def getElement(self, by, element):
        try:
            return self.driver.find_element(by, element)
        except Exception as e:
            print(e)

    def sendText(self, by, element, text):
        try:
            #self.clickElement(by, element)
            self.getElement(by, element).clear()
            self.getElement(by, element).send_keys(text)
        except Exception as e:
            print(e)

    def clickElement(self, by, element):
        try:
            self.getElement(by, element).click()
        except Exception as e:
            print(e, "Failed to click element: "+element)

    def moveToElement(self, element):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform
        except Exception as e:
            print(e)

    def waitForElement(self, by, element):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((by, element)))
        except Exception as e:
            print(e)

    def acceptAlert(self):
        try:
            alert = Alert(self.driver)
            alert.accept
        except Exception as e:
            print(e)

    def numberOfWindows(self):
        return self.driver.window_handles

    def switchWindow(self, tabs):
        try:
            return self.driver.switch_to.window(tabs)
        except Exception as e:
            print(e)

    def isElementPresent(self, by, element):
        try:
            self.waitForElement(by, element)
            self.getElement(by, element).is_displayed()
            print(element+" Element is present on the screen")
            return True
        except Exception as e:
            return False

    def goBack(self):
        self.driver.back()




