"""digitaljuries2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','juries.views.index'),
    url(r'^consent','juries.views.consent'),
    url(r'^survey_pre','juries.views.survey_pre'),
    url(r'^instructions','juries.views.instructions'),
    url(r'^control','juries.views.control'),
    url(r'^survey_control','juries.views.survey_control'),
    url(r'^scaleable','juries.views.scaleable'),
    url(r'^survey_scaleable','juries.views.survey_scaleable'),
    url(r'^immersive','juries.views.immersive'),
    url(r'^survey_immersive','juries.views.survey_immersive'),
    url(r'^survey_complete','juries.views.survey_complete'),
    url(r'^thankyou','juries.views.thankyou'),
]
