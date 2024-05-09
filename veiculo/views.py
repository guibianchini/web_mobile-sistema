# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


class ListarVeiculos(View):
    """
    View para listar veículos cadastrados
    """

    def get(self, request):
        contexto = {
            'veiculos': Veiculo.objects.all().order_by('marca')
        }
        return render(request, 'veiculo/listar.html', contexto)

class FotoVeiculo(View):
    """
    View para mostrar imagem de um veículo
    """

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Veículo não encontrado")
        except Exception as exception:
            raise exception