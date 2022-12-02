from django.urls import path
from apps.vehiculo.views import vehiculo_view
app_name = 'vehiculo'
urlpatterns = [
    path('newv/', vehiculo_view, name='crear_persona'),
    #path('listv/', persona_list, name='lista'),
]



