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

class Artist(models.Model):
    name = models.CharField(default='', max_length=256)
    genre = models.CharField(default='', max_length=256)
    location = models.CharField(default='', max_length=256)
    socialLink = models.CharField(default='', max_length=256)
    favoriteTrack = models.CharField(default='', max_length=256)
    description = models.CharField(default='', max_length=256)
    imageLink = models.CharField(default='', max_length=256)

class Blog(models.Model):
    url = models.CharField(default='', max_length=256, unique=True)
    title = models.CharField(default='', max_length=256, unique=True)
    content = models.CharField(default='', max_length=3000)

class Tab(models.Model):
    url = models.CharField(default='', max_length=256, unique=True)
    filename = models.CharField(default='', max_length=256, unique=True)
    title = models.CharField(default='', max_length=256, unique=True)
    description = models.CharField(default='', max_length=3000)
    videoLink = models.CharField(default='', max_length=256, unique=True)
