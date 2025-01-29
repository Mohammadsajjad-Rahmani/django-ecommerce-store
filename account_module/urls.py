from django.urls import path
from . import views

urlpatterns = [
    path('register', views.Register.as_view(), name='register-page'),
    path('login', views.Login.as_view(), name='login-page'),
    path('logout', views.Logout.as_view(), name='logout-page'),
    path('forget-password', views.ForgetPassword.as_view(), name='forget-password-page'),
    path('reset-password/<str:email_active_code>', views.ResetPassword.as_view(), name='reset-password-page'),
    path('activated-code/<str:email_active_code>', views.AcitivatedAccount.as_view(), name='active-code-page') # mitoni str ro nanevisi

]
