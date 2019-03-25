from django.shortcuts import render
from annoying.decorators import render_to
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



@render_to('juries/index.html')
def index(request):
    return {}

@render_to('juries/consent.html')
def consent(request):
    return {}

def consent_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.filter(username=turk_id)
    if user.exists():
        user = user[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    else:
        user = User.objects.get_or_create(username=turk_id, password=turk_id)
        user = user[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    
    return JsonResponse({})

@render_to('juries/survey_pre.html')
def survey_pre(request):
    return {}

@render_to('juries/instructions.html')
def instructions(request):
    return {}

@render_to('juries/control.html')
def control(request):
    return {}

@render_to('juries/survey_control.html')
def survey_control(request):
    return {}

@render_to('juries/scaleable.html')
def scaleable(request):
    return {}

@render_to('juries/survey_scaleable.html')
def survey_scaleable(request):
    return {}

@render_to('juries/immersive.html')
def immersive(request):
    return {}

@render_to('juries/survey_immersive.html')
def survey_immersive(request):
    return {}

@render_to('juries/survey_complete.html')
def survey_complete(request):
    return {}

@render_to('juries/thankyou.html')
def thankyou(request):
    return {}