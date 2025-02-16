from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/post/', views.job_post, name='job_post'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
]