from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class GroupInfo(models.Model):
    id = models.AutoField(primary_key=True)
    condition = models.IntegerField(default=0) # 1-4 (from the paper)
     
class UserInfo(models.Model):
 
    id = models.AutoField(primary_key=True)
    mturk_user = models.ForeignKey(User, null=True)
    
    groupinfo = models.ForeignKey(GroupInfo, null=True)
    
    
    age_range = models.TextField(null=True)
    gender = models.TextField(null=True)
    education = models.TextField(null=True)
    political = models.TextField(null=True)
    political_engage = models.TextField(null=True)
    
    moral0 = models.IntegerField(default=0) # Likert 1-5
    moral1 = models.IntegerField(default=0)
    moral2 = models.IntegerField(default=0)
    moral3 = models.IntegerField(default=0)
    moral4 = models.IntegerField(default=0)
    moral5 = models.IntegerField(default=0)
    
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
    scaleable_explanation = models.TextField(null=True)
    
    scaleable0 = models.IntegerField(default=0)
    scaleable1 = models.IntegerField(default=0)
    scaleable2 = models.IntegerField(default=0)
    scaleable3 = models.IntegerField(default=0)
    scaleable4 = models.IntegerField(default=0)
    scaleable5 = models.IntegerField(default=0)
    
    immersive_vote = models.FloatField(default=0.0)
    immersive_action_content = models.TextField(null=True)
    immersive_action_user = models.TextField(null=True)
    
    immersive0 = models.IntegerField(default=0)
    immersive1 = models.IntegerField(default=0)
    immersive2 = models.IntegerField(default=0)
    immersive3 = models.IntegerField(default=0)
    immersive4 = models.IntegerField(default=0)
    immersive5 = models.IntegerField(default=0)
    
    complete0 = models.TextField(null=True)
    complete1 = models.TextField(null=True)
    complete2 = models.TextField(null=True)
    complete3 = models.TextField(null=True)
    complete4 = models.TextField(null=True)
    complete5 = models.TextField(null=True)
    complete6 = models.TextField(null=True)
    complete7 = models.TextField(null=True)
    complete8 = models.TextField(null=True)
    complete9 = models.TextField(null=True)
    complete10 = models.TextField(null=True)
    complete11 = models.TextField(null=True)
    
    def __unicode__(self):
        return self.mturk_user.username
     

class ChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    
    user = models.ForeignKey(UserInfo, null=True)
    chat_username = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(GroupInfo, null=True)
    text = models.TextField(null=True)



    