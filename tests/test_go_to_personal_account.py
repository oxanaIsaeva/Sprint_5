from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.elements_to_find import TestLocators

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.LOGIN_BUTTON)))

        assert '/login' in driver.current_url, 'Успешный переход по клику на "Личный кабинет"'
