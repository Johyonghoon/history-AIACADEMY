from django.urls import re_path as url

from exrc.auth.exrc_users import views

urlpatterns = [
    url(r'exrc_users', views.api)
]