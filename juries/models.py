from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Experiment(models.Model):
    active = models.BooleanField(default=True)

class Case(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True) # can be "pepe", "christchurch", "momo"
    context = models.TextField(null=True)
    violations = models.TextField(null=True)
    image = models.TextField(null=True)
    
    decision_score = models.FloatField(default=None, null=True)
    decision_content_action = models.TextField(null=True)
    decision_user_action = models.TextField(null=True)
    decision_justification = models.TextField(null=True)
    
    def __unicode__(self):
        return self.name
     
    

class GroupInfo(models.Model):
    id = models.AutoField(primary_key=True)
    round1 = models.TextField(null=True) # can be "No Jury", "Blind Voting", "Deliberating"
    round2 = models.TextField(null=True)
    round3 = models.TextField(null=True)
    
    #1 = ABC, 2 = ACB, 3 = BAC, 4 = BCA, 5 = CAB, 6 = CBA
    
    case1 = models.ForeignKey(Case, null=True, related_name="case1") 
    case2 = models.ForeignKey(Case, null=True, related_name="case2")
    case3 = models.ForeignKey(Case, null=True, related_name="case3")
    
    def __unicode__(self):
        return str(id) + ': 1-' + self.round1 + ' 2-' + self.round2 + ' 3-' + self.round3
     
class UserInfo(models.Model):
 
    id = models.AutoField(primary_key=True)
    mturk_user = models.ForeignKey(User, null=True)
    
    groupinfo = models.ForeignKey(GroupInfo, null=True)
    
    chat_username = models.TextField(null=True)
    
    age_range = models.TextField(null=True)
    gender = models.TextField(null=True)
    education = models.TextField(null=True)
    political = models.TextField(null=True)
    political_engage = models.TextField(null=True)
    confidence = models.TextField(null=True)
    
    moral0 = models.IntegerField(default=0) # Likert 1-5
    moral1 = models.IntegerField(default=0)
    moral2 = models.IntegerField(default=0)
    moral3 = models.IntegerField(default=0)
    moral4 = models.IntegerField(default=0)
    moral5 = models.IntegerField(default=0)
    
    
    control_difficulty = models.IntegerField(default=0)
    control_time = models.IntegerField(default=0)
    control_satisfaction = models.IntegerField(default=0)
    
    control0 = models.IntegerField(default=0)
    control1 = models.IntegerField(default=0)
    control2 = models.IntegerField(default=0)
    control3 = models.IntegerField(default=0)
    control4 = models.IntegerField(default=0)
    control5 = models.IntegerField(default=0)
    
    scaleable_vote = models.FloatField(default=None, null=True)
    scaleable_content_unlist = models.BooleanField(default=False)
    scaleable_content_delete = models.BooleanField(default=False)
    scaleable_content_report = models.BooleanField(default=False)
    scaleable_user_warn = models.BooleanField(default=False)
    scaleable_user_ban = models.BooleanField(default=False)
    scaleable_user_permaban = models.BooleanField(default=False)
    
    scaleable_justification = models.TextField(null=True)
    scaleable_difficulty = models.IntegerField(default=0)
    scaleable_time = models.IntegerField(default=0)
    scaleable_satisfaction = models.IntegerField(default=0)
    
    scaleable0 = models.IntegerField(default=0)
    scaleable1 = models.IntegerField(default=0)
    scaleable2 = models.IntegerField(default=0)
    scaleable3 = models.IntegerField(default=0)
    scaleable4 = models.IntegerField(default=0)
    scaleable5 = models.IntegerField(default=0)
    
    immersive_vote = models.FloatField(default=None, null=True)
    immersive_content_unlist = models.BooleanField(default=False)
    immersive_content_delete = models.BooleanField(default=False)
    immersive_content_report = models.BooleanField(default=False)
    immersive_user_warn = models.BooleanField(default=False)
    immersive_user_ban = models.BooleanField(default=False)
    immersive_user_permaban = models.BooleanField(default=False)
    
    immersive_justification = models.TextField(null=True)
    immersive_difficulty = models.IntegerField(default=0)
    immersive_time = models.IntegerField(default=0)
    immersive_satisfaction = models.IntegerField(default=0)
    immersive_convo = models.IntegerField(default=0)
    immersive_trust = models.IntegerField(default=0)
    
    immersive0 = models.IntegerField(default=0)
    immersive1 = models.IntegerField(default=0)
    immersive2 = models.IntegerField(default=0)
    immersive3 = models.IntegerField(default=0)
    immersive4 = models.IntegerField(default=0)
    immersive5 = models.IntegerField(default=0)
    

    complete_pref = models.TextField(null=True)
    complete_prefwhy = models.TextField(null=True)
    complete_nonpref = models.TextField(null=True)
    complete_nonprefwhy = models.TextField(null=True)

    complete_participate0 = models.BooleanField(default=False)
    complete_participate1 = models.BooleanField(default=False)
    complete_participate2 = models.BooleanField(default=False)
    complete_participate3 = models.BooleanField(default=False)
    complete_participate4 = models.BooleanField(default=False)
    
    complete_enf_rec = models.IntegerField(default=0)
    complete_enf_enf = models.IntegerField(default=0)
    complete_enf_why = models.TextField(null=True)

    complete3 = models.IntegerField(default=0)
    complete_confidence = models.IntegerField(default=0)
    complete_familiarity = models.IntegerField(default=0)
    complete_comments = models.TextField(null=True)
    email = models.TextField(null=True)

    def __unicode__(self):
        return self.mturk_user.username
     

class ChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    
    user = models.ForeignKey(UserInfo, null=True)
    
    datetime = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(GroupInfo, null=True)
    text = models.TextField(null=True)



    