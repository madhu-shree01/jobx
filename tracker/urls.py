from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hr/login/', views.hr_login, name='hr_login'),
    path('hr/dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('hr/update/<int:job_id>/', views.hr_update_status, name='hr_update_status'),
    path('add/', views.add_job, name='add_job'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),


]
