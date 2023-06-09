# Generated by Django 4.2.1 on 2023-05-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_artigos', models.IntegerField(default=0, verbose_name='Quantidade de artigos')),
                ('numero_pesquisadores', models.IntegerField(default=0, verbose_name='Quantidade de pesquisadores')),
                ('numero_projetos', models.IntegerField(default=0, verbose_name='Quantidade de projetos')),
                ('texto_inicial_port', models.TextField(default='Texto em construção', verbose_name='Texto inicial - Português')),
                ('texto_inicial_ing', models.TextField(default='Text under construction', verbose_name='Texto inicial - Inglês')),
                ('texto_inicial_fra', models.TextField(default='Texte en construction', verbose_name='Texto inicial - Francês')),
                ('texto_opcoes_port', models.TextField(default='Texto em construção', verbose_name='Texto opções site - Português')),
                ('texto_opcoes_ing', models.TextField(default='Text under construction', verbose_name='Texto opções site - Inglês')),
                ('texto_opcoes_fra', models.TextField(default='Texte en construction', verbose_name='Texto opções site - Francês')),
            ],
        ),
    ]
