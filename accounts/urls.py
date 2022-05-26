from django.urls import path,include
from . import views
# from rest_framework.authtoken.views import obtain_auth_token 
from dj_rest_auth.views import LogoutView,LoginView
from django_rest_passwordreset import urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'accounts'

urlpatterns = [
    #Create And Revoke Token
    # path('create-token/',obtain_auth_token,name='token'),
    # path('revoke-token/',views.RevokeTokenView.as_view(),name='revoke'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('login/',LoginView.as_view(),name='login'),
    path('register/', views.RegisterUserView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),

    #change and reset Password
    path('password_change/',views.ChangePasswordView.as_view(),name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls',)),

    #admin panel
    path('admin_panel/',views.AdminPanelView.as_view(),name='admin-panel'),
    path('admin_panel/<int:pk>/',views.AdminPanelView.as_view(),name='admin-panel'),

]