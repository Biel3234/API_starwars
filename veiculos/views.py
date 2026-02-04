from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import VeiculosSerializer
from .services import fetch_veiculos

class VeiculosListView(APIView):
    def get(self, request):
        veiculos = fetch_veiculos() # Todos os veiculos

        veiculos_filtrados = veiculos

        # Filtros
        name = request.query_params.get("name") # Pega o nome do veiculo na URL
        model = request.query_params.get("model") # Pega o modelo na URL
        manufacturer = request.query_params.get("manufacturer") # Pega o fabricante na URL
        vehicle_class = request.query_params.get("vehicle_class") # Pega a classe na URL

        if name:
            veiculos_filtrados = [
                v for v in veiculos_filtrados if name.lower().replace(" ", "") in v['name'].lower().replace(" ", "")
            ]
        
        if model:
            veiculos_filtrados = [
                v for v in veiculos_filtrados if model.lower().replace(" ", "") in v['model'].lower().replace(" ", "")
            ]

        if manufacturer:
            veiculos_filtrados = [
                v for v in veiculos_filtrados if manufacturer.lower().replace(" ", "") == v['manufacturer'].lower().replace(" ", "")
            ]

        if vehicle_class:
            veiculos_filtrados = [
                v for v in veiculos_filtrados if vehicle_class.lower().replace(" ", "") == v['vehicle_class'].lower().replace(" ", "")
            ]

        
        # Tratando erro caso nao encontre o veiculo
        if not veiculos_filtrados:
            return Response(
                {"detail": "Nenhum veiculo encontrado"},
                status=status.HTTP_200_OK
            )   
        
        serializer = VeiculosSerializer(veiculos_filtrados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
