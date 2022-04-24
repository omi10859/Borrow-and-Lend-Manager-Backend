from rest_framework.authtoken import views
from django.urls import path
from .views import GetUsers

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('get_users/', GetUsers.as_view())
]