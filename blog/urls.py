from django.urls import path
from .views.auth_views import renderRegisterForm, renderLoginForm
from .views.home_views import renderHOme
urlpatterns = [
    path('register',renderRegisterForm),
    path('login',renderLoginForm),
    path('home',renderHOme),
]
