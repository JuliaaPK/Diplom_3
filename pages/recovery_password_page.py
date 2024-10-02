import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    @allure.step("вписать email в форме восстановления пароля")
    def set_email(self, email):
        email_field = self.wait_and_find_element(RecoveryPageLocators.input_email_in_lost_password)
        email_field.send_keys(email)
