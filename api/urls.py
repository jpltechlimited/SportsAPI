from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sportsapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tennisplayers/<str:pk>/', views.TennisPlayerAPIView.as_view())
]
