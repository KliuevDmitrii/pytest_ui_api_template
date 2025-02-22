from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pytest_ui_api_template.pages.AuthPage import AuthPage

def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("dimik1986@gmail.com", "di19ma86K@")
    WebDriverWait(browser, 15).until(EC.url_contains("kliuev_dmitrii/boards"))
    
    assert auth_page.get_current_url().endswith("kliuev_dmitrii/boards")
