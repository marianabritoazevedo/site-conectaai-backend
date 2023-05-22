from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-english', views.index_ing, name='index_ing'),
    path('index-francais', views.index_fra, name='index_fra'),
]