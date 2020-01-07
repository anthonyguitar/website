from django.contrib import admin

# Register your models here.
from .models import EmailList, FanCounter, MusicLink

admin.site.register(EmailList)
admin.site.register(FanCounter)
admin.site.register(MusicLink)
