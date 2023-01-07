from django.urls import path
from apps.vehiculo.views import vehiculo_view
from apps.vehiculo.views import vehiculo_persona
app_name = 'vehiculo'
urlpatterns = [
    path('newv/', vehiculo_persona.as_view(), name='crear_persona'),
    #path('listv/', persona_list, name='lista_vehiculos'),
]



