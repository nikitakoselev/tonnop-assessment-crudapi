
from django.urls import path
from . import views


urlpatterns = [
    path('admin/register', views.RegisterUserView.as_view(), name="register-user"),
    path('all/employees', views.GetEmployeesView.as_view(), name="all-employees"),
    path('employee/<int:pk>', views.GetEmployeeView.as_view(), name="get-employee"),
    path('employee', views.PostEmployeeView.as_view(), name='post-employee'),
    path('employee/update/<int:pk>', views.UpdateEmployeeView.as_view(), name="put-employee"),
    path('employee/delete/<int:pk>', views.DeleteEmployeeView.as_view(), name="delete-employee")
]