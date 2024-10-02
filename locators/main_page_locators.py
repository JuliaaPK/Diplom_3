from selenium.webdriver.common.by import By


class MainPageLocators:
    link_constructor = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")  # Ссылка "Конструктор" на главной странице
    link_orders_feed = (
    By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")  # Ссылка "Лента Заказов" на главной странице
    create_burger_title = (
    By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")  # Заголовок "Соберите бургер" в конструкторе
    orders_feed_title = (
    By.XPATH, ".//h1[contains(text(), 'Лента заказов')]")  # Заголовок "Лента заказов" в ленте заказов
    ingredient_element = (
    By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")  # Ингредиент на главной странице
    ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter')]")  # Счетчик ингредиента
    order_basket = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")  # Корзина заказа
    button_create_order = (
    By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ" на главной странице
    created_order_id_title = (
    By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")  # Идентификатор созданного заказа
    details_popup_title = (
    By.XPATH, ".//h2[contains(text(), 'Детали ингредиента')]")  # Заголовок окна Детали ингредиента
