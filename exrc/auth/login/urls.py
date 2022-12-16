from django.urls import re_path as url

from exrc.auth.login import login_views

urlpatterns = [
    url(r'login', login_views.login)
]