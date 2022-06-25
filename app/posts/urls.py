from django.urls import path
from posts.views import ViewCreate, viewPosts, ViewUpdate, ViewDelete, ReadPost 

urlpatterns = [
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('<int:pk>/readpost/', ReadPost.as_view(), name='ReadPost'),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
]