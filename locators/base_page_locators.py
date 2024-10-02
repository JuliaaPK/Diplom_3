from selenium.webdriver.common.by import By


class BasePageLocators:
    modal_popup = (
    By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")  # Главный контейнер любого модального окна на сайте
    button_modal_close = (
    By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")  # Кнопка закрытия модального окна
    loading_overlay = (By.XPATH,
                       ".//div[contains(@class, 'App_App')]/div[contains(@class, 'Modal_modal')]")  # Верхний слой, включаемый при продолжительных операциях
    modal_overlays = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")  # Слои перекрытия нажатий
