from selenium.webdriver.common.by import By

from CommonFunc.WebDriverClass import WebDriverClass


class MyCart(WebDriverClass):

    def __init__(self, driver):
        self.driver = driver

    btn_Popup_Remove = (By.XPATH, "//a[@class='prod-remove']")

    def removeItem(self):
        self.waitForElement(By.XPATH, "//div[@class='item']")
        self.clickElement(By.XPATH, "//div[@class='item']//a[text()='Samsung Galaxy M31 (128 GB)  (6 GB RAM)']//following::a[@class='remove']")
        self.clickElement(*self.btn_Popup_Remove)
        #assert False == self.isElementPresent(By.XPATH, "//div[@class='item']//a[text()='Samsung Galaxy M31 (128 GB)  (6 GB RAM)']")

