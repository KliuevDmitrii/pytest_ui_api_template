from pages.AuthPage import AuthPage

def first_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
