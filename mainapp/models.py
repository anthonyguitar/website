from django.db import models

# Create your models here.
class EmailList(models.Model):
    email = models.EmailField(max_length=200, default='notset', unique=True)
    fanNumber = models.IntegerField(default=0)

    def __repr__(self):
        return self.email
    def __str__(self):
        return self.email

class FanCounter(models.Model):
    name = models.CharField(default='fanCount', max_length=200)
    count = models.IntegerField(default=0)

    def __repr__(self):
        return str(self.count)
    def __str__(self):
        return str(self.count)
