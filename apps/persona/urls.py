from django.urls import path
from apps.persona.views import saludoP,persona_view, persona_list
app_name = 'persona'
urlpatterns = [
    path('saludop/', saludoP, name='index'),
    path('newp/', persona_view, name='crear_persona'),
    path('listp/', persona_list, name='persona_listar'),
]
