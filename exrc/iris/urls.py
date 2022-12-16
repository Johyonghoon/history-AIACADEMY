from django.urls import re_path as url

from exrc.iris import iris_views

urlpatterns = [
    url(r'iris', iris_views.iris)
]
