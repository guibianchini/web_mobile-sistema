# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo

class ListarVeiculos(View):
    """
    View para listar veículos cadastrados
    """

    def get(self, request):
        contexto = {
            'veiculos': Veiculo.objects.all().order_by('marca')
        }
        return render(request, 'veiculo/listar.html', contexto)