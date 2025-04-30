import requests

response = requests.get("http://127.0.0.1:8000/deal-info/all")
data = response.json()  # Получаем данные в формате JSON
print(data)