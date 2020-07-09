from django.urls import path
from . import views


appname = 'ds'
urlpatterns = [
    path('', views.index, name='index')
]