from django.urls import re_path as url
from exrc.login import views

urlpatterns = [
    url(r'login', views.login)
]