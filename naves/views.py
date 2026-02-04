from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import NavesSerializer
from .services import fetch_naves

class NaveListView(APIView):

    def get(self, request):
        naves = fetch_naves()
        naves_filtradas = naves
    
        # Filtros
        name = request.query_params.get("name")
        model = request.query_params.get("model")
        manufacturer = request.query_params.get("model")

        if name:
            naves_filtradas = [
                n for n in naves_filtradas if (name.lower()).replace(" ", "") in (n["name"].lower()).replace(" ", "")
            ]
        
        if model:
            naves_filtradas = [
                n for n in naves_filtradas if model.lower().replace(" ", "") in n["model"].lower().replace(" ", "")
            ]

        if manufacturer:
            naves_filtradas = [
                n for n in naves_filtradas if manufacturer.lower().replace(" ", "") in n["manufacturer"].lower().replace(" ", "")
            ]

        if not naves:
            return Response(
                {"detail": "Nenhum personagem encontrado"},
            status=status.HTTP_200_OK
            )
        
        serializer = NavesSerializer(naves_filtradas, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
