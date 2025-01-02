from django.urls import path
from . import views

urlpatterns = [
    #path to home page 
    path('', views.home_page, name='home'),  # Home page

    #paths to the account registration/login 
    path('login-register/', views.register_login, name = 'login-register'),
    path('register/', views.signup_view, name='register'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    #user registration paths: 
    path('verify-email/', views.verify_email, name='verify-email'),
    path('verify-email/done/', views.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', views.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', views.verify_email_complete, name='verify-email-complete'),

    #path to the user interface
    # path('volunteer_page/', )
]