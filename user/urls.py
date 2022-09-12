from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserAPI

urlpatterns = [

    path('api/auth_token/', TokenObtainPairView.as_view()),
    path('api/refresh_token/', TokenRefreshView.as_view()),
    path('user/', UserAPI.as_view()),

]
