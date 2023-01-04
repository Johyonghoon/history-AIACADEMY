from django.urls import re_path as url

from exrc.nlp.imdb import views

urlpatterns = [
    url(r'imdb', views.api)
]
