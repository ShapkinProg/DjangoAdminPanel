from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:vuzid>/', vuz_show, name='show_vuz'),
    path('<int:vuzid>/add/', addperson, name='add_person')
]