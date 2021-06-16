from django.urls import path
from .views import UserRegisterView
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.login_red, name='login_red'),
    path('register/', UserRegisterView.as_view(), name='register',)
]
