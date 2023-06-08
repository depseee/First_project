from django.urls import path
from . import views

urlpatterns = [
    path('', views.keanu),
    path('power_man', views.power_man),
    path('bar_name', views.bar_name),
    path('count_needle', views.count_needle),
    path('people', views.people_info),
    path('table', views.table),
]