from django.urls import path
from . import views


app_name = 'qaa'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('<int:question_id>/edit/', views.edit, name='edit'),
    path('<int:question_id>/delete/', views.delete, name='delete'),
    path('start/', views.start, name='start'),
    path('<int:question_id>/add_answer/', views.add_answer, name='add_answer'),
    path('clear/', views.clear, name='clear'),
]