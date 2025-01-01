from django.urls import path
from . import views

urlpatterns = [
    #path to home page 
    path('', views.home_page, name='home'),  # Home page

    #paths to the account registration/login 
    path('login-register/', views.register_login, name = 'login-register'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    #path to the user interface
    # path('volunteer_page/', )
]