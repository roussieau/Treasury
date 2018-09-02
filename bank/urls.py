from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('add/', views.add_ticket, name='add_ticket'),
    path('history', views.history_of_my_transactions, name='history_of_my_transactions'),
]
