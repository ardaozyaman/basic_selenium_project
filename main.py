from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from utils import *
import random


class LCWTest(unittest.TestCase):

    COOKIES_BUTTON = (By.ID, "cookieseal-banner-accept")
    OPT_IN_CLOSE = (By.CLASS_NAME, "ins-web-opt-in-reminder-close-button")
    NAV_LISTS = (By.CLASS_NAME, "menu-nav__lists")
    NAV_LIST_ITEMS = (By.CLASS_NAME, "menu-header-item")
    CATEGORIES = ("KADIN", "ERKEK", "KIZ ÇOCUK", "ERKEK ÇOCUK")

    CAT_PRODUCT_GRID = (By.CLASS_NAME, "product-grid")
    CAT_PRODUCT_GRID_ITEM = (By.CSS_SELECTOR, ".product-card.product-card--one-of-4")

    PROD_INFO = (By.CSS_SELECTOR, ".row.info-panel")
    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "[class='add-to-card']",
    )  # Sorunlu, tutarsız selector
    SIZE_SELECT_BOX = (
        By.CSS_SELECTOR,
        ".option-box.option-size-box.option-size-box__stripped",
    )

    def setUp(self):
        self.driver = webdriver.Chrome(keep_alive=False)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def test_mainCase(self):
        driver = self.driver
        maxAttempts = 3
        while maxAttempts > 1:
            try:
                self.navigateToHomepage(driver)
                self.goToProductPage(driver, byPassCookies=maxAttempts < 3)
                self.selectRandomProduct(driver)
                self.addProductToCart(driver)
                break
            except Exception as e:
                maxAttempts -= 1
                print(f"Error: {e}")
                print(f"Remaining attempts: {maxAttempts}")
                if maxAttempts == 0:
                    self.fail()
                time.sleep(1)

        self.verifyCart(driver)

    def navigateToHomepage(self, driver):
        driver.get("https://www.lcwaikiki.com/")
        self.wait.until(lambda driver: page_has_loaded(driver))
        time.sleep(1)
    #happy path testi değile monkey testi deniliyor olması lazım buna kesin sorarsın neden random diye buddym
    def selectRandomProduct(self, driver):
        prodGrid = driver.find_element(*self.CAT_PRODUCT_GRID)
        prodElements = prodGrid.find_elements(*self.CAT_PRODUCT_GRID_ITEM)
        productGridElement = random.choice(prodElements)
        driver.execute_script("arguments[0].scrollIntoView(true);", productGridElement)
        productGridElement.click()
        time.sleep(1)

    def addProductToCart(self, driver):
        prodInfoElement = driver.find_element(*self.PROD_INFO)
        sizeSelectBox = prodInfoElement.find_element(*self.SIZE_SELECT_BOX)
        sizeSelectBox.click()
        time.sleep(1)
        addToCartButton = prodInfoElement.find_element(*self.ADD_TO_CART_BUTTON)
        addToCartButton.click()
        time.sleep(1)

    def verifyCart(self, driver):
        driver.get("https://www.lcw.com/sepetim")
        self.wait.until(lambda driver: page_has_loaded(driver))
        time.sleep(2)
        driver.get("https://www.lcw.com")
        self.wait.until(lambda driver: page_has_loaded(driver))
        time.sleep(2)

    def goToProductPage(self, driver, byPassCookies=False):
        self.wait.until(lambda driver: page_has_loaded(driver))
        time.sleep(1)
        if not byPassCookies:
            waitClick(self.wait, driver.find_element(*self.COOKIES_BUTTON)).click()
            waitClick(self.wait, driver.find_element(*self.OPT_IN_CLOSE)).click()

        navElement = driver.find_element(*self.NAV_LISTS)
        navElements = navElement.find_elements(*self.NAV_LIST_ITEMS)
        chosenNavElements = [nav for nav in navElements if removeSpecChars(nav.text) in map(removeSpecChars, self.CATEGORIES)]
        random.choice(chosenNavElements).click()
        self.wait.until(lambda driver: page_has_loaded(driver))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
