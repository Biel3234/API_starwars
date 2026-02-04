from django.conf import settings
import requests

# Coleta todos os planetas da API
def fetch_planetas():
    planetas = []
    url = f'{settings.BASE_URL}/planets'

    # Para mostrar todos os personagens em uma pagina so
    while url:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        planetas.extend(data["results"])
        url = data["next"]

    return planetas