from django.urls import path
from veiculo.views import ListarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos')
]
