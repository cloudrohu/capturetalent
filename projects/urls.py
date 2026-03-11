from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('ongoing/', views.ongoing_projects, name='ongoing'),
    path('complete/', views.complete_projects, name='complete'),

]