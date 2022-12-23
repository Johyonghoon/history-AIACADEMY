from django.urls import re_path as url

from exrc.auth.exrc_users import view as exrc_users_views

urlpatterns = [
    url(r'users', exrc_users_views.api)
]