from django.urls import path
from .views import EspeciesListView

urlpatterns = [
    path('especies/', EspeciesListView.as_view()),
]