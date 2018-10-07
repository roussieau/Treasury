from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('add/', views.add_ticket, name='add_ticket'),
    path('add/money/', views.add_money, name='add_money'),
    path('history', views.history_of_my_transactions, name='history_of_my_transactions'),
    path('history/commu', views.history_transactions_commu, name='history_commu'),
    path('history/expenses', views.expenses_history, name='expenses_history'),
    path('charts', views.charts, name='charts'),
    path('status', views.status, name='status'),
]
