from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.elements_to_find import TestLocators

class TestConstructor:
    def test_constructor_buns(self, driver):

        driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.SAUCES_SECTION)))

        driver.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.BUNS_SECTION)))

        assert driver.find_element(*TestLocators.BUNS_SECTION), 'Успешный переход к разделу "Булки"'

    def test_constructor_sauces(self, driver):
        driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.SAUCES_SECTION)))

        assert driver.find_element(*TestLocators.SAUCES_SECTION), 'Успешный переход к разделу "Соусы"'

    def test_constructor_fillings(self, driver):
        driver.find_element(*TestLocators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.FILLINGS_SECTION)))
        assert driver.find_element(*TestLocators.FILLINGS_SECTION), 'Успешный переход к разделу "Начинки"'