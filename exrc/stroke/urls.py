from django.urls import re_path as url

from exrc.stroke import stroke_views

urlpatterns = [
    url(r'stroke', stroke_views.stroke)
]
