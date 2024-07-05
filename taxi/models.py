from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> str:
        return f"{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.last_name} ({self.license_number})"
        )
