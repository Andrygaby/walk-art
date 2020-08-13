from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin,FormView
from django.views.generic import View, TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, OuterRef, Subquery
from acounts.models import Post,Profile
from acounts.forms import ProfileEditForm, SearchPostForm, SearchUserForm, SpeedPostForm, InboxForm

from django.contrib import messages
from acounts.forms import AddCommentForm
from acounts.models import Post

#===============================================================================
class ProfileView(LoginRequiredMixin, TemplateView,FormView):
    login_url = '/accounts/login'
    redirect_field_name = 'profile'
    
    template_name = 'accounts/profile.html'
    form_class = SearchPostForm
    #form_class = SearchUserForm
    
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date_posted')[:5]
        context['users'] = User.objects.all()
        context['u_form'] = SearchUserForm()
        context['post_form'] = SpeedPostForm()
        
        context['now'] = timezone.now()
        return context
        
    def form_valid(self, post_form):
        post_form.instance.user = self.request.user
        return super().form_valid(post_form)  
    """
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
    """
    
#===============================================================================  
class ProfileEditView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = 'profile'
    
    model = Profile
    fields = ['age','city','country','profile_image','citation']
    template_name = 'accounts/profile_detail.html'
    success_url = '/accounts/profile'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class UserDetailView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = 'profile'
    
    model = User
    fields = ['username','email']
    template_name = 'accounts/user_detail.html'
    success_url = '/accounts/profile'
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class SearchPostResultsView(ListView):
    template_name = 'accounts/search_Post_results.html'
    model = Post
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
                        Q(title__icontains=query) | Q(description__icontains=query)
                        )
        return object_list
        
class SearchUserResultsView(ListView):
    template_name = 'accounts/search_user_results.html'
    model = User
    
    def get_queryset(self):
        if self.request.method == 'GET':
            query = self.request.GET.get('q')
            object_list = User.objects.filter(
                            Q(username__icontains=query) | Q(email__icontains=query)
                            )
        else:
            object_list = SearchUserForm()
            context = object_list
            return context
        return object_list

def upload(request):
    #inbox_form = InboxForm()
    #context = {}
    if request.method == 'POST':
        inbox_form = InboxForm(request.POST, request.FILES)
        if inbox_form.is_valid():
            inbox_form.save()
            return redirect('upload')
    
    else:
        inbox_form = InboxForm()
        """     
        uploaded_file = request.FILES['doc']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    """
    return render(request, 'accounts/upload.html', {'inbox_form':inbox_form})
#===============================================================================
class PostListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    #redirect_field_name = 'profile'
    
    template_name = 'accounts/post_list.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        
class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class PostCreateView(CreateView):
    #template_name = 'accounts/profile.html'
    model = Post
    fields = ['title','description']
    success_url = '/accounts/profile'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    comment_form_class = AddCommentForm
    fields = ['title','description','comments',]
    success_url = '/accounts/profile'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/accounts/profile'
    
class AddCommentView(TemplateView):
    template_name = 'accounts/profile.html'
    form_class = AddCommentForm
    model = Post
    fields = ['comments',]
    success_url = '/accounts/profile'
    
    def post(self, request):
        post_data = request.POST or None
        
        #post_form = self.post_form_class(post_data, prefix='post')
        form = self.form_class(post_data, prefix='comment')
        
        context = self.get_context_data(form=form) #post_form=post_form,
        """
        if post_form.is_valid():
            self.form_save(post_form)
           """
        if form.is_valid():
            self.form_save(form)
            
        return self.render_to_response(context)
    
    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

