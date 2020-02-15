from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from sportsapi import views

urlpatterns = [
    url(r'^api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'admin/', admin.site.urls),
    path(r'api/tennisplayers/<str:pk>/', views.TennisPlayerAPIView.as_view())
]
