from django.urls import path
from posts.views import viewPosts, ViewCreate, ViewUpdate, ViewDelete

#TODO Renombrar name´s
urlpatterns = [
    path('viewPosts/', viewPosts, name="viewPosts"),
    path('newpost/', ViewCreate.as_view(), name="blogPostForm"),
    path('blogpostupdate/<int:pk>/update', ViewUpdate.as_view(), name="blogpostupdate"),
    path('blogpostdelete/<int:pk>/delete', ViewDelete.as_view(), name='blogpostdelete'),
]
