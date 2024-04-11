# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

class Login(View):
    """
    Class Based View para autenticação de usuários
    """
    def get(self, request):
        contexto = {'mensagem': ''}
        return render(request, 'autenticacao.html', contexto)