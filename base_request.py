import json

import requests
import pprint


class BaseRequest:
    def init(self, base_url):
        self.base_url = base_url


    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:
            if request_type == 'GET':
                response = requests.get(url)
            elif request_type == 'POST':
                response = requests.post(url, json=data)
            elif request_type == 'PUT':
                response = requests.put(url, json=data)
            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True
        return response

    def get(self, endpoint, endpoint_id, expected_error=True):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id='', body=None):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body, expected_error=True)
        return response.json()

    def delete(self, endpoint, endpoint_id=''):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()['message']

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()['message']


BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)

data = {
    "id": 3,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2023-12-27T18:25:17.448Z",
    "status": "placed",
    "complete": False
}

user_data = {
    'id': 2,
    'username': "AK",
    'firstName': "Artem",
    'lastName': "Kamaldinov",
    'email': "artemkamaldinov@mail.ru",
    'password': "Artem12345",
    'phone': "912132132123",
    'userStatus': 0
  }

#Добавлениу заказа
# push_order = base_request.post('store', 'order', data) 

#Удаление заказа
# base_request.delete('store/order', 3) 

#получение информации о списке товаров
# store_info = base_request.get('store', 'inventory') 
# pprint.pprint(store_info)

 #получение информации о заказе
# result = base_request.get('store/order', 2)  
# pprint.pprint(result)

#Добавление пользователя
# user = base_request.post('user', body=user_data) 
# pprint.pprint(user)

#Изменение пользователя
# user = base_request.put('user', 'AK', user_data)
# pprint.pprint(user)

#Получение информации о пользователе
# user2 = base_request.get('user', 'AK')
# pprint.pprint(user2)

#Удаление пользователя
# delete = base_request.delete('user', 'AK')
# print(delete)