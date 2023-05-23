# Generated by Django 4.2.1 on 2023-05-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_outraacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do pesquisador')),
                ('tipo', models.CharField(choices=[('Pesquisador(a) líder', 'Pesquisador(a) líder'), ('Pesquisador(a) sênior', 'Pesquisador(a) sênior'), ('Pesquisador(a) - Graduação', 'Pesquisador(a) - Graduação'), ('Pesquisador(a) - Mestrado', 'Pesquisador(a) - Mestrado'), ('Pesquisador(a) - Doutorado', 'Pesquisador(a) - Doutorado'), ('Outro', 'Outro')], max_length=200, verbose_name='Tipo de pesquisador')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail do pesquisador')),
                ('github', models.CharField(max_length=200, verbose_name='Github do pesquisador')),
                ('linkedin', models.CharField(max_length=200, verbose_name='Linkedin do pesquisador')),
                ('texto', models.TextField(verbose_name='Texto sobre o pesquisador')),
                ('texto_ing', models.TextField(verbose_name='Texto sobre o pesquisador - Inglês')),
                ('texto_fra', models.TextField(verbose_name='Texto sobre o pesquisador - Francês')),
                ('img_pesquisador', models.ImageField(upload_to='fotos/', verbose_name='Imagem do pesquisador')),
            ],
        ),
    ]
