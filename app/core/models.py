from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    
    def create_user(self, email, password = None, **extra_fields):
        """Creates and save a new user """
        if not email:
            raise ValueError("Users must provide an email address")
        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 


    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True 
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """Custom User models that defines using email instead of username"""
    email   = models.EmailField(max_length=255,  unique  = True)
    name    = models.CharField(max_length = 200)
    is_active = models.BooleanField(default  = True)
    is_staff  = models.BooleanField(default  = False) 
    objects  = UserManager()
    USERNAME_FIELD = 'email'
