from django.urls import path
from . import views

app_name = 'supper'
urlpatterns = [
    path('planning/', views.planning, name='planning'),
    path('day/<int:id>/switch', views.switch, name='switch_day'),
    path('day/<int:id>/up', views.upWeight, name='up_weight'),
    path('day/<int:id>/down', views.downWeight, name='down_weight'),
    path('day/<int:id>/', views.day, name='day'),
]