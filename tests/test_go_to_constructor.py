from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.elements_to_find import TestLocators

class TestGoToConstructor:
    def test_go_to_constructor_by_constructor_menu(self, driver):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.LOGIN_BUTTON)))

        driver.find_element(*TestLocators.CONSTRUCTOR_MENU).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.COLLECT_BURGER_TEXT)))

        assert driver.find_element(*TestLocators.CONSTRUCTOR_SECTION), \
            'Успешный переход к конструктору по клику на "Конструктор"'

    def test_go_to_constructor_by_stellar_burgers_logo(self, driver):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.LOGIN_BUTTON)))

        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.COLLECT_BURGER_TEXT)))

        assert driver.find_element(*TestLocators.CONSTRUCTOR_SECTION), \
            'Успешный переход к конструктору по клику на логотип Stellar Burgers'
