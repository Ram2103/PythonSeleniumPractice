import time

from selenium.webdriver.common.by import By

from CommonFunc.WebDriverClass import WebDriverClass


class LoginPage(WebDriverClass):

    btn_Signin = (By.ID, "sign-in")
    input_Username = (By.ID, "main_user_login")
    input_Password= (By.XPATH, "//*[@id='login']//input[@class='label_jump password_txt']")
    btn_Login = (By.CSS_SELECTOR, "#login_button")
    btn_Logout = (By.CSS_SELECTOR, ".usr_signout")
    btn_Profile = (By.ID, "sc_uname")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def login(self):
        self.waitForElement(*self.btn_Signin)
        self.clickElement(*self.btn_Signin)
        self.waitForElement(*self.input_Username)
        self.clickElement(*self.input_Username)
        self.sendText(*self.input_Username, "ramanathan11111@gmail.com")
        self.clickElement(*self.input_Password)
        self.sendText(*self.input_Password, "ramanathan21")
        self.clickElement(*self.btn_Login)
        self.waitForElement(*self.btn_Profile)

    def logout(self):
        self.waitForElement(*self.btn_Profile)
        self.clickElement(*self.btn_Profile)
        self.waitForElement(*self.btn_Logout)
        self.clickElement(*self.btn_Logout)

