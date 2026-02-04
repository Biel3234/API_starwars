from django.conf import settings
import requests

# Coleta todos os veiculos da API
def fetch_veiculos():
    veiculos = []
    url = f'{settings.BASE_URL}/vehicles'

    # Para mostrar todos os veiculos em uma pagina so
    while url:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        veiculos.extend(data["results"])
        url = data["next"]

    return veiculos
