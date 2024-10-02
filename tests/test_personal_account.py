import allure

from Urls import Urls
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Проверка перехода в личным кабинет при клике по кнопке "Личный кабинет"')
    def test_move_to_personal_account_page(self, driver):
        personal_page = PersonalAccountPage(driver)
        personal_page.open_page(Urls.BASE_PAGE_URL)
        personal_page.to_personal_account_by_link_in_header()

        assert driver.current_url == Urls.USER_LOGIN

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_move_to_history(self, driver, new_random_user):
        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])
        personal_page.to_personal_account_by_link_in_header()
        personal_page.to_orders_history()

        assert driver.current_url == Urls.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_account_logout(self, driver, new_random_user):
        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])
        personal_page.to_personal_account_by_link_in_header()
        personal_page.clck_logout()

        assert driver.current_url == Urls.USER_LOGIN
