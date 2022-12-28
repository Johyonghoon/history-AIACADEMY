from django.urls import re_path as url

from exrc.dlearn.iris import view as view_iris

urlpatterns = [
    url(r'iris', view_iris.api)
]
