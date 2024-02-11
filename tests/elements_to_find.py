from selenium.webdriver.common.by import By
class TestLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "html/body/div/div/header/nav/a/p[text()='Личный Кабинет']"
    # Кнопка "Личный кабинет" на главной странице
    EMAIL_INPUT_FIELD = By.NAME, "name" # Поле ввода 'Email'
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name='Пароль']" # Поле ввода 'Пароль'
    LOGIN_BUTTON = By.XPATH, "html/body/div/div/main/div/form/button[text()='Войти']" # Кнопка 'Войти'
    COLLECT_BURGER_TEXT = By.XPATH, "html/body/div/div/main/section/h1[text()='Соберите бургер']"
    # Текст "Соберите бургер" на главной странице
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, "html/body/div/div/main/section/div/button[text()='Войти в аккаунт']"
    # Кнопка "Войти в аккаунт" на главной странице
    RESISTER_BUTTON = By.XPATH, "html/body/div/div/main/div/div/p/a[text()='Зарегистрироваться']"
    # Линк "Зарегистрироваться", переход на форму регистрации
    LOGIN_LINK = By.XPATH, "html/body/div/div/main/div/div/p/a[text()='Войти']"
    # Линк "Войти", переход в личный кабинет
    PASSWORD_RECOVERY_LINK = By.XPATH, "html/body/div/div/main/div/div/p/a[text()='Восстановить пароль']"
    # Линк "Восстановить пароль", переход к форме восстановления пароля
    CONSTRUCTOR_MENU = By.XPATH, "html/body/div/div/header/nav/ul/li/a/p[text()='Конструктор']"
    # Линк на секцию "Конструктор"
    CONSTRUCTOR_SECTION = By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"
    # Секция "Конструктор"
    STELLAR_BURGERS_LOGO = By.XPATH, "html/body/div/div/header/nav/div[@class='AppHeader_header__logo__2D0X2']"
    # Лого "Stellar Burgers"
    LOG_OUT_BUTTON = By.XPATH, "html/body/div/div/main/div/nav/ul/li/button[text()='Выход']" # Кнопка 'Выход'
    LOGIN_TEXT = By.XPATH, "html/body/div/div/main/div/h2[text()='Вход']" # Текст 'Вход'
    SAUCES_BUTTON = By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Соусы']"
    # Кнопка 'Соусы' в консттрукторе
    SAUCES_SECTION = By.XPATH, ".//img[@alt='Соус Spicy-X']" # Секция 'Соусы' конструктора
    BUNS_BUTTON = By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Булки']"
    # Кнопка 'Булки' в консттрукторе
    BUNS_SECTION = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']" # Секция 'Булки' конструктора
    FILLINGS_BUTTON = By.XPATH, "html/body/div/div/main/section/div/div/span[text()='Начинки']"
    # Кнопка 'Начинки' в консттрукторе
    FILLINGS_SECTION = By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']" # Секция 'Начинки' конструктора