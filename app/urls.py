from django.urls import path
from . import views   

urlpatterns = [
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("register-employee/", views.register_employee, name="register-employee"),
    path("employees/", views.list_employees, name="list-employees"),
    path("employees/<str:employee_id>/update/", views.update_employee, name="update-employee"),
    path("employees/<str:employee_id>/delete/", views.delete_employee, name="delete-employee"),
    path('attendance-summary/', views.attendance_summary_api, name='attendance-summary-api'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('clock_in/', views.clock_in, name='clock_in'),
    path('clock_out/', views.clock_out, name='clock_out'),
    path('break_in/', views.break_in, name='break_in'),
    path('break_out/', views.break_out, name='break_out'),
    path('lunch_in/', views.lunch_in, name='lunch_in'),
    path('lunch_out/', views.lunch_out, name='lunch_out'),

    path("muster-request/", views.create_muster_request, name="create-muster-request"),
    path("muster-request/list/", views.list_muster_requests, name="list-muster-request"),
    path("muster-request/<int:request_id>/edit/", views.edit_muster_request, name="edit-muster-request"),
]
