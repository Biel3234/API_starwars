from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import EspeciesSerializer
from .services import fetch_species

class EspeciesListView(APIView):
    def get(self, request):
        especies = fetch_species() # Todas as especies

        especies_filtradas = especies

        # Filtros
        name = request.query_params.get("name") # Pega o nome da especie na URL
        classification = request.query_params.get("classification") # Pega a classificação na URL
        designation = request.query_params.get("designation") # Pega a designação na URL
        language = request.query_params.get("language") # Pega a linguagem na URL

        if name:
            especies_filtradas = [
                s for s in especies_filtradas if name.lower().replace(" ", "") in s['name'].lower().replace(" ", "")
            ]
        
        if classification:
            especies_filtradas = [
                s for s in especies_filtradas if classification.lower().replace(" ", "") in s['classification'].lower().replace(" ", "")
            ]

        if designation:
            especies_filtradas = [
                s for s in especies_filtradas if designation.lower().replace(" ", "") in s['designation'].lower().replace(" ", "")
            ]

        if language:
            especies_filtradas = [
                s for s in especies_filtradas if language.lower().replace(" ", "") in s['language'].lower().replace(" ", "")
            ]

        
        # Tratando erro caso nao encontre a especie
        if not especies_filtradas:
            return Response(
                {"detail": "Nenhuma especie encontrada"},
                status=status.HTTP_200_OK
            )   
        
        serializer = EspeciesSerializer(especies_filtradas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
