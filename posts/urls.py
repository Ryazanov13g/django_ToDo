from django.urls import path

from posts.views import (PostCreateView, PostsListView, PostUpdateView,
                         not_actuality, post_delete)

app_name = 'posts'

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post_not_actuality/', not_actuality, name='post_not_actuality'),
    path('post_delete/<int:post_id>', post_delete, name='post_delete'),
]
