#-*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User, AbstractBaseUser
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
            self).get_queryset().filter(
                status="published")
        
class Post(models.Model):
    published = PublishedManager()
    
    STATUS_CHOICES = (
            ('draft','Draft'),
            ('published','Published'),
        )
        
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author =models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_post')
    body = models.TextField(blank=True)
    likes = models.ManyToManyField(
         settings.AUTH_USER_MODEL,
         related_name = 'likes', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft')
    
    objects = User()
    
    class Meta:
        pass
        
    def __str__(self):
        return self.title
        
