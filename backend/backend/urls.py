from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  # Home and authentication URLs
    path('authentication/', include('authentication.urls')),  # Include authentication URLs
    path('reviews/', include('reviews.urls'))
]
