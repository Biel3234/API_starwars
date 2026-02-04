from django.urls import path
from .views import PlanetasListView

urlpatterns = [
    path('planetas/', PlanetasListView.as_view()),
]