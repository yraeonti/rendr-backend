from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views


urlpatterns = format_suffix_patterns([
    path('request_categories', views.RequestCategory.as_view(), name='categories'),
    path('requests', views.Requests.as_view(), name='requests'),
    path('request/<int:pk>', views.SingleRequest.as_view(), name='request'),
    path('employees', views.Employees.as_view(), name='employees'),
    path('employee/<int:pk>', views.SingleEmployee.as_view(), name='employee'),
    path('search_employees', views.SearchEmployees.as_view(), name='search_employees'),
    path('bulk_create_employees', views.BulkCreateEmployee.as_view(), name='bulk_employees'),
    path('parse_request_file', views.ParseRequestFile.as_view(), name='parse_request_file'),
    path('bulk_create_employees_file', views.ParseBulkEmployeesFile.as_view(), name='bulk_create_employees_file'),
])