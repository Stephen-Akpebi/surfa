from re import template
from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('post_index/', views.PostList.as_view(), name='post_index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]