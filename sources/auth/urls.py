from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views

from .views import profile

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             extra_context={'next': settings.MAIN_PAGE}),
         name='login',
         ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('profile/', profile, name='profile'),
]
