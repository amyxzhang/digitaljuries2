from django.contrib import admin
from juries.models import GroupInfo, UserInfo, ChatMessage, Case, Experiment

admin.site.register(GroupInfo)
admin.site.register(UserInfo)
admin.site.register(ChatMessage)
admin.site.register(Case)
admin.site.register(Experiment)