from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    # self.driver.find_element_by_css_selector("").click()
    def getCheckOutItems1(self):
        return self.driver.find_element(*CheckOutPage.checkOut1)

    def getCheckOutItems2(self):
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
