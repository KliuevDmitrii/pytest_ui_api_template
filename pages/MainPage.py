import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        url = ConfigProvider().get("ui", "base_url")


    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Открыть боковое меню")
    def open_menu(self):
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='header-member-menu-button']"))
            ).click()

    @allure.step("Прочитать информацию о пользователе")    
    def get_account_info(self) -> list[str]:
        container = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.TyNFo3ay3iQKOz"))
        )
        name = container.find_element(By.CSS_SELECTOR, "div.lzFtVDCea8Z9jO").text
        email = container.find_element(By.CSS_SELECTOR, "div.Ej7WGzTnvdxL7I").text

        return [name, email]