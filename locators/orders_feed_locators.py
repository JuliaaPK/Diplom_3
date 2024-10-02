from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    order_ingredients_title = (
    By.XPATH, ".//p[contains(text(), 'Cостав')]")  # Заголовок Состав в модальном окне состава
    order_element = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]")  # Заказ на странице в ленте
    order_id_element = (By.XPATH,
                        ".//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')]")  # ИД заказа на странице в ленте
    total_orders_counter = (
    By.XPATH, ".//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")  # Счетчик всех заказов
    today_orders_counter = (
    By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")  # Счетчик всех заказов за сегодня
    orders_id_in_work = (
    By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")
