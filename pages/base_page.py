import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    base_wait_timeout = 4

    def __init__(self, driver):
        self.driver = driver

    @allure.step("открыть страницу с определенным URL")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("поиск (с ожиданием появления) элемента внутри другого элемента")
    def wait_and_find_element_in_element(self, parent, locator_of_element):
        WebDriverWait(parent, self.base_wait_timeout) \
            .until(expected_conditions.visibility_of_element_located(locator_of_element))
        return parent.find_element(*locator_of_element)

    @allure.step("поиск (с ожиданием появления) элемента по всему документу")
    def wait_and_find_element(self, locator_of_element):
        return self.wait_and_find_element_in_element(self.driver, locator_of_element)

    @allure.step("поиск (с ожиданием появления) элементов по всему документу")
    def wait_and_find_several_elements(self, locator_of_element):
        WebDriverWait(self.driver, self.base_wait_timeout) \
            .until(expected_conditions.visibility_of_any_elements_located(locator_of_element))
        return self.driver.find_elements(*locator_of_element)

    @allure.step("поиск (с заданным ожиданием появления) элемента, содержащего определенный текст, по всему документу")
    def wait_text_and_find_element_with_timeout(self, locator_of_element, text, timeout):
        WebDriverWait(self.driver, timeout) \
            .until(expected_conditions.text_to_be_present_in_element(locator_of_element, text))
        return self.driver.find_element(*locator_of_element)

    @allure.step("поиск (с ожиданием появления) элемента, содержащего определенный текст, по всему документу")
    def wait_text_and_find_element(self, locator_of_element, text):
        return self.wait_text_and_find_element_with_timeout(locator_of_element, text, self.base_wait_timeout)

    @allure.step("ожидание, пока URL не станет равным заданному")
    def wait_until_url_to_be(self, url):
        WebDriverWait(self.driver, self.base_wait_timeout).until(expected_conditions.url_to_be(url))

    @allure.step("выполнить клик по элементу (с ожиданием появления этого эелемента)")
    def click_element_by_locator(self, locator):
        self.hide_modal_layers()
        WebDriverWait(self.driver, self.base_wait_timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("выполнить клик по элементу")
    def click_element(self, element):
        self.hide_modal_layers()
        element.click()

    @allure.step("проверка того, находится ли элемент (с ожиданием его появления) в фокусе")
    def is_element_in_focus(self, locator):
        return self.wait_and_find_element(locator) == self.driver.switch_to.active_element

    @allure.step("ожидание того, как элемент (по локатору) станет невидимым")
    def wait_until_invisibility(self, locator):
        WebDriverWait(self.driver, self.base_wait_timeout) \
            .until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("ожидание того, как элемент станет невидимым")
    def wait_until_invisibility_element(self, element):
        WebDriverWait(self.driver, self.base_wait_timeout) \
            .until(expected_conditions.invisibility_of_element(element))

    @allure.step("перетащить элемент 'source' в элемент 'target'")
    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("ожидание, пока загрузочный слой станет невидим")
    def wait_until_loading_overlay_hidden(self):
        self.wait_until_invisibility(BasePageLocators.loading_overlay)

    @allure.step("закрыть модальный попап, нажатием на крестик, с ожиданием скрытия этого попапа")
    def close_modal_popup_and_wait_closing(self):
        modal = self.get_modal_popup_element()
        self.click_element_by_locator(BasePageLocators.button_modal_close)
        self.wait_until_invisibility_element(modal)

    @allure.step("скрыть слои, перехватывающие нажатия")
    def hide_modal_layers(self):
        WebDriverWait(self.driver, self.base_wait_timeout) \
            .until(expected_conditions.presence_of_all_elements_located(BasePageLocators.modal_overlays))

        overlays = self.driver.find_elements(*BasePageLocators.modal_overlays)

        for overlay in overlays:
            self.driver.execute_script("arguments[0].style.visibility = 'hidden'", overlay)

    @allure.step("вернуть элемент с модальным окном")
    def get_modal_popup_element(self):
        return self.wait_and_find_element(BasePageLocators.modal_popup)