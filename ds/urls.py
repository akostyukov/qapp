from django.urls import path
from . import views


app_name = 'ds'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:tobacco_id>/delete/', views.delete, name='delete'),
]