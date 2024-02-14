import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.elements_to_find import TestLocators
from selenium.webdriver.chrome.options import Options
from classes import UserRegistration
import random

number = random.randint(1111, 9999)

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture()
def log_in_to_account(driver):
    driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

    driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys("oksanarsaeva5432@ya.ru")
    driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys("oks123")
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (TestLocators.COLLECT_BURGER_TEXT)))


@pytest.fixture()
def correct_login_data():
    return UserRegistration(name='', login='oksanarsaeva5432@ya.ru', password='oks123')


@pytest.fixture()
def incorrect_login_data():
    return UserRegistration(name='', login='oksanarsaeva5432@ya.ru', password='12345')

@pytest.fixture()
def correct_registration_data():
    return UserRegistration(name='Oksana', login=f'oksanaisaeva{number}@ya.ru', password='oks555')

@pytest.fixture()
def incorrect_registration_data():
    return UserRegistration(name='Oksana', login='oksanaisaeva5422@ya.ru', password='555')
