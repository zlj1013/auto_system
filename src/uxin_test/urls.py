# -*- coding: utf-8 -*-
#import mysite
#import xadmin
from django.contrib import admin
from django.urls import path
from user.views import *
#from django.conf.urls import include, url

urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('xadmin/', xadmin.site.urls),    
    path("gologin/",gologin),
    path("dologin/",login),
    path("index/",index),
    path("logout/",logout),
    ]