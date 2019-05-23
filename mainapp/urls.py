from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', TemplateView.as_view(template_name='mainapp/robots.txt', content_type='text/plain'), name='robots'),
    path('sitemap.txt', TemplateView.as_view(template_name='mainapp/sitemap.txt', content_type='text/plain'), name='sitemap'),
    path('createFan', views.createFan, name='createFan'),
    path('blog/<str:blogName>', views.blog, name='blog'),
]
