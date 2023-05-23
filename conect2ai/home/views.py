from django.shortcuts import render, redirect
from .models import InfoHome, Publicacao

def index(request):
    template_name='index.html'
    info_home = InfoHome.objects.first()
    publicacao = Publicacao.objects.all()
    context = {
        'info_home': info_home,
        'publicacao': publicacao,
    }
    return render(request, template_name, context)

def index_ing(request):
    template_name='index-ingles.html'
    info_home = InfoHome.objects.first()
    publicacao = Publicacao.objects.all()
    context = {
        'info_home': info_home,
        'publicacao': publicacao,
    }
    return render(request, template_name, context)

def index_fra(request):
    template_name='index-frances.html'
    info_home = InfoHome.objects.first()
    publicacao = Publicacao.objects.all()
    context = {
        'info_home': info_home,
        'publicacao': publicacao,
    }
    return render(request, template_name, context)
