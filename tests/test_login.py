from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.conftest import driver
from tests.elements_to_find import TestLocators


class TestLogin:
    def test_login_by_login_to_account_button(self, driver, correct_login_data):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(correct_login_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(correct_login_data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.COLLECT_BURGER_TEXT))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'Успешный логин через кнопку "Войти в аккаунт"'

    def test_login_by_login_to_account_button_negative(self, driver, incorrect_login_data):
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(incorrect_login_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(incorrect_login_data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.INCORRECT_PASSWORD_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and driver.find_element(
            *TestLocators.INCORRECT_PASSWORD_TEXT), \
            'Неуспешный логин через кнопку "Войти в аккаунт", некорректный пароль'

    def test_login_by_personal_account_button(self, driver, correct_login_data):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(correct_login_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(correct_login_data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.COLLECT_BURGER_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'Успешный логин через кнопку "Личный кабинет"'


    def test_login_by_personal_registration_form(self, driver, correct_login_data):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.RESISTER_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(correct_login_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(correct_login_data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.COLLECT_BURGER_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'Успешный логин через кнопку в форме регистрации'


    def test_login_by_password_recovery_form(self, driver, correct_login_data):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.PASSWORD_RECOVERY_LINK).click()
        driver.find_element(*TestLocators.LOGIN_LINK).click()

        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(correct_login_data.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(correct_login_data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.COLLECT_BURGER_TEXT))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', \
            'Успешный логин через кнопку в форме восстановления пароля'


