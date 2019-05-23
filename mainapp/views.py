from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import EmailList, FanCounter

# Create your views here.
def index(request):
    fanNumber = FanCounter.objects.all()[0].count
    context = { 'fanCount': fanNumber }
    return render(request, 'mainapp/index.html', context)

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

def blog(request, blogName):
    try:
        blog = Blog.objects.get(title=blogName)
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')
    return HttpResponse("You're looking at blog %s" % blogName)
