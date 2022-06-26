from django.urls import path
<<<<<<< HEAD
from posts.views import ViewCreate, viewPosts, ViewUpdate, ViewDelete

urlpatterns = [
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
]
=======
from posts.views import viewPosts, ViewRead, ViewCreate, ViewUpdate, ViewDelete

urlpatterns = [
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('blogpostread/<int:pk>/readpost', ViewRead.as_view(), name='blogpostread'),
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
]
>>>>>>> 398b73e812eadb45c4e525cec062eb11a9109357
