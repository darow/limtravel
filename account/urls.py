from django.urls import path, include
from . import views
from django.contrib import admin
from .views import SignUpView


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', views.register, name='signup'),
    path('private_aria/', views.private_area, name='private_area'),
    # path('', include('django.contrib.auth.urls')),
    path('became_partner/', views.became_partner, name="became_partner"),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),

]