from django.urls import re_path as url
from exrc.dlearn.fashion import view as view_fashion

urlpatterns = [
    url(r'fashion', view_fashion.api),
]
