from django.contrib import admin
from juries.models import GroupInfo, UserInfo, ChatMessage

admin.site.register(GroupInfo)
admin.site.register(UserInfo)
admin.site.register(ChatMessage)