import allure
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from pages.AuthPage import AuthPage
from pages.MainPage import MainPage

import pytest

@pytest.mark.skip
def auth_test(browser):
    username = 'Kliuev Dmitrii'
    email = "dimik1986@gmail.com"
    password = "di19ma86K@"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)
    WebDriverWait(browser, 15).until(EC.url_contains("kliuev_dmitrii/boards"))

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url + "заканчивается на kliuev_dmitrii/boards"):
        assert main_page.get_current_url().endswith("kliuev_dmitrii/boards")
    
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть "+username):
             assert info[0] == username
             
        with allure.step("Почта пользователя должна быть "+email):   
             assert info[1] == email
