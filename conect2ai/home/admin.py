from django.contrib import admin
from .models import InfoHome, Publicacao, Artigo, TextoInicialPags, LinhaPesquisa, OutraAcao

admin.site.register(InfoHome)
admin.site.register(Publicacao)
admin.site.register(Artigo)
admin.site.register(TextoInicialPags)
admin.site.register(LinhaPesquisa)
admin.site.register(OutraAcao)
