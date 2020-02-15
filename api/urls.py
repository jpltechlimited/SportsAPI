from django.contrib import admin
from django.urls import path
from sportsapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tennisplayers/<int:pk>/', views.TennisPlayerAPIView.as_view())
]
