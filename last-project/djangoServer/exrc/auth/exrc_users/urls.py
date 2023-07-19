from django.urls import re_path as url

from exrc.auth.exrc_users import views

urlpatterns = [
    url(r'exrc-users', views.create_dummy_accounts),
    url(r'list$', views.user_list),
    url(r'list/name', views.user_list_by_name),
    url(r'login', views.login),
]
