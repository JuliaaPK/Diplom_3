from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    button_my_account = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный Кабинет"
    email_field = (By.XPATH, ".//label[text() = 'Email']/following-sibling::*")  # Поле "Email"
    password_field = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле "Пароль"
    button_sign_in = (By.XPATH, ".//button[contains(text(),'Войти')]")  # Кнопка "Войти" на странице логина
    button_logout = (By.XPATH, ".//button[contains(text(),'Выход')]")  # Кнопка "Выход" на странице личного кабинета
    link_history = (
    By.XPATH, ".//a[contains(text(),'История заказов')]")  # Ссылка "История заказов" на странице личного кабинета
    order_id_in_history = (By.XPATH,
                           ".//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits')]")  # Идентификатор заказа в истории заказов
