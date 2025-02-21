from time import sleep
from pytest_ui_api_template.pages.AuthPage import AuthPage

def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("dimik1986@gmail.com", "di19ma86K@")
    sleep(10)
    assert auth_page.get_current_url().endswith("kliuev_dmitrii/boards")
