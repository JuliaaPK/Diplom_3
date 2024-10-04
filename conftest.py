import pytest
from selenium import webdriver

from Urls import Urls
from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.maximize_window()
    browser.get(Urls.BASE_PAGE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def new_random_user():
    random_user_data = Helpers.create_random_user_data_for_registration()
    response_registration = StellarBurgerApi.stellar_registration_user(random_user_data)
    access_token = response_registration.json()["accessToken"]

    yield random_user_data

    StellarBurgerApi.stellar_delete_user(access_token)
