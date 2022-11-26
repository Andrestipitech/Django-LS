from django.urls import path
from apps.persona.views import saludoP,persona_view

urlpatterns = [
    path('saludop/', saludoP, name='index'),
    path('newp/', persona_view, name='crear_persona'),
    
]
