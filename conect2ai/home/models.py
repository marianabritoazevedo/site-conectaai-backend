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

class Publicacao(models.Model):
    img_publicacao = models.ImageField(verbose_name='Imagem da publicação', upload_to='publicacoes/')
    link_publicacao = models.CharField(verbose_name='Link da publicacao', max_length=500)

    def __str__(self):
        return self.link_publicacao 

class Artigo(models.Model):
    titulo = models.CharField(verbose_name='Título do artigo', max_length=500)
    autores = models.TextField(verbose_name='Autores')
    ano = models.IntegerField(verbose_name='Ano de publicação')
    local = models.CharField(verbose_name='Local de publicação', max_length=500)
    link_artigo = models.CharField(verbose_name='Link do artigo', max_length=500)

    def __str__(self):
        return self.titulo + ' - ' + str(self.ano)

class TextoInicialPags(models.Model):
    texto_publicacoes = models.TextField(default='Texto em construção', verbose_name='Texto inicial publicações - Português')
    texto_publicacoes_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial Publicações - Inglês')
    texto_publicacoes_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial Publicações - Francês')
    texto_pesquisa = models.TextField(default='Texto em construção', verbose_name='Texto inicial pesquisa - Português')
    texto_pesquisa_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial pesquisa - Inglês')
    texto_pesquisa_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial pesquisa - Francês')
    texto_equipe = models.TextField(default='Texto em construção', verbose_name='Texto inicial equipe - Português')
    texto_equipe_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial equipe - Inglês')
    texto_equipe_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial equipe - Francês')
    texto_parcerias = models.TextField(default='Texto em construção', verbose_name='Texto inicial parcerias - Português')
    texto_parcerias_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial parcerias - Inglês')
    texto_parcerias_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial parcerias - Francês')
    texto_divulgacao = models.TextField(default='Texto em construção', verbose_name='Texto inicial divulgacao - Português')
    texto_divulgacao_ing = models.TextField(default='Text under construction', verbose_name='Texto inicial divulgacao - Inglês')
    texto_divulgacao_fra = models.TextField(default='Texte en construction', verbose_name='Texto inicial divulgacao - Francês')

    def __str__(self):
        return self.texto_publicacoes

class LinhaPesquisa(models.Model):
    titulo = models.CharField(verbose_name='Linha de pesquisa', max_length=300, default='-')
    titulo_ing = models.CharField(verbose_name='Linha de pesquisa - Inglês', max_length=300, default='-')
    titulo_fra = models.CharField(verbose_name='Linha de pesquisa - Francês', max_length=300, default='-')
    texto = models.TextField(verbose_name='Texto sobre a linha de pesquisa', default='-')
    texto_ing = models.TextField(verbose_name='Texto sobre a linha de pesquisa - Inglês', default='-')
    texto_fra = models.TextField(verbose_name='Texto sobre a linha de pesquisa - Francês', default='-')
    tecnologias = models.TextField(verbose_name='Tecnologias envolvidas (separar por vírgula)', default='-')
    codigo_imagem = models.CharField(verbose_name='Código da imagem do font-awesome', max_length=300, default='-')

    def __str__(self):
        return self.titulo

class OutraAcao(models.Model):
    ACAO_CHOICES = (
        ("Curso", "Curso"),
        ("Evento", "Evento"),
        ("Projeto de extensão", "Projeto de extensão")
    )
    tipo = models.CharField(max_length=100, choices=ACAO_CHOICES, verbose_name='Tipo de ação')
    titulo = models.CharField(max_length=100, verbose_name='Título da ação')
    titulo_ing = models.CharField(max_length=100, verbose_name='Título da ação - Inglês')
    titulo_fra = models.CharField(max_length=100, verbose_name='Título da ação - Francês')
    texto = models.TextField(verbose_name='Texto sobre a ação')
    texto_ing = models.TextField(verbose_name='Texto sobre a ação - Inglês')
    texto_fra = models.TextField(verbose_name='Texto sobre a ação - Francês')

    def __str__(self):
        return self.titulo

class Pesquisador(models.Model):

    PESQUISADOR_CHOICES = (
        ("Pesquisador(a) líder", "Pesquisador(a) líder"),
        ("Pesquisador(a) sênior", "Pesquisador(a) sênior"),
        ("Pesquisador(a) - Graduação", "Pesquisador(a) - Graduação"),
        ("Pesquisador(a) - Mestrado", "Pesquisador(a) - Mestrado"),
        ("Pesquisador(a) - Doutorado", "Pesquisador(a) - Doutorado"),
        ("Outro", "Outro")
    )

    nome = models.CharField(verbose_name='Nome do pesquisador', max_length=200)
    tipo = models.CharField(max_length=200, choices=PESQUISADOR_CHOICES, verbose_name='Tipo de pesquisador')
    email = models.CharField(max_length=200, verbose_name='E-mail do pesquisador')
    github = models.CharField(max_length=200, verbose_name='Github do pesquisador')
    linkedin = models.CharField(max_length=200, verbose_name='Linkedin do pesquisador')
    texto = models.TextField(verbose_name='Texto sobre o pesquisador')
    texto_ing = models.TextField(verbose_name='Texto sobre o pesquisador - Inglês')
    texto_fra = models.TextField(verbose_name='Texto sobre o pesquisador - Francês')
    img_pesquisador = models.ImageField(verbose_name='Imagem do pesquisador', upload_to='fotos/')

    def __str__(self):
        return self.nome

