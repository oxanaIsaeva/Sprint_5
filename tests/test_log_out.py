from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.conftest import log_in_to_account
from tests.elements_to_find import TestLocators

class TestLogOut:
    def test_log_out(self, driver, log_in_to_account):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.LOG_OUT_BUTTON)))

        driver.find_element(*TestLocators.LOG_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.LOGIN_BUTTON)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and driver.find_element(*TestLocators.LOGIN_TEXT), \
            'Успешный выход из аккаунта по кнопке «Выйти» в личном кабинете.'