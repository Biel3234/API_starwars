from django.conf import settings
import requests

# Coleta todas as naves da API
def fetch_naves():
    naves = []
    url = f'{settings.BASE_URL}/starships'

    # Para mostrar todas as naves em uma pagina so
    while url:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        naves.extend(data["results"])
        url = data["next"]

    return naves