from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fkliuev_dmitrii%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D%26jiraInviteLink%3D"
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

