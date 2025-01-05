from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<str:pk>', views.newsDetail, name='news-detail'),
    path('news-admin', views.newsAdmin, name='news-admin'),

    path('create-news', views.createNews, name='create-news'),
    path('edit-news/<str:pk>', views.editNews, name='edit-news'),
    path('delete-news/<str:pk>', views.deleteNews, name='delete-news'),
]