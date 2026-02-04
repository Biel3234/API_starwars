from django.urls import path
from .views import PersonagensListView

urlpatterns = [
    path('personagens/', PersonagensListView.as_view()),
]