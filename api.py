import json
import requests

import settings


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": settings.VALID_EMAIL,
                "password": settings.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json()
        return status, amount

    def create_pet(self) -> json:
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Molly', "type": 'dog', "age": 2, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def update_pet(self) -> json:
        """Запрос к Swagger сайта для обновления данных о питомце с передачей всех обязательных полей"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Molly_Taylor', "type": 'dog'}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_updated_pet(self) -> json:
        """Запрос к Swagger сайта для получеения данных питомца, который был изменен"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().update_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_name = res.json()['pet']['name']
        status = res.status_code
        return status, pet_name

    def failed_update_pet_empty_type(self):
        """Запрос к Swagger сайта для обновления данных о питомце с передачей не всех обязательных полей -
        без типа питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Molly_Taylor'}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def failed_update_pet_empty_name(self):
        """Запрос к Swagger сайта для обновления данных о питомце с передачей не всех обязательных полей -
        без имени питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "type": 'dog'}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def like_pet(self):
        """Запрос к Swagger сайта для для добавления лайка питомцу без лайка"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status, pet_id

    def delete_pet(self) -> json:
        """Запрос к Swagger сайта для удаления питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status, pet_id

    def get_liked_pet(self) -> json:
        """Запрос к Swagger сайта для получеения данных питомца, который был лайкнут"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().like_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_id = res.json()['pet']['id']
        likes = res.json()['pet']['likes_count']
        status = res.status_code
        return status, pet_id, likes

    def get_deleted_pet(self) -> json:
        """Запрос к Swagger сайта для верификации удаления питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().delete_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status


Pets().get_liked_pet()
