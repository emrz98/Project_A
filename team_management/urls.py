from django.urls import path
from . import views
from django.conf.urls import url

app_name = "team_management"
urlpatterns = [path('menu/', views.main_menu, name = "menu")]