from django.urls import path
from . import views


urlpatterns = [
    path('', views.jobs, name="jobs"),
    path('job-object/<str:pk>/', views.job, name="job"),
]
