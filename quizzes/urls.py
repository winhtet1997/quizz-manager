from django.urls import path
from . import views

app_name = 'quizzes'
urlpatterns = [
    path('', views.quiz_list, name='list'),
    path('quiz/<int:pk>/', views.quiz_detail, name='detail'),
    path('quiz/<int:pk>/submit/', views.quiz_submit, name='submit'),
    path('history/', views.history, name='history'),
]
