from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),# Endpoint para obter o token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# Endpoint para renovar o token
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]