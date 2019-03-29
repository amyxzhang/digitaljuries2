from django.shortcuts import render
from annoying.decorators import render_to
from django.http import JsonResponse

import random

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from juries.models import UserInfo, GroupInfo, ChatMessage, Case

CASES = ['pepe','christchurch','momo']


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
    ui.confidence = request.POST.get('confidence1')
    
    ui.save()
    
    return JsonResponse({})

def morals_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)

    ui.moral0 = int(request.POST.get('mv1') if request.POST.get('mv1') else '0')
    ui.moral1 = int(request.POST.get('mv2') if request.POST.get('mv2') else '0')
    ui.moral2 = int(request.POST.get('mv3') if request.POST.get('mv3') else '0')
    ui.moral3 = int(request.POST.get('mv4') if request.POST.get('mv4') else '0')
    ui.moral4 = int(request.POST.get('mv5') if request.POST.get('mv5') else '0')
    ui.moral5 = int(request.POST.get('mv6') if request.POST.get('mv6') else '0')
    
    ui.save()
    
    return JsonResponse({})

def controlsurvey_post(request):
    turk_id = request.POST.get('id')
    round = int(request.POST.get('round'))
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.control_difficulty = int(request.POST.get('control_difficulty') if request.POST.get('control_difficulty') else '0')
    ui.control_time = int(request.POST.get('control_time') if request.POST.get('control_time') else '0')
    ui.control_satisfaction = int(request.POST.get('control_satisfaction') if request.POST.get('control_satisfaction') else '0')
    
    
    ui.control0 = int(request.POST.get('control1') if request.POST.get('control1') else '0')
    ui.control1 = int(request.POST.get('control2') if request.POST.get('control2') else '0')
    ui.control2 = int(request.POST.get('control3') if request.POST.get('control3') else '0')
    ui.control3 = int(request.POST.get('control4') if request.POST.get('control4') else '0')
    ui.control4 = int(request.POST.get('control5') if request.POST.get('control5') else '0')
    ui.control5 = int(request.POST.get('control6') if request.POST.get('control6') else '0')
    
    ui.save()
    g2 = ui.groupinfo
    
    next_round = None
    next_case = None
    next_round_num = None
    if round == 1:
        next_round = g2.round2
        next_case = g2.case2
        next_round_num = 2
    elif round == 2:
        next_round = g2.round3
        next_case = g2.case3
        next_round_num = 3
        
    if next_round:
        if next_round == "No Jury":
            return JsonResponse({'url': '/control?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name})
        elif next_round == "Blind Voting":
            return JsonResponse({'url': '/scaleable?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
        elif next_round == "Deliberating":
            return JsonResponse({'url': '/immersive?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
    else:
        return JsonResponse({'url': '/survey_complete?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id)})
    

def scaleable_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.scaleable_vote = float(request.POST.get('vote'))
    ui.scaleable_content_unlist = (request.POST.get('unlist') == "true")
    ui.scaleable_content_delete = (request.POST.get('del')  == "true")
    ui.scaleable_content_report = (request.POST.get('report')  == "true")
    ui.scaleable_user_warn = (request.POST.get('warn')  == "true")
    ui.scaleable_user_ban = (request.POST.get('ban') == "true")
    ui.scaleable_user_permaban = (request.POST.get('permaban') == "true")
#     ui.scaleable_explanation = request.POST.get('explanation')
    
    ui.save()
    
    return JsonResponse({})
   
def immersive_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.immersive_vote = float(request.POST.get('vote'))
    ui.immersive_content_unlist = (request.POST.get('unlist') == "true")
    ui.immersive_content_delete = (request.POST.get('del')  == "true")
    ui.immersive_content_report = (request.POST.get('report')  == "true")
    ui.immersive_user_warn = (request.POST.get('warn')  == "true")
    ui.immersive_user_ban = (request.POST.get('ban') == "true")
    ui.immersive_user_permaban = (request.POST.get('permaban') == "true")

    ui.save()
    
    return JsonResponse({})
     


def scaleablesurvey_post(request):
    turk_id = request.POST.get('id')
    round = int(request.POST.get('round'))
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.scaleable_justification = request.POST.get('scaleable_justification')
    ui.scaleable_difficulty = int(request.POST.get('scaleable_difficulty') if request.POST.get('scaleable_difficulty')  else '0')
    ui.scaleable_time = int(request.POST.get('scaleable_time') if request.POST.get('scaleable_time') else '0')
    ui.scaleable_satisfaction = int(request.POST.get('scaleable_satisfaction') if request.POST.get('scaleable_satisfaction')  else '0')
    
    ui.scaleable0 = int(request.POST.get('scaleable1') if request.POST.get('scaleable1') else '0')
    ui.scaleable1 = int(request.POST.get('scaleable2') if request.POST.get('scaleable2') else '0')
    ui.scaleable2 = int(request.POST.get('scaleable3') if request.POST.get('scaleable3')  else '0')
    ui.scaleable3 = int(request.POST.get('scaleable4') if request.POST.get('scaleable4')  else '0')
    ui.scaleable4 = int(request.POST.get('scaleable5') if request.POST.get('scaleable5')  else '0')
    ui.scaleable5 = int(request.POST.get('scaleable6') if request.POST.get('scaleable6')  else '0')
    
    ui.save()
    
    g2 = ui.groupinfo
    
    
    next_round = None
    next_case = None
    next_round_num = None
    if round == 1:
        next_round = g2.round2
        next_case = g2.case2
        next_round_num = 2
    elif round == 2:
        next_round = g2.round3
        next_case = g2.case3
        next_round_num = 3
        
    if next_round:
        if next_round == "No Jury":
            return JsonResponse({'url': '/control?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name})
        elif next_round == "Blind Voting":
            return JsonResponse({'url': '/scaleable?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
        elif next_round == "Deliberating":
            return JsonResponse({'url': '/immersive?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
    else:
        return JsonResponse({'url': '/survey_complete?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id)})
 

 
def immersivesurvey_post(request):
    turk_id = request.POST.get('id')
    round = int(request.POST.get('round'))
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.immersive_justification = request.POST.get('immersive_justification')
    ui.immersive_difficulty = int(request.POST.get('immersive_difficulty') if request.POST.get('immersive_difficulty') else '0')
    ui.immersive_time = int(request.POST.get('immersive_time') if request.POST.get('immersive_time') != '' else '0')
    ui.immersive_satisfaction = int(request.POST.get('immersive_satisfaction') if request.POST.get('immersive_satisfaction')else '0')
    ui.immersive_convo = int(request.POST.get('immersive_convo') if request.POST.get('immersive_convo') else '0')
    ui.immersive_trust = int(request.POST.get('immersive_trust') if request.POST.get('immersive_trust')  else '0')
    
    ui.immersive0 = int(request.POST.get('immersive1') if request.POST.get('immersive1') else '0')
    ui.immersive1 = int(request.POST.get('immersive2') if request.POST.get('immersive2')  else '0')
    ui.immersive2 = int(request.POST.get('immersive3') if request.POST.get('immersive3')  else '0')
    ui.immersive3 = int(request.POST.get('immersive4') if request.POST.get('immersive4') else '0')
    ui.immersive4 = int(request.POST.get('immersive5') if request.POST.get('immersive5') else '0')
    ui.immersive5 = int(request.POST.get('immersive6') if request.POST.get('immersive6') else '0')
    
    ui.save()
    
    g2 = ui.groupinfo
    
     
    next_round = None
    next_case = None
    next_round_num = None
    if round == 1:
        next_round = g2.round2
        next_case = g2.case2
        next_round_num = 2
    elif round == 2:
        next_round = g2.round3
        next_case = g2.case3
        next_round_num = 3
        
    if next_round:
        if next_round == "No Jury":
            return JsonResponse({'url': '/control?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name})
        elif next_round == "Blind Voting":
            return JsonResponse({'url': '/scaleable?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
        elif next_round == "Deliberating":
            return JsonResponse({'url': '/immersive?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=' + str(next_round_num) + '&case=' + next_case.name })
    else:
        return JsonResponse({'url': '/survey_complete?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id)})
 

    

def completesurvey_post(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    ui.complete0 = request.POST.get('mv1')
    ui.complete1 = request.POST.get('mv2')
    ui.complete2 = request.POST.get('mv3')
    ui.complete3 = request.POST.get('mv4')
    ui.complete4 = request.POST.get('mv5')
    ui.complete5 = request.POST.get('mv6')
    ui.complete6 = request.POST.get('mv7')
    ui.complete7 = request.POST.get('mv8')
    ui.complete8 = request.POST.get('mv9')
    ui.complete9 = request.POST.get('mv10')
    ui.complete10 = request.POST.get('mv11')
    ui.complete11 = request.POST.get('mv12')
    
    
    ui.save()
    return JsonResponse({})



    
    
def chat_username(request):
    turk_id = request.POST.get('id');
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    ui.chat_username = request.POST.get('username');
    
    ui.save()
    
    return JsonResponse({})
    
def post_chat_message(request):
    turk_id = request.POST.get('id')
    
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    c = ChatMessage.objects.create(user=ui, 
                                   group=ui.groupinfo, 
                                   text=request.POST.get('message'))
    
    return JsonResponse({'id': c.id})
    
def get_chat_messages(request):
    group_id = request.GET.get('group');
    
    g = GroupInfo.objects.get(id=int(group_id))
    c = ChatMessage.objects.filter(group=g)
    
    res = {'messages': []}
    
    for i in c:
        d = {'username': i.user.chat_username,
             'message': i.text,
             'id': i.id}

        res['messages'].append(d)
    
    return JsonResponse(res)

def poll_chat(request):
    group_id = request.GET.get('group');
    last_m = request.GET.get('last_m');
    last_id = int(last_m.split('_')[1])
    
    g = GroupInfo.objects.get(id=int(group_id))
    c = ChatMessage.objects.filter(group=g, id__gt=last_id)
    
    res = {'messages': []}
    
    for i in c:
        d = {'username': i.user.chat_username,
             'message': i.text,
             'id': i.id}

        res['messages'].append(d)
    
    return JsonResponse(res)


def post_immersive_vote(request):
    turk_id = request.POST.get('id')
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    vote = request.POST.get('vote')
    
    ui.immersive_vote = float(vote)
    
    ui.save()
    
    return JsonResponse({})
    

def post_immersive_action(request):
    turk_id = request.POST.get('id')
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    check = request.POST.get('check')
    action = request.POST.get('action')
    if action == "unlist":
        ui.immersive_content_unlist = (check=="true")
    elif action == "delete":
        ui.immersive_content_delete = (check=="true")
    elif action == "report":
        ui.immersive_content_report = (check=="true")
    elif action == "warn":
        ui.immersive_user_warn = (check=="true")
    elif action == "ban":
        ui.immersive_user_ban = (check=="true")
    elif action == "permaban":
        ui.immersive_user_permaban = (check=="true")
    
    ui.save()
    return JsonResponse({})
    
def poll_immersive(request):
    group_id = request.GET.get('group');
    
    gi = GroupInfo.objects.get(id=group_id)
    ui = UserInfo.objects.filter(groupinfo=gi, immersive_vote__isnull=False)

    user_votes = {}
    vote = 0.0
    unlist = 0
    delete = 0
    report = 0
    warn = 0
    ban = 0
    permaban = 0
    
    for u in ui:
        user_votes[u.chat_username] = u.immersive_vote
        vote += u.immersive_vote
        if u.immersive_content_unlist:
            unlist += 1
        if u.immersive_content_delete:
            delete += 1
        if u.immersive_content_report:
            report += 1
        if u.immersive_user_warn:
            warn += 1
        if u.immersive_user_ban:
            ban += 1
        if u.immersive_user_permaban:
            permaban += 1
    
    vote = float(float(vote)/float(ui.count()))
    return JsonResponse({'count': ui.count(),
                         'vote': vote,
                         'unlist': unlist,
                         'del': delete,
                         'report': report,
                         'warn': warn,
                         'ban': ban,
                         'permaban': permaban,
                         'user_votes': user_votes})

    

    
def poll_scaleable(request):
    group_id = request.GET.get('group');
    jury = int(request.GET.get('jury'));
    
    gi = GroupInfo.objects.get(id=group_id)
    ui = UserInfo.objects.filter(groupinfo=gi, scaleable_vote__isnull=False)
    if ui.count() >= jury:
        
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
        
        vote = float(float(vote)/float(jury))
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
    
    turk_id = request.GET.get('id')
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    if not ui.groupinfo:
    
        gcount = GroupInfo.objects.all().count()
        
        if gcount > 0:
            g = GroupInfo.objects.latest('id')
            num_users = UserInfo.objects.filter(groupinfo=g).count()
        else:
            g = GroupInfo.objects.create()
            g.round1 = "No Jury" # can be "No Jury", "Blind Voting", "Deliberating"
            g.round2 = "Blind Voting"
            g.round3 = "Deliberating"
            
            random.shuffle(CASES) 
            g.case1 = Case.objects.get(name=CASES[0])
            g.case2 = Case.objects.get(name=CASES[1])
            g.case3 = Case.objects.get(name=CASES[2])   
            
            g.save()
            num_users = 0
        
        if num_users >= 6:
            g2 = GroupInfo.objects.create()
            
            id = g2.id
            
            rem = id % 6
            if rem == 0:
                g2.round1 = "Deliberating"
                g2.round2 = "Blind Voting"
                g2.round3 = "No Jury"
            elif rem == 1:
                g2.round1 = "No Jury"
                g2.round2 = "Blind Voting"
                g2.round3 = "Deliberating"
            elif rem == 2:
                g2.round1 = "No Jury"
                g2.round2 = "Deliberating"
                g2.round3 = "Blind Voting"
            elif rem == 3:
                g2.round1 = "Blind Voting"
                g2.round2 = "No Jury"
                g2.round3 = "Deliberating"
            elif rem == 4:
                g2.round1 = "Blind Voting"
                g2.round2 = "Deliberating"
                g2.round3 = "No Jury"
            elif rem == 5:
                g2.round1 = "Deliberating"
                g2.round2 = "No Jury"
                g2.round3 = "Blind Voting"

            #1 = ABC, 2 = ACB, 3 = BAC, 4 = BCA, 5 = CAB, 6 = CBA
            
            random.shuffle(CASES) 
            g2.case1 = Case.objects.get(name=CASES[0])
            g2.case2 = Case.objects.get(name=CASES[1])
            g2.case3 = Case.objects.get(name=CASES[2])   
            
            g2.save()
        else:
            g2 = g
            
        ui.groupinfo = g2
        
        ui.save()
    else:
        g2 = ui.groupinfo

    if g2.round1 == "No Jury":
        return {'url': '/control?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=1&case=' + g2.case1.name}
    elif g2.round1 == "Blind Voting":
        return {'url': '/scaleable?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=1&case=' + g2.case1.name }
    elif g2.round1 == "No Jury":
        return {'url': '/immersive?id=' + str(ui.mturk_user.username) + '&group=' + str(g2.id) + '&round=1&case=' + g2.case1.name }

@render_to('juries/control.html')
def control(request):
    case = request.GET.get('case')
    c = Case.objects.get(name=case)
    return {'case': c}

@render_to('juries/survey_control.html')
def survey_control(request):
    return {}

@render_to('juries/scaleable.html')
def scaleable(request):
    turk_id = request.GET.get('id')
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    case = request.GET.get('case')
    c = Case.objects.get(name=case)
    
    if ui.scaleable_vote:
        return {'voted': True, 'case': c}
    else:
        return {'voted': False, 'case': c}

@render_to('juries/survey_scaleable.html')
def survey_scaleable(request):
    return {}

@render_to('juries/immersive.html')
def immersive(request):
    turk_id = request.GET.get('id')
    user = User.objects.get(username=turk_id)
    ui = UserInfo.objects.get(mturk_user=user)
    
    case = request.GET.get('case')
    c = Case.objects.get(name=case)
    
    if ui.immersive_vote:
        return {'voted': True,
                'ui': ui,
                'case': c}
    else:
        return {'voted': False,
                'ui': ui,
                'case': c}
    
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
