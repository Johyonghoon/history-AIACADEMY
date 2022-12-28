from django.urls import re_path as url

from exrc.webcrawler.naver_movie import view as view_navermovie

urlpatterns = [
    url(r'naver-movie', view_navermovie.api)
]
