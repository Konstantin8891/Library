from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(
            self,
            username,
            email,
            password=None
    ):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self,
            username,
            email,
            password=None
    ):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
