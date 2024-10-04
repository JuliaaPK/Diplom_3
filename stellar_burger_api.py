import requests

from Urls import Urls


class StellarBurgerApi:
    @staticmethod
    def stellar_registration_user(user_data):
        return requests.post(Urls.USER_CREATION, json=user_data)

    @staticmethod
    def stellar_delete_user(user_access_token):
        return requests.delete(Urls.USER_DELETE, headers={'Authorization': user_access_token})
