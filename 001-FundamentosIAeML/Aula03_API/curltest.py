import requests
import json

url = "http://localhost:8000/items"

payload = json.dumps({
    "name": "Felippe",
    "description": "Exemplo de Descrição",
    "price": 10.99,
    "on_offer": False
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)