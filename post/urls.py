from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^create/$',"post.views.posts_create"),
    url(r'^(?P<id>\d+)/$',"post.views.posts_detail",name='detail'),
    url(r'^$',"post.views.posts_list",name='list'),
    #url(r'^update/$',"post.views.posts_update"),
    url(r'^(?P<id>\d+)/delete/$',"post.views.posts_delete"),
    url(r'^(?P<id>\d+)/edit/$',"post.views.posts_update",name='update'),	
    
]
