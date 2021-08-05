from django.urls import path
from .views import FeedBackView


urlpatterns = [
    path('',FeedBackView,name='feedback')
]