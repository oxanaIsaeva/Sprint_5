from selenium.webdriver.common.by import By
class TestLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Личный Кабинет']"
    # Кнопка "Личный кабинет" на главной странице
    EMAIL_INPUT_FIELD = By.NAME, "name" # Поле ввода 'Email'
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name='Пароль']" # Поле ввода 'Пароль'
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']" # Кнопка 'Войти'
    COLLECT_BURGER_TEXT = By.XPATH, ".//h1[text()='Соберите бургер']"
    # Текст "Соберите бургер" на главной странице
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    # Кнопка "Войти в аккаунт" на главной странице
    RESISTER_BUTTON = By.XPATH, ".//a[text()='Зарегистрироваться']"
    # Линк "Зарегистрироваться", переход на форму регистрации
    LOGIN_LINK = By.XPATH, ".//a[text()='Войти']"
    # Линк "Войти", переход в личный кабинет
    PASSWORD_RECOVERY_LINK = By.XPATH, ".//a[text()='Восстановить пароль']"
    # Линк "Восстановить пароль", переход к форме восстановления пароля
    CONSTRUCTOR_MENU = By.XPATH, ".//p[text()='Конструктор']"
    # Линк на секцию "Конструктор"
    CONSTRUCTOR_SECTION = By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"
    # Секция "Конструктор"
    STELLAR_BURGERS_LOGO = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"
    # Лого "Stellar Burgers"
    LOG_OUT_BUTTON = By.XPATH, ".//button[text()='Выход']" # Кнопка 'Выход'
    LOGIN_TEXT = By.XPATH, ".//h2[text()='Вход']" # Текст 'Вход'
    SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']"
    # Кнопка 'Соусы' в консттрукторе
    SAUCES_SECTION = By.XPATH, ".//img[@alt='Соус Spicy-X']" # Секция 'Соусы' конструктора
    BUNS_BUTTON = By.XPATH, ".//span[text()='Булки']"
    # Кнопка 'Булки' в консттрукторе
    BUNS_SECTION = By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']" # Секция 'Булки' конструктора
    FILLINGS_BUTTON = By.XPATH, ".//span[text()='Начинки']"
    # Кнопка 'Начинки' в консттрукторе
    FILLINGS_SECTION = By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']" # Секция 'Начинки' конструктора
    INCORRECT_PASSWORD_TEXT = By.XPATH, ".//p[@class='input__error text_type_main-default']" # Ошибка "Некорректный пароль"
    NAME_INPUT_FIELD_REG = By.XPATH, ".//label[text()='Имя']/ancestor::fieldset//input" # Поле ввода 'Имя' в форме регистрации
    EMAIL_INPUT_FIELD_REG = By.XPATH, ".//label[text()='Email']/ancestor::fieldset//input"  # Поле ввода 'Email' в форме регистрации
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"  # Кнопка 'Зарегистрироваться'