from django.urls import re_path as url

from exrc.auth.login import views

urlpatterns = [
    url(r'login', views.login),
]