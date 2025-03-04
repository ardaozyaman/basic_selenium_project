from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def removeSpecChars(text):
    cleanedText = re.sub(r'[^a-zA-Z0-9İÜÖÇĞ]', '', text)
    return cleanedText

def waitClick(wait:WebDriverWait,element):
    return wait.until(EC.element_to_be_clickable(element))

def page_has_loaded(driver:webdriver.Chrome):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

























