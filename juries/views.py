from django.shortcuts import render
from annoying.decorators import render_to
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from juries.models import UserInfo, GroupInfo


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

def demographics_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get_or_create(mturk_user=user)
    ui = ui[0]
    
    ui.age_range = request.POST.get('age')
    ui.gender = request.POST.get('gender')
    ui.education = request.POST.get('education')
    ui.political = request.POST.get('political')
    ui.political_engage = request.POST.get('engagement')
    
    ui.save()
    
    return JsonResponse({})

def morals_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.morals0 = int(request.POST.get('mv1') if request.POST.get('mv1') != '' else '0')
    ui.morals1 = int(request.POST.get('mv2') if request.POST.get('mv2') != '' else '0')
    ui.morals2 = int(request.POST.get('mv3') if request.POST.get('mv3') != '' else '0')
    ui.morals3 = int(request.POST.get('mv4') if request.POST.get('mv4') != '' else '0')
    ui.morals4 = int(request.POST.get('mv5') if request.POST.get('mv5') != '' else '0')
    ui.morals5 = int(request.POST.get('mv6') if request.POST.get('mv6') != '' else '0')
    
    ui.save()
    
    return JsonResponse({})

def controlsurvey_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.control0 = int(request.POST.get('control1') if request.POST.get('control1') != '' else '0')
    ui.control1 = int(request.POST.get('control2') if request.POST.get('control2') != '' else '0')
    ui.control2 = int(request.POST.get('control3') if request.POST.get('control3') != '' else '0')
    ui.control3 = int(request.POST.get('control4') if request.POST.get('control4') != '' else '0')
    ui.control4 = int(request.POST.get('control5') if request.POST.get('control5') != '' else '0')
    ui.control5 = int(request.POST.get('control6') if request.POST.get('control6') != '' else '0')
    
    ui.save()
    
    if not ui.groupinfo:
    
        gcount = GroupInfo.objects.all().count()
        
        if gcount > 0:
            g = GroupInfo.objects.latest('id')
            num_users = UserInfo.objects.filter(groupinfo=g).count()
        else:
            g = GroupInfo.objects.create()
            g.condition = 1
            g.save()
            num_users = 0
        
        if num_users >= 6:
            g2 = GroupInfo.objects.create()
            if g.condition == 4:
                g2.condition = 1
            else:
                g2.condition = g.condition + 1
            g2.save()
        else:
            g2 = g
            
        ui.groupinfo = g2
        
        ui.save()
    else:
        g2 = ui.groupinfo
    
    if g2.condition == 1 or g2.condition == 2:
        return JsonResponse({'url': '/scaleable?group=' + str(g2.id) + '&condition=' + str(g2.condition)})
    else:
        return JsonResponse({'url': '/immersive?group=' + str(g2.id) + '&condition=' + str(g2.condition)})

def scaleable_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.scaleable_vote = float(request.POST.get('vote'))
    ui.scaleable_content_unlist = request.POST.get('unlist')
    ui.scaleable_content_delete = request.POST.get('del')
    ui.scaleable_content_report = request.POST.get('report')
    ui.scaleable_user_warn = request.POST.get('warn')
    ui.scaleable_user_ban = request.POST.get('ban')
    ui.scaleable_user_permaban = request.POST.get('permaban')
    ui.scaleable_explanation = request.POST.get('explanation')
    
    ui.save()
    
    return JsonResponse({})
    


def scaleablesurvey_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.scaleable0 = int(request.POST.get('scaleable1') if request.POST.get('scaleable1') != '' else '0')
    ui.scaleable1 = int(request.POST.get('scaleable2') if request.POST.get('scaleable2') != '' else '0')
    ui.scaleable2 = int(request.POST.get('scaleable3') if request.POST.get('scaleable3') != '' else '0')
    ui.scaleable3 = int(request.POST.get('scaleable4') if request.POST.get('scaleable4') != '' else '0')
    ui.scaleable4 = int(request.POST.get('scaleable5') if request.POST.get('scaleable5') != '' else '0')
    ui.scaleable5 = int(request.POST.get('scaleable6') if request.POST.get('scaleable6') != '' else '0')
    
    ui.save()
    
    g2 = ui.groupinfo
    
    if g2.condition == 3 or g2.condition == 4:
        return JsonResponse({'url': '/scaleable?group=' + str(g2.id) + '&condition=' + str(g2.condition)})
    else:
        return JsonResponse({'url': '/immersive?group=' + str(g2.id) + '&condition=' + str(g2.condition)})
    
    
    
def poll_scaleable(request):
    group_id = request.GET.get('group');
    
    gi = GroupInfo.objects.get(id=group_id)
    ui = UserInfo.objects.filter(groupinfo=gi, scaleable_vote__isnull=False)
    if ui.count() >= 6:
        
        vote = 0.0
        unlist = 0
        delete = 0
        report = 0
        warn = 0
        ban = 0
        permaban = 0
        
        for u in ui:
            vote += u.scaleable_vote
            if u.scaleable_content_unlist:
                unlist += 1
            if u.scaleable_content_delete:
                delete += 1
            if u.scaleable_content_report:
                report += 1
            if u.scaleable_user_warn:
                warn += 1
            if u.scaleable_user_ban:
                ban += 1
            if u.scaleable_user_permaban:
                permaban += 1
        
        vote = float(float(vote)/6.0)
        return JsonResponse({'count': ui.count(),
                             'vote': vote,
                             'unlist': unlist,
                             'del': delete,
                             'report': report,
                             'warn': warn,
                             'ban': ban,
                             'permaban': permaban})

    else:
        return JsonResponse({'count': ui.count()})
    

    


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
