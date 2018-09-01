from django.urls import path
from . import views

app_name = 'bank'
urlpatterns = [
    path('add/', views.add_ticket, name='add_ticket')
]
