from django.urls import path

from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('createFan', views.createFan, name='createFan'),
    path('blog/<str:blogName>', views.blog, name='blog'),
]
