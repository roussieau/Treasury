from django.urls import path
from . import views

app_name = 'supper'
urlpatterns = [
    path('planning/', views.planning, name='planning'),
]