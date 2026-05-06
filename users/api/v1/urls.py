from django.urls import path
from users.api.v1.views import RegisterView, LoginView, VerifyOtpView, ProfileView, ResendOtpView


urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify-otp/<str:username>/', VerifyOtpView.as_view(), name='verify-otp'),
    path('resend-otp/<str:username>/', ResendOtpView.as_view(), name='resend-otp'),
]