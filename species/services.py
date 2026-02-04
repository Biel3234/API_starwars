from django.conf import settings
import requests

# Coleta todas as especies da API
def fetch_species():
    species = []
    url = f'{settings.BASE_URL}/species'

    # Para mostrar todas as especies em uma pagina so
    while url:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        species.extend(data["results"])
        url = data["next"]

    return species
