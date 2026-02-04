from django.conf import settings
import requests

# Coleta todos os personagens da API
def fetch_personagens():
    url = f'{settings.BASE_URL}/people'
    response = requests.get(url)
    return response.json()['results']