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
    
    url(r'^consent_post','juries.views.consent_post'),
    url(r'^demographics_post','juries.views.demographics_post'),
    url(r'^morals_post','juries.views.morals_post'),
    url(r'^controlsurvey_post','juries.views.controlsurvey_post'),
    
    url(r'^scaleable_post','juries.views.scaleable_post'),
    url(r'^immersive_post','juries.views.immersive_post'),
    
    url(r'^scaleablesurvey_post','juries.views.scaleablesurvey_post'),
    url(r'^immersivesurvey_post','juries.views.immersivesurvey_post'),
    url(r'^completesurvey_post','juries.views.completesurvey_post'),
    
    
        
    url(r'^post_immersive_vote','juries.views.post_immersive_vote'),
    url(r'^post_immersive_action','juries.views.post_immersive_action'),
    
    url(r'^chat_username','juries.views.chat_username'),
    url(r'^post_chat_message','juries.views.post_chat_message'),
    url(r'^get_chat_messages','juries.views.get_chat_messages'),
    
    url(r'^poll_chat','juries.views.poll_chat'),
    
    url(r'^poll_immersive','juries.views.poll_immersive'),
    url(r'^poll_scaleable','juries.views.poll_scaleable'),
    
    url(r'^consent','juries.views.consent'),
    url(r'^survey_demographics','juries.views.survey_demographics'),
    url(r'^survey_morals','juries.views.survey_morals'),
    url(r'^instructions','juries.views.instructions'),
    url(r'^control','juries.views.control'),
    url(r'^survey_control','juries.views.survey_control'),
    url(r'^scaleable','juries.views.scaleable'),
    url(r'^survey_scaleable','juries.views.survey_scaleable'),
    url(r'^immersive','juries.views.immersive'),
    url(r'^survey_immersive','juries.views.survey_immersive'),
    url(r'^survey_complete','juries.views.survey_complete'),
    url(r'^thankyou','juries.views.thankyou'),
    
    url(r'^tracking/', include('tracking.urls')),
    
    
]
