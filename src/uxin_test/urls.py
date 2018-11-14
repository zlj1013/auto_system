# -*- coding: utf-8 -*-
#import mysite
import xadmin
from django.urls import path
#from django.conf.urls import include, url

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    ]