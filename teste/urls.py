from django.urls import path, include
from . import views

app_name = 'teste'

urlpatterns = [
    path('', views.Teste.as_view(), name='usuario'),

    #path('',   views.UsuarioView.as_view(), name='UsuarioView'),
    #path('senha/',   views.AlterarSenha.as_view(), name='altera-senha'),
    #path('telefone/',   views.AddTelefone.as_view(), name='altera-senha'),
    #path('novo/',   views.NovoUsuario.as_view(), name='cadastro'),
    #path('tt/',   views.Testes.as_view(), name='cadastro'),"""
]
