from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token 
from dj_rest_auth.views import LogoutView,LoginView

app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/', views.RegisterUserView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
]