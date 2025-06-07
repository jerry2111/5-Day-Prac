
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_spectacular.views import SpectacularAPIView , SpectacularSwaggerView
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from  tasks.views import RegisterView


def api_root_view(request) :
    return JsonResponse(
        {
            "api_name": "Todo API",
            "version": "v1",
            "routes": {
                "list_tasks": "/api/tasks/",
                "get_task_detail": "/api/tasks/<id>/",
                "swagger_docs": "/api/docs/",
                "schema": "/api/schema/",
                "admin": "/admin/"
            }
        }
    )




urlpatterns = [
    path("", api_root_view), 
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(), name='register')
]
