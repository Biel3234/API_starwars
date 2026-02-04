from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonagensSerializer
from .services import fetch_personagens


class PersonagensListView(APIView):
    def get(self, request):
        personagens = fetch_personagens() # Todos os personagens

        personagens_filtrados = personagens

        # Filtros
        name = request.query_params.get("name") # Pega o nome do personagem na URL
        gender = request.query_params.get("gender") # Pega o sexo do personagem na URL

        if name:
            personagens_filtrados = [
                p for p in personagens_filtrados if name.lower() in p['name'].lower()
            ]
        
        if gender:
            personagens_filtrados = [
                p for p in personagens_filtrados if gender.lower() == p['gender'].lower()
            ]
        # Tratando erro caso nao encontre o personagem
        if not personagens_filtrados:
            return Response(
        {"detail": "Nenhum personagem encontrado"},
        status=status.HTTP_200_OK
        )   
        
        serializer = PersonagensSerializer(personagens_filtrados, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


