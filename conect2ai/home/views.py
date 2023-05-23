from re import template
from django.shortcuts import render, redirect
from .models import InfoHome, Publicacao, Artigo, TextoInicialPags, LinhaPesquisa, OutraAcao

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


def publicacoes(request):
    template_name = 'publicacoes.html'
    anos_publicacao = Artigo.objects.values('ano').distinct().order_by('-ano')
    texto_inicial = TextoInicialPags.objects.first()

    artigos_por_ano = {}
    for ano in anos_publicacao:
        artigos = Artigo.objects.filter(ano=ano['ano'])
        artigos_por_ano[ano['ano']] = artigos

    context = {
        'artigos_por_ano': artigos_por_ano,
        'texto_inicial': texto_inicial,
    }
    return render(request, template_name, context)

def publicacoes_ing(request):
    template_name='publicacoes-ingles.html'
    anos_publicacao = Artigo.objects.values('ano').distinct().order_by('-ano')
    texto_inicial = TextoInicialPags.objects.first()

    artigos_por_ano = {}
    for ano in anos_publicacao:
        artigos = Artigo.objects.filter(ano=ano['ano'])
        artigos_por_ano[ano['ano']] = artigos

    context = {
        'artigos_por_ano': artigos_por_ano,
        'texto_inicial': texto_inicial,
    }
    return render(request, template_name, context)

def publicacoes_fra(request):
    template_name='publicacoes-frances.html'
    anos_publicacao = Artigo.objects.values('ano').distinct().order_by('-ano')
    texto_inicial = TextoInicialPags.objects.first()

    artigos_por_ano = {}
    for ano in anos_publicacao:
        artigos = Artigo.objects.filter(ano=ano['ano'])
        artigos_por_ano[ano['ano']] = artigos

    context = {
        'artigos_por_ano': artigos_por_ano,
        'texto_inicial': texto_inicial,
    }
    return render(request, template_name, context)

def pesquisa(request):
    template_name = 'pesquisa.html'
    texto_inicial = TextoInicialPags.objects.first()
    linhas_pesquisa = LinhaPesquisa.objects.all()
    for linha_pesquisa in linhas_pesquisa:
        linha_pesquisa.tecnologias = linha_pesquisa.tecnologias.split(',')
    context = {
        'texto_inicial': texto_inicial,
        'linhas_pesquisa': linhas_pesquisa
    }
    return render(request, template_name, context)

def pesquisa_ing(request):
    template_name = 'pesquisa-ingles.html'
    texto_inicial = TextoInicialPags.objects.first()
    linhas_pesquisa = LinhaPesquisa.objects.all()
    for linha_pesquisa in linhas_pesquisa:
        linha_pesquisa.tecnologias = linha_pesquisa.tecnologias.split(',')
    context = {
        'texto_inicial': texto_inicial,
        'linhas_pesquisa': linhas_pesquisa
    }
    return render(request, template_name, context)

def pesquisa_fra(request):
    template_name = 'pesquisa-frances.html'
    texto_inicial = TextoInicialPags.objects.first()
    linhas_pesquisa = LinhaPesquisa.objects.all()
    for linha_pesquisa in linhas_pesquisa:
        linha_pesquisa.tecnologias = linha_pesquisa.tecnologias.split(',')
    context = {
        'texto_inicial': texto_inicial,
        'linhas_pesquisa': linhas_pesquisa
    }
    return render(request, template_name, context)

def divulgacao(request):
    template_name = 'divulgacao-cientifica.html'
    texto_inicial = TextoInicialPags.objects.first()
    publicacao = Publicacao.objects.all()
    acoes = OutraAcao.objects.all()
    context = {
        'texto_inicial': texto_inicial,
        'publicacao': publicacao,
        'acoes': acoes,
    }
    return render(request, template_name, context)

def divulgacao_ing(request):
    template_name = 'divulgacao-cientifica-ingles.html'
    texto_inicial = TextoInicialPags.objects.first()
    publicacao = Publicacao.objects.all()
    acoes = OutraAcao.objects.all()
    context = {
        'texto_inicial': texto_inicial,
        'publicacao': publicacao,
        'acoes': acoes,
    }
    return render(request, template_name, context)

def divulgacao_fra(request):
    template_name = 'divulgacao-cientifica-frances.html'
    texto_inicial = TextoInicialPags.objects.first()
    publicacao = Publicacao.objects.all()
    acoes = OutraAcao.objects.all()
    context = {
        'texto_inicial': texto_inicial,
        'publicacao': publicacao,
        'acoes': acoes,
    }
    return render(request, template_name, context)