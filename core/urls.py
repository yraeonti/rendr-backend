from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views


urlpatterns = format_suffix_patterns([
    path('request_categories', views.RequestCategory.as_view(), name='categories'),
    path('requests', views.Requests.as_view(), name='requests'),
    path('request/<int:pk>', views.SingleRequest.as_view(), name='request'),
    path('bulk_create_employees', views.BulkCreateEmployee.as_view(), name='bulk_employees')
])