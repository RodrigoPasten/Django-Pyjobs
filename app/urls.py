from django.urls import path
from app import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.job_list, name='jobs_home'),
    path('job/<slug:slug>/', views.job_detail, name='job_detail'),
]