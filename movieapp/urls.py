from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_page, name='login'),
    path('signup/',register_page,name='signup'),
    path('',home,name='home'),
    path('logout/',custom_logout,name='logout'),
]