from django.urls import re_path as url
from exrc.auth import auth_views

urlpatterns = [
    url(r'auth', views.login)
]