from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from sportsapi import views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^', include_docs_urls(title='Sports API')),
    url(r'^api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'admin/', admin.site.urls),
    path(r'api/tennisplayers/<str:pk>/', views.TennisPlayerAPIView.as_view())
]
