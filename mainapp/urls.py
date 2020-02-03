from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('musictheory_one', views.musictheory_one, name='musictheory_one'),
    path('musictheory_two', views.musictheory_two, name='musictheory_two'),
    path('robots.txt', TemplateView.as_view(template_name='mainapp/robots.txt', content_type='text/plain'), name='robots'),
    path('sitemap.txt', TemplateView.as_view(template_name='mainapp/sitemap.txt', content_type='text/plain'), name='sitemap'),
    path('createFan', views.createFan, name='createFan'),
    path('submissions', views.submissions, name='submissions'),
    #path('videos', views.videos, name='videos'),
    #path('blogs', views.blogs, name='blogs'),
    #path('blogs/<str:url>', views.blogs, name='blogs'),
    #path('tabs', views.tabs, name='tabs'),
    #path('tabs/<str:url>', views.tabs, name='tabs'),
]
