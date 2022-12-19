from django.urls import re_path as url

from exrc.dlearn.mnist import view as view_mnist

urlpatterns = [
    url(r'mnist', view_mnist.api)
]
