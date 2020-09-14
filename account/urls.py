from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework import routers

from .views import (
    RegisterView,
    login_request,
    logout_request,
    UserView,
    ProfileAPIView,
    profile_request,
)

app_name = 'account'

router = routers.DefaultRouter()
router.register(r'users', UserView, basename='users')

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login/',  login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('home', login_required(TemplateView.as_view(template_name='account/home.html')), name='home'),
    path('profile/<int:pk>', profile_request, name='profile'),
    # path('api/', include(router.urls), name='users'),
    path('api/profile/<int:pk>/', ProfileAPIView.as_view())
]