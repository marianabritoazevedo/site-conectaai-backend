from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-english', views.index_ing, name='index_ing'),
    path('index-francais', views.index_fra, name='index_fra'),
    path('publicacoes', views.publicacoes, name='publicacoes'),
    path('publicacoes-english', views.publicacoes_ing, name='publicacoes_ing'),
    path('publicacoes-francais', views.publicacoes_fra, name='publicacoes_fra'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('pesquisa-english', views.pesquisa_ing, name='pesquisa_ing'),
    path('pesquisa-francais', views.pesquisa_fra, name='pesquisa_fra'),
    path('divulgacao', views.divulgacao, name='divulgacao'),
    path('divulgacao-english', views.divulgacao_ing, name='divulgacao_ing'),
    path('divulgacao-francais', views.divulgacao_fra, name='divulgacao_fra'),
]