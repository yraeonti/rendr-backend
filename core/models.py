from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.



class Employee(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    role = models.CharField()
    password = models.CharField(default=None, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RequestCategory(models.Model):
    item = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.item

class Request(models.Model):

    class RequestStatus(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        DECLINED = "DECLINED", _("Declined")
        SUCCESSFULL = "SUCCESSFULL", _("Successful")

    request_id = models.CharField(unique=True, default='')
    procure_items = models.JSONField()
    approvals = models.JSONField()
    status = models.CharField(choices=RequestStatus, default=RequestStatus.PENDING)
    request_category = models.ForeignKey(RequestCategory, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

