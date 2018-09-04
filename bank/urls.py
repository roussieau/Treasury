from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('add/', views.add_ticket, name='add_ticket'),
    path('add/money/', views.add_money, name='add_money'),
    path('history', views.history_of_my_transactions, name='history_of_my_transactions'),
    path('history/all', views.history_of_transactions, name='history_of_transactions'),
]
