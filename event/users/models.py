from django.contrib.auth.models import AbstractUser
from django.db import models

from events.models import Organization
from .managers import MyUserManager


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
