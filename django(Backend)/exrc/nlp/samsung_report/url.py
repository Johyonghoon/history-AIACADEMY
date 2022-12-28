from django.urls import re_path as url

from exrc.nlp.samsung_report import views

urlpatterns = [
    url(r'samsung-report', views.api)
]
