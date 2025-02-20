import time
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.AuthPage import AuthPage

def first_test():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(4)
    browser.maximize_window()

    auth_page = AuthPage(browser)
    auth_page.go()

    time.sleep(5)