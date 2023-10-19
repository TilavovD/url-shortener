from django.urls import path
from .views import shortify

urlpatterns = [
    path('', shortify, name='home'),
]
