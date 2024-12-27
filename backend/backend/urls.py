from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')), 
    #need to fix user and admin home 
    # path('user_home/', user_home, name='user_home'),
    # path('admin_home/', admin_home, name='admin_home'),
]
