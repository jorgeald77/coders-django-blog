from django.urls import path
from posts.views import ViewCreate, viewPosts, ViewUpdate, ViewDelete

urlpatterns = [
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
]