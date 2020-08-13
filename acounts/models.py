from django.db import models
from django.db.models import F
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=25,blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    profile_image = models.ImageField(blank=True)
    citation = models.TextField(max_length=200,blank=True)
    
    def __str__(self):
        return self.user.username
        
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk':self.pk})
        
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
        
class Inbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    files = models.FileField(upload_to="accounts/Inbox/%Y/%m/%d/")
    
    def __str__(self):
        return self.name
        

    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=25,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250, blank=True)
    adore = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='adores',
                                 blank=True
                                 )
    #comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
     #                               related_name='comment',
     #                               blank=True,
      #                              )
    
    #is_liked = models.BooleanField(default=False)
    
    objects = User()
    ordering = [F('-date_posted').asc(nulls_last=True)]
    
    class Meta:
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.title
                
    def total_likes(self):
        return self.adore.count()
        
    #def total_comments(self):
        #return self.comments.count()
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
""" 
class Comment(Post):
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.content
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
        
    @property
    def is_liked(self):
        try:
            if self.likes.filter(id=self.user.id).exists():
                 self.likes.is_liked = True
                 return True
            else:
                self.likes.is_liked = False
                return False
        except User.DoesNotExist:
            return None
  """    

"""
class Like(models.Model):
    post = models.OneToOneField('notify.Post',related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.users.id
                
    def total_users(self):
        return self.users.count()
"""
