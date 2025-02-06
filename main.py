from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from utils import *

class LCWTest(unittest.TestCase):
    
    COOKIES_BUTTON = (By.ID,"cookieseal-banner-accept")
    OPT_IN_CLOSE = (By.CLASS_NAME,"ins-web-opt-in-reminder-close-button")
    NAV_LISTS = (By.CLASS_NAME, "menu-nav__lists")
    CAT_PRODUCT_GRID = (By.CLASS_NAME, "product-grid")
    ADD_TO_CART_BUTTON = (By.ID, "")
    CART_BUTTON = (By.CLASS_NAME, "")
    HOMEPAGE_LOGO = (By.CLASS_NAME, "")
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get("https://www.lcwaikiki.com/")

    def test_shopping_flow(self):
        driver = self.driver
        self.wait.until(lambda driver:page_has_loaded(driver))
        waitClick(self.wait,driver.find_element(*self.COOKIES_BUTTON)).click()

        waitClick(self.wait,driver.find_element(*self.OPT_IN_CLOSE)).click()

        elements = driver.find_elements(*(By.CLASS_NAME,"menu-header-item"))
        for element in elements:
            if element.text=="ERKEK":
                element.click()
                break
        
        self.wait.until(lambda driver:page_has_loaded(driver))
    
        prodGrid = driver.find_element(*self.CAT_PRODUCT_GRID)

        prodElements = prodGrid.find_elements(By.CLASS_NAME,"product-card product-card--one-of-4")

        prodElements[0].find_element(By.TAG_NAME, "a").click()

        time.sleep(5)
        #self.assertIn("erkek", driver.current_url)
    """    
        driver.find_element(*self.PRODUCT_LINK).click()
        time.sleep(2)
        self.assertTrue("urun" in driver.current_url)
        
        add_to_cart_btn = driver.find_element(*self.ADD_TO_CART_BUTTON)
        self.assertTrue(add_to_cart_btn.is_displayed())
        add_to_cart_btn.click()
        time.sleep(2)
        
        driver.find_element(*self.CART_BUTTON).click()
        time.sleep(2)
        self.assertIn("sepetim", driver.current_url)
        
        driver.find_element(*self.HOMEPAGE_LOGO).click()
        time.sleep(2)
        self.assertTrue("lcwaikiki.com" in driver.current_url)

    """
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=1)
