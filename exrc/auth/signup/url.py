from django.urls import re_path as url

from exrc.auth.signup import view as signup_views

urlpatterns = [
    url(r'signup', signup_views.api)
]