import platform
import json
import requests

system = platform.system()

data = {'system': platform.system()}
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data_json = json.dumps(data)
r = requests.post('http://127.0.0.1:8000/api/add/', data=data_json, headers=headers)
