import requests

# Hacer una solicitud GET a una API de ejemplo
response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=5)

# Imprimir la respuesta
print(response.status_code)
print(response.json())