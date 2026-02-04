from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("personagens.urls")),
    path('api/', include("naves.urls")),
    path('api/', include("planetas.urls")),
    path('api/', include("species.urls")),
]
