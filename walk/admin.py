from django.contrib import admin

from django.contrib.auth.models import User,Group
from walk.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('created','title','status')

admin.site.register(Post, PostAdmin)
