from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from authentication import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = format_suffix_patterns([
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.MyTokenTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
])