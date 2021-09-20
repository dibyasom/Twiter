from . import views
from django.urls import path

urlpatterns = [
    path('', views.tweets, name='feed'),
    path('<int:pk>', views.tweet, name='tweet-details')
]
