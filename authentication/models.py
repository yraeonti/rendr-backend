
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.timezone import now
from authentication.usermanager import UserManager

# Create your models here.




class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    name=models.CharField()
    company_name=models.CharField()
    forgot_password_token = models.CharField(null=True)
    forgot_password_expiry = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateField(default=now())

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["name", "company_name"]

    def save(self, *args, **kwargs) -> None:
        self.created_at = now()
        self.set_password(self.password)
        self.email = UserManager.normalize_email(self.email)
        return super().save(*args, **kwargs)

    


