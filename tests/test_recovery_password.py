import allure

from helpers import Helpers
from locators.recovery_page_locators import RecoveryPageLocators
from pages.recovery_password_page import RecoveryPage


class TestRecoveryPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_go_to_recovery_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_signin_by_account)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_sign_in_lost_password)
        recovery_button = recovery_page.wait_and_find_element(RecoveryPageLocators.button_recovery_password)

        assert recovery_button is not None

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_input_email_and_recover_button(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_signin_by_account)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_sign_in_lost_password)
        recovery_page.set_email(Helpers.generate_new_email())
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_recovery_password)
        button_save = recovery_page.wait_and_find_element(RecoveryPageLocators.button_save_in_recovery_password_window)

        assert button_save is not None

    @allure.title('Проверка фокуса на поле с паролем при клике по кнопке скрыть/показать')
    def test_click_on_button_hide_view(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_signin_by_account)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_sign_in_lost_password)
        recovery_page.set_email(Helpers.generate_new_email())
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_recovery_password)
        recovery_page.click_element_by_locator(RecoveryPageLocators.button_click_on_eye)

        assert recovery_page.is_element_in_focus(RecoveryPageLocators.input_recovery_password) is True
