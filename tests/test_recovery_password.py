import allure

from helpers import Helpers
from pages.recovery_password_page import RecoveryPage


class TestRecoveryPassword:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_go_to_recovery_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_button_signin_by_account()
        recovery_page.click_button_sign_in_lost_password()
        recovery_button = recovery_page.get_button_recovery_password()

        assert recovery_button is not None

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_input_email_and_recover_button(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_button_signin_by_account()
        recovery_page.click_button_sign_in_lost_password()
        recovery_page.set_email(Helpers.generate_new_email())
        recovery_page.click_button_recovery_password()
        button_save = recovery_page.get_button_save()

        assert button_save is not None

    @allure.title('Проверка фокуса на поле с паролем при клике по кнопке скрыть/показать')
    def test_click_on_button_hide_view(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_button_signin_by_account()
        recovery_page.click_button_sign_in_lost_password()
        recovery_page.set_email(Helpers.generate_new_email())
        recovery_page.click_button_recovery_password()
        recovery_page.click_button_show_hide_password()

        assert recovery_page.is_input_recovery_password_in_focus() is True
