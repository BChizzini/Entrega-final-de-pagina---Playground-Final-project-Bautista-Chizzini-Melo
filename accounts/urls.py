from django.urls import path
from .views import profile_detail_view, CustomLoginView, CustomLogoutView, signup_view, profile_view, change_password_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/<str:username>/', profile_detail_view, name='profile_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('change_password/', change_password_view, name='change_password'),
]