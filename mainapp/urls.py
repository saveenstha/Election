from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('ballotblitz/', views.ballotBlitz, name='ballot_blitz'),
]