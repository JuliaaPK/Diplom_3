import allure

from Urls import Urls
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step("залогиниться с email и паролем")
    def login(self, email, password):
        self.open_page(Urls.USER_LOGIN)
        email_field = self.wait_and_find_element(PersonalAccountPageLocators.email_field)
        email_field.send_keys(email)

        password_field = self.wait_and_find_element(PersonalAccountPageLocators.password_field)
        password_field.send_keys(password)

        self.click_element_by_locator(PersonalAccountPageLocators.button_sign_in)
        self.wait_until_url_to_be(Urls.BASE_PAGE_URL)

    @allure.step("перейти в личный кабинет по ссылке в шапке")
    def to_personal_account_by_link_in_header(self):
        self.click_element_by_locator(PersonalAccountPageLocators.button_my_account)

    @allure.step("перейти в историю заказов")
    def to_orders_history(self):
        self.click_element_by_locator(PersonalAccountPageLocators.link_history)

    @allure.step("нажать кнопку выйти в личном кабинете")
    def clck_logout(self):
        self.click_element_by_locator(PersonalAccountPageLocators.button_logout)
        self.wait_until_url_to_be(Urls.USER_LOGIN)

    @allure.step("получить список ИД заказов из истории")
    def get_order_ids_from_history(self):
        return list(map(
            lambda x: x.text,
            self.wait_and_find_several_elements(PersonalAccountPageLocators.order_id_in_history)
        ))
