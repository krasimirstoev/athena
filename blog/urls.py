from django.urls import path
from . import views
from .feeds import LatestPostsFeed, LatestCommentsFeed

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('categories/', views.category_list, name='category_list'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('rss/posts/', LatestPostsFeed(), name='posts_rss_feed'),
    path('rss/comments/', LatestCommentsFeed(), name='comments_rss_feed'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
