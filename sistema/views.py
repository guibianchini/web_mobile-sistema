# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

class Login(View):
    """
    Class Based View para autenticação de usuários
    """
    def get(self, request):
        contexto = {'mensagem': ''}
        if not request.user.is_authenticated:
            return render(request, 'autenticacao.html', contexto)
        else:
            return HttpResponse('Usuário já está autenticado!')
            # return render(request, 'veiculos.html', contexto)
    
    def post(self, request):
        # Obtém as credenciais de autenticação do formulário
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        # logger.info('Usuario: {}'.format(usuario))
        # logger.info('Senha: {}'.format(senha))

        # Verifique se as credenciais de autenticação sao validas
        user = authenticate(request,username=usuario, password=senha)
        if user is not None:

            # Verifica se o usuário ainda está ativo no sistema
            if user.is_active:
                    login(request, user)
                    return HttpResponse('Login efetuado com sucesso!')
                    # return redirect("/veiculos")

            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo!'})
            
        return render(request, 'autenticacao.html', {'mensagem': 'Login ou senha inválido!'})

class Logout(View):
    """
    Class Based View para logout de usuários
    """
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
