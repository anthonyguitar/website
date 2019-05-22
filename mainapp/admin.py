from django.contrib import admin

# Register your models here.
from .models import EmailList, FanCounter

admin.site.register(EmailList)
admin.site.register(FanCounter)
