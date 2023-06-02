from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>/', views.get_info_about_day_by_num),
    path('<str:day>/', views.get_info_about_day, name='week_days-name'),
]