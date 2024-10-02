import random


class Helpers:
    @staticmethod
    def generate_new_email():
        return f'testUserReg{random.randint(100, 999)}@yandex.ru'

    @staticmethod
    def generate_new_password():
        return f'{random.randint(100000, 999999)}'

    @staticmethod
    def generate_new_name():
        return f'user{random.randint(100, 999)}'

    @staticmethod
    def create_random_user_data_for_registration():
        return {
            "email": Helpers.generate_new_email(),
            "password": Helpers.generate_new_password(),
            "name": Helpers.generate_new_name()
        }
