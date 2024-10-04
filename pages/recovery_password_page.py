import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    @allure.step("вписать email в форме восстановления пароля")
    def set_email(self, email):
        email_field = self.wait_and_find_element(RecoveryPageLocators.input_email_in_lost_password)
        email_field.send_keys(email)

    @allure.step("кликнуть по кнопке 'Войти в аккаунт'")
    def click_button_signin_by_account(self):
        self.click_element_by_locator(RecoveryPageLocators.button_signin_by_account)

    @allure.step("кликнуть по кнопке 'Восстановить пароль'")
    def click_button_sign_in_lost_password(self):
        self.click_element_by_locator(RecoveryPageLocators.button_sign_in_lost_password)

    @allure.step("кликнуть по кнопке 'Восстановить'")
    def click_button_recovery_password(self):
        self.click_element_by_locator(RecoveryPageLocators.button_recovery_password)

    @allure.step("кликнуть по кнопке 'Показать/скрыть пароль'")
    def click_button_show_hide_password(self):
        self.click_element_by_locator(RecoveryPageLocators.button_click_on_eye)

    @allure.step("получить элемент кнопки 'Восстановить'")
    def get_button_recovery_password(self):
        return self.wait_and_find_element(RecoveryPageLocators.button_recovery_password)

    @allure.step("получить элемент кнопки 'Сохранить'")
    def get_button_save(self):
        return self.wait_and_find_element(RecoveryPageLocators.button_save_in_recovery_password_window)

    @allure.step("проверка фокуса на поле с паролем")
    def is_input_recovery_password_in_focus(self):
        return self.is_element_in_focus(RecoveryPageLocators.input_recovery_password)
