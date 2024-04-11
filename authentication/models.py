
from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.timezone import now
from authentication.usermanager import UserManager

# Create your models here.




class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email=models.EmailField(unique=True)
    name=models.CharField()
    company_name=models.CharField()
    forgot_password_token = models.CharField(null=True)
    forgot_password_expiry = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["name", "company_name"]

    def save(self, *args, **kwargs) -> None:
        self.created_at = now()
        self.set_password(self.password)
        self.email = UserManager.normalize_email(self.email)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name

    


