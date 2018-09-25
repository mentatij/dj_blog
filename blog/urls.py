from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list_url'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post_detail_url'),
    path('tags/', TagsListView.as_view(), name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', TagDetailView.as_view(), name='tag_detail_url'),
]
