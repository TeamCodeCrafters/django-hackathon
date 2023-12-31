"""
Database models.
"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def is_admin(self):
        for group in self.groups.all():
            if group.name == "Administradores":
                return True
        return False

    @property
    def is_avaliador(self):
        if self.is_admin:
            return True
        for group in self.groups.all():
            if group.name == "Avaliadores":
                return True
        return False

    @property
    def is_professor(self):
        if self.is_admin:
            return True
        for group in self.groups.all():
            if group.name == "Professores":
                return True
        return False

    @property
    def is_aluno(self):
        if self.is_admin:
            return True
        for group in self.groups.all():
            if group.name == "Alunos":
                return True
        return False
