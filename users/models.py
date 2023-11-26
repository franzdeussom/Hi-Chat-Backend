import time

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.text import gettext_lazy as _


def user_profile_upload_location(instance: AbstractUser, filename: str):
    return f"{instance.id}/profiles/{time.time()}{filename[filename.rfind('.'):]}"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password=password, **extra_fields)


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', _("homme")
        FEMALE = 'F', _("femme")
        __empty__ = _("(unknown)")

    class AccountType(models.TextChoices):
        STANDARD = "STANDARD", _("standard")
        PENDING = "PENDING", _("en cours de verification")
        PREMIUM = "PREMIUM", _("premium")

    username = False
    email = models.EmailField("email", max_length=255, unique=True)
    # password est deja défini par défaut
    age = models.IntegerField()
    gender = models.CharField("sexe", max_length=1, choices=Gender.choices, null=True)
    phone = models.CharField("telephone", max_length=20, null=True)
    birthday = models.DateField("anniversaire", null=True)
    country = models.CharField("pays", max_length=255, null=True)
    city = models.CharField("ville", max_length=255, null=True)
    profile = models.ImageField("profile", upload_to=user_profile_upload_location, max_length=512, null=True)
    account_type = models.CharField("type compte", choices=AccountType.choices, default=AccountType.STANDARD,
                                    max_length=10)

    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        # TODO check if password is not encrypted at every save
        return super().save(*args, **kwargs)