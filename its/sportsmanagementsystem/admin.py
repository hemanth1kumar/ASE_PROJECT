from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Player,Sport,Coach,Complaint,Tournament,Schedule,Notification,Performance
admin.site.register(Player)
admin.site.register(Sport)
admin.site.register(Coach)
admin.site.register(Complaint)
admin.site.register(Tournament)
admin.site.register(Schedule)
admin.site.register(Notification)
admin.site.register(Performance)