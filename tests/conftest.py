import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.elements_to_find import TestLocators
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
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
