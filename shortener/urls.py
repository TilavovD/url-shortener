from django.urls import path
from .views import shortify, link_match

urlpatterns = [
    path('', shortify, name='shortify'),
    path('<str:link>', link_match, name='match'),
]
