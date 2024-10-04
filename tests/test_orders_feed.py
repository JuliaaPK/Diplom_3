import allure

from Urls import Urls
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrdersFeed:
    @allure.title('Проверка появления всплывающего окна с деталями заказа при клике на заказ')
    def test_open_details_popup_for_order(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open_page(Urls.ORDERS_FEED)
        orders_feed.click_on_order(3)
        ingredients_title = orders_feed.get_ingredients_title_from_modal_popup()

        assert ingredients_title is not None and ingredients_title.is_displayed()

    @allure.title('Проверка отображения заказов из раздела "История заказов" в разделе "Лента заказов"')
    def test_users_orders_visible_in_feed_orders_from_history_orders(self, driver, new_random_user):
        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])

        main_page = MainPage(driver)
        main_page.create_order_with_first_bun_and_first_sauce()

        personal_page.to_personal_account_by_link_in_header()
        personal_page.to_orders_history()
        order_ids_from_user_history = personal_page.get_order_ids_from_history()
        main_page.to_orders_feed_by_link_in_header()

        feed_page = OrdersFeedPage(driver)
        order_ids_from_feed = feed_page.get_order_ids_from_feed()

        intersection = set(order_ids_from_user_history).intersection(order_ids_from_feed)

        assert len(intersection) == len(order_ids_from_user_history)

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_increment_total_orders(self, driver, new_random_user):
        feed_page = OrdersFeedPage(driver)
        feed_page.open_page(Urls.ORDERS_FEED)
        current_total_orders = feed_page.get_total_orders()

        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])

        main_page = MainPage(driver)
        main_page.create_order_with_first_bun_and_first_sauce()

        feed_page.open_page(Urls.ORDERS_FEED)
        updated_total_orders = feed_page.get_total_orders()

        assert updated_total_orders > current_total_orders

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_increment_today_orders(self, driver, new_random_user):
        feed_page = OrdersFeedPage(driver)
        feed_page.open_page(Urls.ORDERS_FEED)
        current_today_orders = feed_page.get_today_orders()

        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])

        main_page = MainPage(driver)
        main_page.create_order_with_first_bun_and_first_sauce()

        feed_page.open_page(Urls.ORDERS_FEED)
        updated_today_orders = feed_page.get_today_orders()

        assert updated_today_orders > current_today_orders

    @allure.title('Проверка отображения нового заказа в разделе "В работе" после его оформления')
    def test_new_order_in_work(self, driver, new_random_user):
        personal_page = PersonalAccountPage(driver)
        personal_page.login(new_random_user["email"], new_random_user["password"])

        main_page = MainPage(driver)
        main_page.create_order_with_first_bun_and_first_sauce()

        personal_page.to_personal_account_by_link_in_header()
        personal_page.to_orders_history()
        order_id = personal_page.get_first_order_id_from_history()
        main_page.to_orders_feed_by_link_in_header()

        feed_page = OrdersFeedPage(driver)
        order_in_work = feed_page.wait_until_order_id_in_work(order_id)

        assert order_in_work is not None
