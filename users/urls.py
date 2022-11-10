from django.urls import path, include 
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', )
    path('', views.UserView.as_view(), name='user_view'), # url 바뀌어도 name으로 가져올 수 있다.
    # path('mock/', views.mockView.as_view(), name='mock_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]