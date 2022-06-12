from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer



urlpatterns = [
    # path('admin/', admin.site.urls),
     path('api/v1/admin/login', TokenObtainPairView.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('employees.urls'))
]