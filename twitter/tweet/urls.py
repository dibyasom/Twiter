from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.TweetList.as_view(), name='feed'),
    path('<int:pk>', views.TweetDetail.as_view(), name='tweet-details')
]

urlpatterns = format_suffix_patterns(urlpatterns)
print(urlpatterns)