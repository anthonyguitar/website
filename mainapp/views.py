from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import EmailList, FanCounter, Artist, Blog
import random
from random import randint as r
import datetime

# Create your views here.
def index(request):
    dt = datetime.datetime.today() 
    dtInt = dt.year*10000 + dt.month*100 + dt.day
    random.seed(dtInt)
    artistIndex = r(0, Artist.objects.count() - 1)
    #artistIndex = 0
    fanNumber = FanCounter.objects.all()[0].count
    context = { 'fanCount': fanNumber, 'artist': Artist.objects.all()[artistIndex] }
    return render(request, 'mainapp/index.html', context)

def test(request):
    dt = datetime.datetime.today() 
    dtInt = dt.year*10000 + dt.month*100 + dt.day
    random.seed(dtInt)
    artistIndex = r(0, Artist.objects.count() - 1)
    #artistIndex = 0
    fanNumber = FanCounter.objects.all()[0].count
    context = { 'fanCount': fanNumber, 'artist': Artist.objects.all()[artistIndex] }
    return render(request, 'mainapp/homepage.html', context)

def videos(request):
    context = {}
    return render(request, 'mainapp/videos.html', context)

def robots(request):
    return(request, 'mainapp/robots.txt')

def createFan(request):

    # grab email from signup form
    email = request.POST.get('email')

    # if the email already exists let them know
    if EmailList.objects.filter(email=email).exists():
        context = { 'status': '*Email address is already registered.' }
        return JsonResponse(context)

    try:

        # incremement fan counter
        f = FanCounter.objects.all()[0]
        f.count += 1
        f.save()

        # create new fan object
        e = EmailList()
        e.email = email
        e.fanNumber = f.count
        e.save()

        # return success
        context = { 'status': 'success', 'count': e.fanNumber }
        return JsonResponse(context)

    except Exception as e:
        context = { 'status':  str(e) }
        return JsonResponse(context)

def blog(request, url):
    try:
        blog = Blog.objects.get(url=url)
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')
    context = { 'blog': blog }
    return render(request, 'mainapp/blog.html', context)
