import allure

from Urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("перейте в конструткор по клику ссылки в шапке")
    def to_constructor_by_link_in_header(self):
        self.click_element_by_locator(MainPageLocators.link_constructor)

    @allure.step("перейте в ленту заказаов по клику ссылки в шапке")
    def to_orders_feed_by_link_in_header(self):
        self.click_element_by_locator(MainPageLocators.link_orders_feed)

    @allure.step("получить ингредиент по поярдковому номеру из общего списка ингредиентов")
    def get_ingredient(self, ingredient_number):
        ingredients = self.wait_and_find_several_elements(MainPageLocators.ingredient_element)
        return ingredients[ingredient_number]

    @allure.step("кликнуть по ингредиенту по поярдковому номеру из общего списка ингредиентов")
    def click_on_ingredient(self, ingredient_number):
        ingredient = self.get_ingredient(ingredient_number)
        self.click_element(ingredient)

    @allure.step("получить текущие число данного ингредиента (по его порядковому номеру) в заказе")
    def get_ingredient_counter(self, ingredient_number):
        ingredient = self.get_ingredient(ingredient_number)
        counter = self.wait_and_find_element_in_element(ingredient, MainPageLocators.ingredient_counter)
        return int(counter.text)

    @allure.step("добавить ингредиент (по его порядковому номеру) в заказ) в заказе")
    def add_ingredient_to_order(self, ingredient_number):
        ingredient = self.get_ingredient(ingredient_number)
        order_basket = self.wait_and_find_element(MainPageLocators.order_basket)
        self.drag_and_drop(ingredient, order_basket)

    @allure.step("нажать кнопку создания заказа")
    def click_create_order(self):
        self.click_element_by_locator(MainPageLocators.button_create_order)

    @allure.step("создать заказ: 2 булки и соус")
    def create_order_with_first_bun_and_first_sauce(self):
        self.open_url_if_its_not_opened_yet(Urls.BASE_PAGE_URL)
        self.add_ingredient_to_order(0)
        self.add_ingredient_to_order(3)
        self.click_create_order()
        self.wait_until_loading_overlay_hidden()
        self.close_modal_popup_and_wait_closing()
