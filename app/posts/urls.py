from django.urls import path
from posts.views import *
from posts import views

urlpatterns = [
    path('newpost/', views.blogPostForm, name="blogPostForm"),
    path('viewPosts/', views.viewPosts, name="viewPosts"),
    path('blogpostupdate/<int:pk>/update', views.updatePosts, name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', views.deletePosts, name='blogpostdelete'),
]
