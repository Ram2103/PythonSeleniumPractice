import pytest
import sys

sys.path.append(".")

from CommonFunc.Driver import Driver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.MyCart import MyCart

@pytest.fixture(scope="class")
def OneTimeSetup(request):
    objDriver = Driver()
    driver = objDriver.createDriver()
    driver.get("https://www.shopclues.com/")

    request.cls.driver = driver
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    request.cls.myCart = MyCart(driver)
    yield
    driver.quit()


