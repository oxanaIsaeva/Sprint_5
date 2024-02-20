from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.elements_to_find import TestLocators


class TestRegistration:
    def test_registration(self, driver, correct_registration_data):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.RESISTER_BUTTON).click()

        driver.find_element(*TestLocators.NAME_INPUT_FIELD_REG).send_keys(correct_registration_data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_REG).send_keys(correct_registration_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(correct_registration_data.password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', \
            'Успешная регистрация нового пользователя'

    def test_registration_negative(self, driver, incorrect_registration_data):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.RESISTER_BUTTON).click()

        driver.find_element(*TestLocators.NAME_INPUT_FIELD_REG).send_keys(incorrect_registration_data.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD_REG).send_keys(incorrect_registration_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(incorrect_registration_data.password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.INCORRECT_PASSWORD_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' and driver.find_element(*TestLocators.INCORRECT_PASSWORD_TEXT), \
            'Неуспешная регистрация нового пользователя, некорректный пароль'