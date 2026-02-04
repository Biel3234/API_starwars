from django.urls import path
from .views import VeiculosListView

urlpatterns = [
    path('veiculos/', VeiculosListView.as_view()),
]