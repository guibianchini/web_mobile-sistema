from django.urls import path
from veiculo.views import ListarVeiculos, FotoVeiculo

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('fotos/<str:arquivo>', FotoVeiculo.as_view(), name='foto-veiculo')
]
