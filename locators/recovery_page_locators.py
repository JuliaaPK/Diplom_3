from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    button_signin_by_account = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    button_sign_in_lost_password = (
    By.LINK_TEXT, "Восстановить пароль")  # Кнопка "Восстановить пароль" в окне на странице логина
    input_email_in_lost_password = (
        By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']"
    )  # Поле для ввода email в окне восстановления пароля
    button_recovery_password = (
        By.XPATH, ".//button[contains(text(),'Восстановить')]"
    )
    button_save_in_recovery_password_window = (By.XPATH, ".//button[contains(text(), 'Сохранить')]")
    button_click_on_eye = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    modal_layer = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")
    input_recovery_password = (
        By.XPATH, ".//input[@name='Введите новый пароль']"
    )
