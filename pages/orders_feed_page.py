import allure

from locators.orders_feed_locators import OrdersFeedLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step("получить заказ по его порядковому номеру в общем списке")
    def get_order(self, order_number):
        orders = self.wait_and_find_several_elements(OrdersFeedLocators.order_element)
        return orders[order_number]

    @allure.step("кликнуть на заказ по его порядковому номеру в общем списке")
    def click_on_order(self, order_number):
        order = self.get_order(order_number)
        self.click_element(order)

    @allure.step("получить список ИД заказов")
    def get_order_ids_from_feed(self):
        return list(map(lambda x: x.text, self.wait_and_find_several_elements(OrdersFeedLocators.order_id_element)))

    @allure.step("получить число заказов за все время")
    def get_total_orders(self):
        return int(self.wait_and_find_element(OrdersFeedLocators.total_orders_counter).text)

    @allure.step("получить число заказов за сегодня")
    def get_today_orders(self):
        return int(self.wait_and_find_element(OrdersFeedLocators.today_orders_counter).text)

    @allure.step("ожидать, пока ИД заказа не появится в списке 'в работе'")
    def wait_until_order_id_in_work(self, order_id):
        return self.wait_text_and_find_element_with_timeout(OrdersFeedLocators.orders_id_in_work, order_id, 10)

    @allure.step("вернуть элемент с заголовком состав из модального окна заказа")
    def get_ingredients_title_from_modal_popup(self):
        modal_popup = self.get_modal_popup_element()
        return self.wait_and_find_element_in_element(modal_popup, OrdersFeedLocators.order_ingredients_title)
