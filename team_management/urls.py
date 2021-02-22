from django.urls import path
from . import views
from django.conf.urls import url

app_name = "team_management"
urlpatterns = [path('task/', views.task, name = "task"),
                path('calendar/', views.calendar, name="calendar"),
                path('projects/',  views.projects, name  = "projects"),
                path('details/', views.details, name = "details")]