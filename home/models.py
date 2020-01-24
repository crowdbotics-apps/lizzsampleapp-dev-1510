from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    lizzcustomfield = models.FloatField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Car(models.Model):
    "Generated Model"
    model = models.CharField(max_length=256,)
    year = models.DateField()
    brand = models.CharField(max_length=256,)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="car_owner",
    )
    doors = models.BigIntegerField()
    engine = models.ForeignKey(
        "home.Engine",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="car_engine",
    )
    description = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="car_description",
    )


class Engine(models.Model):
    "Generated Model"
    fuel = models.CharField(max_length=256,)
    bhp = models.BigIntegerField()
    torque = models.FloatField()
    description = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="engine_description",
    )
