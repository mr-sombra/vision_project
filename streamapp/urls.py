from django.urls import path
from streamapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name="user"),
    path("video_feed", views.video_feed, name="video_feed"),
]
