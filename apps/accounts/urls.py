from django.urls import path

from .views import (
    UserRegisterView, 
    LoginView,
    LogoutView,
    UpdateUserView,
    PasswordResetView,
    CheckVerifyCodeView,
    PasswordResetConfirmView,
    Login_or_Logout_View,
)
app_name='accounts'
urlpatterns =[
    path('register/', UserRegisterView.as_view(), name='register' ),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('password_reset/', PasswordResetView.as_view(), name = "password_reset"),
    path('check_verify_code/<uuid:uuid>/', CheckVerifyCodeView.as_view(), name="check_verify"),
    path('password_reset_confirm/<uuid:uuid>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('login_or_logout/', Login_or_Logout_View.as_view(), name=''),
]
