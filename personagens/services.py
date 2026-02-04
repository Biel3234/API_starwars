from django.conf import settings
import requests

# Coleta todos os personagens da API
def fetch_personagens():
    personagens = []
    url = f'{settings.BASE_URL}/people'

    # Para mostrar todos os personagens em uma pagina so
    while url:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        personagens.extend(data["results"])
        url = data["next"]

    return personagens