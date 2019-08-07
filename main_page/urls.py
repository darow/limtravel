from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('tourist_visas', views.tourist_visas, name="tourist_visas"),
    path('long-term_visas', views.long_term_visas, name="long-term_visas"),
    path('international_passport', views.international_passport, name="international_passport"),
    path('invitations', views.invitations, name="invitations"),
]
