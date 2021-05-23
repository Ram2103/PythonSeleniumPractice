import time

import order as order
import pytest
from selenium.webdriver.common.by import By

from CommonFunc.BaseClass import BaseClass
from Pages.LoginPage import LoginPage


class Test_Cart(BaseClass):

    @pytest.fixture()
    def setup(self):
        self.loginPage.login()
        yield
        self.loginPage.logout()

    @pytest.mark.addCart(order == 1)
    def testSearchAndAddCart(self, setup):
        self.homePage.searchItem("samsung m31")
        self.homePage.selectItem()
        Tabs = self.homePage.numberOfWindows()
        self.homePage.switchWindow(Tabs[1])
        self.homePage.isElementPresent(By.XPATH, "//h1[contains(text(),'Samsung Galaxy M31')]")
        self.homePage.selectColor()
        self.homePage.addCart()
        self.homePage.driver.close()
        self.homePage.switchWindow(Tabs[0])

    @pytest.mark.removeCart(order == 2)
    def testRemoveItemInCart(self, setup):
        self.homePage.clickCart()
        self.myCart.removeItem()
        self.myCart.goBack()
