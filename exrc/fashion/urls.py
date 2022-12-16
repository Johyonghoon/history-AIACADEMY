from django.urls import re_path as url
from exrc.fashion import fashion_views

urlpatterns = [
    url(r'fashion', fashion_views.fashion),
    # url(r'fashion/(?P<test_num>)$', fashion_views.fashion),
]
