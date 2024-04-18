from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class Login(View):

    def get(self, request):
        
        contexto = {'mensagem':''}
        if not request.user.is_authenticated:
            return HttpResponse('usuario ja está autenticado')
            #return redirect("/veiculos")
        else:
            return render(request, 'autenticacao.html', contexto)
            
    # Obtem as credenciais de autenticação do formulário
    def post(self, request):
        
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        
        #verifica as credenciais de autenticação fornecidas
        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            
            # verifica se
            
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuário autenticado com sucesso')
            
                # return redirect("/veiculos")
                
            return render(request, 'autenticacao.html', {'mensagem': 'usuario inativo'})
        return render(request, 'autenticacao.html', {'mensagem': 'usuário ou senha incorretos'} )
class Logout (View):
    
    def get(self, request):
        imput(request)
        return request(settings.LOGIN_URL)