from selenium.webdriver.common.by import By
from CommonFunc.WebDriverClass import WebDriverClass


class HomePage(WebDriverClass):

    def __init__(self, driver):
        self.driver = driver

    input_Search = (By.XPATH, "//input[@id='autocomplete']")
    btn_Search = (By.XPATH, "//span[@id='search']/input[@type='submit']")
    btn_AddCart = (By.ID, "add_cart")
    btn_SelectColor = (By.XPATH, "//li[@id='472787']//span[@class='variant var ']")
    btn_Cart = (By.CSS_SELECTOR, "li.qCart")


    def searchItem(self, text):
        self.sendText(*self.input_Search, text)
        self.clickElement(*self.btn_Search)

    def selectItem(self):
        self.waitForElement(By.XPATH, "//h2[text()='Samsung Galaxy M31 (128 GB)  (6 GB RAM)']")
        self.clickElement(By.XPATH, "//h2[text()='Samsung Galaxy M31 (128 GB)  (6 GB RAM)']")

    def selectColor(self):
        self.clickElement(*self.btn_SelectColor)

    def addCart(self):
        self.moveToElement(self.getElement(*self.btn_AddCart))
        self.clickElement(*self.btn_AddCart)

    def clickCart(self):
        self.clickElement(*self.btn_Cart)