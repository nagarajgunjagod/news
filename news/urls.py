from django.urls import path
from .views import news_list,news_detail

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('<int:pk>/', news_detail, name='news_detail'),
]
