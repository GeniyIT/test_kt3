import requests

class BaseRequest:
   def __init__(self, base_url):
       self.base_url = base_url

   def get(self, endpoint):
       url = f"{self.base_url}/{endpoint}"
       response = requests.get(url)
       return response

   def post(self, endpoint, data):
       url = f"{self.base_url}/{endpoint}"
       response = requests.post(url, json=data)
       return response


base_url = "https://petstore.swagger.io"
api = BaseRequest(base_url)

 


user_id = 1
response = api.get(f"user/{user_id}")
print(response.json())

 


new_user_data = {"username": "example_user", "email": "example@example.com"}
response = api.post("user", new_user_data)
print(response.json())



order_id = 1
response = api.get(f"store/order/{order_id}")
print(response.json())


new_order_data = {"petId": 1, "quantity": 1, "status": "placed"}
response = api.post("store/order", new_order_data)
print(response.json())