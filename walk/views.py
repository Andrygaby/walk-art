from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from walk.models import Post as walk
from acounts.models import Post as show

class PostListView(ListView):
    template_name = 'home.html'
    model = walk
    context_object_name = 'posts'
    ordering = ['-created']
 
class PublicListView(ListView):
    template_name = 'public.html'
    model = show
    context_object_name = 'publics'
    ordering = ['-date_posted']
    
