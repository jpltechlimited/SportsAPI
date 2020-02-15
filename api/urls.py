from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sportsapi import views

router = routers.DefaultRouter()
router.register('tennisplayers', views.TennisPlayerAPI)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]