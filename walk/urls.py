#!/usr/bin/python3

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from walk.views import PostListView, PublicListView

urlpatterns = [
    path('', PostListView.as_view(template_name="home.html"),name="home"),
    path('walk/public', PublicListView.as_view(template_name="public.html"),name="public"),
    
    #path('', include('accounts.urls')),

] 
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
