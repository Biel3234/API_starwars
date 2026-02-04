from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PlanetaSerializer
from .services import fetch_planetas

class PlanetasListView(APIView):
    def get(self, request):
        planetas = fetch_planetas() # Todos os planetas

        planetas_filtrados = planetas

        # Filtros
        name = request.query_params.get("name") # Pega o nome do planeta na URL
        climate = request.query_params.get("climate") # Pega o clima do planeta na URL
        terrain = request.query_params.get("terrain") # Pega o terreno do planeta na URL
        population = request.query_params.get("population") # Pega a população do planeta na URL
        gravity = request.query_params.get("gravity") # Pega a gravidade do planeta na URL

        if name:
            planetas_filtrados = [
                p for p in planetas_filtrados if name.lower().replace(" ", "") in p['name'].lower().replace(" ", "")
            ]
        
        if climate:
            planetas_filtrados = [
                p for p in planetas_filtrados if climate.lower().replace(" ", "") == p['climate'].lower().replace(" ", "")
            ]

        if terrain:
            planetas_filtrados = [
                p for p in planetas_filtrados if terrain.lower().replace(" ", "") == p['terrain'].lower().replace(" ", "")
            ]

        if population:
            planetas_filtrados = [
                p for p in planetas_filtrados if population.lower() == p['population'].lower()
            ]

        if gravity:
            planetas_filtrados = [
                p for p in planetas_filtrados if gravity.lower().replace(" ", "") == p['gravity'].lower().replace(" ", "")
            ]

        
        # Tratando erro caso nao encontre o planeta
        if not planetas_filtrados:
            return Response(
                {"detail": "Nenhum planeta encontrado"},
                status=status.HTTP_200_OK
            )   
        
        serializer = PlanetaSerializer(planetas_filtrados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
