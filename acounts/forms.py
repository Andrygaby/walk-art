from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from acounts.models import Profile, Post, Inbox

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = {'user',}

class AddCommentForm(forms.ModelForm):
    comments = forms.CharField(max_length=500, help_text = "Enter your comment")
    
    class Meta:
        model = Post
        exclude = {'user',}
        fields = ['comments',]

class SpeedPostForm(forms.Form):
    title = forms.CharField(max_length=500)
    
    class Meta:
        model = Post
        exclude = {'post',}
        fields = ['title',]
        
class SearchPostForm(forms.Form):
    q = forms.CharField(max_length=500, help_text = "Enter your research hear")

class SearchUserForm(forms.Form):
    q = forms.CharField(max_length=500, help_text = "Search sohear",required=False)
    
    #class Meta:
    #    model = Post
    #    exclude = {'user',}
    #    fields = ['comments',]
    
class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox
        #exclude = {'user',}
        fields = ['user','name','files']
