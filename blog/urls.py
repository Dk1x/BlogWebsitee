from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users_view, name='users'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('categories/', views.categories_view, name='categories'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('comments/', views.comments_view, name='comments'),
    path('blogs/', views.blog_list, name='blogs'),
    path('blogs/<int:post_id>/', views.blogdetails, name='blogdetails'),
]