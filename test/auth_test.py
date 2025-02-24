from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage
from pages.MainPage import MainPage

def auth_test(browser):
    email = "dimik1986@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "di19ma86K@")
    WebDriverWait(browser, 15).until(EC.url_contains("kliuev_dmitrii/boards"))

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    assert main_page.get_current_url().endswith("kliuev_dmitrii/boards")
    assert info[0] == 'Kliuev Dmitrii'
    assert info[1] == email
