from django.shortcuts import render
from annoying.decorators import render_to


@render_to('juries/index.html')
def index(request):
    return {}

@render_to('juries/consent.html')
def consent(request):
    return {}

@render_to('juries/survey_demographics.html')
def survey_demographics(request):
    return {}

@render_to('juries/survey_morals.html')
def survey_morals(request):
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
