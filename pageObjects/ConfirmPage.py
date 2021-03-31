from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_id("country").send_keys("ind")
    typeCountry = (By.ID, "country")
    # self.driver.find_element_by_link_text("India").click()
    chooseCountry = (By.LINK_TEXT, "India")
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    clickCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element_by_css_selector("[type='submit']").click()
    clickPurchase = (By.CSS_SELECTOR, "[type='submit']")
    # textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
    verifySuccessText = (By.CSS_SELECTOR, "[class*='alert-success']")


    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.typeCountry)

    def getChooseCountry(self):
        return self.driver.find_element(*ConfirmPage.chooseCountry)

    def getClickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.clickCheckbox)

    def getClickPurchase(self):
        return self.driver.find_element(*ConfirmPage.clickPurchase)

    def getVerifySuccessText(self):
        return self.driver.find_element(*ConfirmPage.verifySuccessText)

