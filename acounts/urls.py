from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from acounts.views import (PostListView, PostCreateView,
                            PostDetailView,PostUpdateView,
                            PostDeleteView,
                            AddCommentView,
                            
                            UserDetailView,
                            ProfileEditView,
                            ProfileView,
                            
                            SearchPostResultsView,
                            SearchUserResultsView
                            )
from acounts import views

urlpatterns = [
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    path('accounts/profile/search',
            SearchPostResultsView.as_view(),
            name='search_results'),
    path('accounts/profile/search_people',
            SearchUserResultsView.as_view(),
            name='search_user_results'),

    url(r'^accounts/profile', ProfileView.as_view(template_name="accounts/profile.html"),name="profile"),
    #url(r'^accounts/profile', PostListView.as_view(template_name="accounts/profile.html"),name="profile"),
    url(r'^accounts/profile', AddCommentView.as_view(template_name="accounts/profile.html"),name="profile"),
    path('accounts/edit_profile/<int:pk>/',
    ProfileEditView.as_view(template_name="accounts/profile_detail.html"),name='profile-detail'),
    path('accounts/edit_profile/<int:pk>/update',
    UserDetailView.as_view(template_name='accounts/user_detail.html'), name='profile-update'),
        
    path('accounts/public', PostCreateView.as_view(), name='post-create'),
    path('accounts/public/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('accounts/public/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('accounts/public/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),


    path('accounts/upload', views.upload, name='upload'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
