import allure

from Urls import Urls
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestMain:
    @allure.title('Проверка перехода в конструктор при клике по кнопке "Конструктор"')
    def test_move_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.USER_LOGIN)
        main_page.to_constructor_by_link_in_header()
        create_burgers_title = main_page.get_title_of_create_burger()

        assert create_burgers_title is not None

    @allure.title('Проверка перехода в ленту заказов при клике по кнопке "Лента заказов"')
    def test_move_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.to_orders_feed_by_link_in_header()
        orders_feed_title = main_page.get_title_of_orders_feed()

        assert orders_feed_title is not None

    @allure.title('Проверка появления всплывающего окна с деталями заказа при клике на ингредиент')
    def test_open_details_popup_for_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient(3)
        ingredient_details_title = main_page.get_title_of_details_popup()

        assert ingredient_details_title is not None and ingredient_details_title.is_displayed()

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_details_popup_for_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient(3)
        modal_popup = main_page.get_modal_popup_element()
        main_page.close_modal_popup_and_wait_closing()

        assert modal_popup.is_displayed() is False

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    def test_increment_ingredient_counter_on_adding(self, driver):
        main_page = MainPage(driver)
        ingredient_number = 3
        origin_counter = main_page.get_ingredient_counter(ingredient_number)
        main_page.add_ingredient_to_order(ingredient_number)
        updated_counter = main_page.get_ingredient_counter(ingredient_number)

        assert updated_counter == origin_counter + 1

    @allure.title('Проверка оформления заказа под авторизованным пользователем')
    def test_create_order_for_login_user(self, driver, new_random_user):
        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(4)
        main_page.click_create_order()
        created_order_id_title = main_page.get_title_of_created_order_id()

        assert created_order_id_title is not None
