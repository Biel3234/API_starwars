from django.urls import path
from .views import NaveListView

urlpatterns = [
    path('naves/', NaveListView.as_view()),
]