from django.urls import path 
from .views import home, create_post, view_post, update_post, delete_post

urlpatterns = [
    path('', home , name="home"),
    path('create_post/', create_post, name="create_post"),
    path('posts/<int:id>', view_post, name="post_view"),
    path('update_post/<int:id>', update_post ,name="update_post" ),
    path('delete_post/<int:id>', delete_post,name="delete_post")
]
