from django.urls import path
from users.api.v1.views import RegisterView, LoginView, Register, VerifyOtpView, ProfileView


urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify-otp/',VerifyOtpView.as_view(),name='verify-otp')
]