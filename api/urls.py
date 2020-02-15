from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from sportsapi import views

schema_view = get_schema_view(
   openapi.Info(
      title="Sports API",
      default_version='v1'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'admin/', admin.site.urls),
    #path(r'api/tennisplayers/<str:pk>/', views.TennisPlayerAPIView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/hello/', views.HelloView.as_view(), name='hello'),
]
