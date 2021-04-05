from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutpage.getCheckOutItems1().click()
        confirmpage = checkoutpage.getCheckOutItems2()
        log.info("Entering country name as ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirmpage.getCountry().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")
        # self.driver.find_element_by_link_text("India").click()
        confirmpage.getChooseCountry().click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmpage.getClickCheckbox().click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmpage.getClickPurchase().click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        confirmpage.getVerifySuccessText().text

        log.info("Text received from application is " + textMatch)

        assert ("Success! Thanksss you! " in textMatch)
