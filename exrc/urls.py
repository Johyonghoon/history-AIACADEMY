from django.urls import re_path as url
from exrc import views

urlpatterns = [
    url(r'stroke', views.stroke),
    url(r'iris', views.iris)
]
