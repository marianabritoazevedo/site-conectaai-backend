from django.db import models

class InfoHome(models.Model):
    numero_artigos = models.IntegerField(default=0, verbose_name='Quantidade de artigos')
    numero_pesquisadores = models.IntegerField(default=0, verbose_name='Quantidade de pesquisadores')
    numero_projetos = models.IntegerField(default=0, verbose_name='Quantidade de projetos')
    texto_inicial_port = models.TextField(default='Texto em construção', verbose_name='Texto inicial - Português')
    texto_inicial_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial - Inglês')
    texto_inicial_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial - Francês')
    texto_opcoes_port = models.TextField(default='Texto em construção', verbose_name='Texto opções site - Português')
    texto_opcoes_ing = models.TextField(default='Text under construction', verbose_name='Texto opções site - Inglês')
    texto_opcoes_fra = models.TextField(default='Texte en construction', verbose_name='Texto opções site - Francês')

    def __str__(self):
        return str(self.numero_artigos) + ' artigos, ' + str(self.numero_pesquisadores) + ' pesquisadores, ' + str(self.numero_projetos) + ' projetos'
