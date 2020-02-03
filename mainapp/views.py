from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import EmailList, FanCounter, Artist, Blog, Tab, MusicLink
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
    context = { 'fanCount': fanNumber, 'artist': Artist.objects.all()[artistIndex],
                'title': 'Anthony Meyer Guitar'}
    return render(request, 'mainapp/homepage.html', context)

def musictheory_one(request):
    context = { 'title': 'What is Music Theory?' }
    return render(request, 'mainapp/musictheory_one.html', context)

def musictheory_two(request):
    context = { 'title': 'How do I Choose Which Notes to Play?' }
    return render(request, 'mainapp/musictheory_two.html', context)

'''
def tabs(request, url='None'):
    # try to grab a tab object
    context = {'validPage': False }
    if Tab.objects.filter(url=url).exists():
        t = Tab.objects.get(url=url)
        context['validPage'] = True
        context['tab'] = t
    else:
        tabs = Tab.objects.all()
        context['tabs'] = tabs
    return render(request, 'mainapp/tabs.html', context)
'''  
'''
def videos(request):
    context = { 'title': 'Anthony Meyer Videos' }
    return render(request, 'mainapp/videos.html', context)

def blogs(request, url='none'):
    if Blog.objects.filter(url=url).exists():
        blog = Blog.objects.get(url=url)
        context = { 'blog': blog }
        return render(request, 'mainapp/blogs.html', context)
    return render(request, 'mainapp/blogs.html')
'''
def robots(request):
    return(request, 'mainapp/robots.txt')

def submissions(request):
    if request.method == 'POST':
        context = {'status': 'success', 'title': 'Music Submissions'}
        email = request.POST.get('email')
        link = request.POST.get('link')
        ml = MusicLink()
        ml.email = email
        ml.link = link
        ml.save()
        return JsonResponse(context)
    return render(request, 'mainapp/submissions.html', {'title': 'Music Submissions'})

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

