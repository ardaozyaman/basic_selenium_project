from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitClick(wait:WebDriverWait,element):
    return wait.until(EC.element_to_be_clickable(element))

def page_has_loaded(driver:webdriver.Chrome):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'