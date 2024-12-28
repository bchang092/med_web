from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns 
    #note to self: anything I put on this page will be on top of review path: ie review/x
    path('volunteer_page', views.volunteer_page, name='volunteer_page'),
]
