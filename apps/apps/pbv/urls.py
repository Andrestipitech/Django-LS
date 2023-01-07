from django.urls import path
from apps.pbv.views import saludoP, insertar_pbv, pbv_list, pbv_delete, pbv_editar
from apps.pbv.views import crear_listar, Pbv_editar

app_name = 'pbv'
urlpatterns = [
    path('pbv1/', saludoP, name='index'),
    path('pbv2/', crear_listar.as_view(), name='lista'),
    path('pbvdel/<int:id_pbv>', pbv_delete, name='eliminar_pbv'),
    path('pbvedit/<int:pk>', Pbv_editar.as_view(), name='editar_pbv'),

]
