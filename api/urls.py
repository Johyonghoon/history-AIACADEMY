"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import hello

urlpatterns = [
    path("", hello),
    path("exrc/auth/", include('exrc.auth.login.url')),
    path("exrc/auth/", include('exrc.auth.exrc_users.url')),
    path("exrc/", include('exrc.stroke.url')),
    path("exrc/dlearn/", include('exrc.dlearn.iris.url')),
    path("exrc/dlearn/", include('exrc.dlearn.fashion.url')),
    path("exrc/dlearn/", include('exrc.dlearn.mnist.url')),
    path("exrc/", include('exrc.webcrawler.naver_movie.url')),
    path("exrc/nlp/", include('exrc.nlp.samsung_report.url')),
]
