from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    path('',index, name="index"),
    path('signup/',signup, name="signup"),
    path('user_login/',user_login, name="user_login"),
    path('index2/',index2, name="index2"),
    path('logout/', userLogout, name="logout"),
    path('adminreg',adminreg,name="adminreg"),

    # path('contact/',contact, name="contact"),
    # path('about/',about, name="about"),
    path('check_user_exists/', check_user_exists, name='check_user_exists'),


    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
#     path('forgotPassword/',forgotPassword, name="forgotpassword")
   ]