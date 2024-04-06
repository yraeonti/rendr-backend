
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, company_name, password=None):
        """
        Creates and saves a User with the given email, name,
        company_name and password
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=email,
            name=name,
            company_name=company_name,
            password=password
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, company_name, password=None):
        """
        Creates and saves a superuser with the given email, name,
        company_name and password
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            company_name=company_name
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
