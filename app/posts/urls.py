from django.urls import path
from posts.views import viewPosts, ViewRead, ViewCreate, ViewUpdate, ViewDelete, addComment

urlpatterns = [
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('blogpostread/<int:pk>/readpost', ViewRead.as_view(), name='blogpostread'),
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
    path('addcomment/', addComment, name='addcomment'),
]
