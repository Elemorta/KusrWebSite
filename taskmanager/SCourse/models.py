import datetime

from django.db import models
from django.urls import reverse


class Town(models.Model):
    Name_Town = models.CharField(max_length=255)

    def __str__(self):
        return self.Name_Town


class Street(models.Model):
    Name_Street = models.CharField(max_length=255)
    Town = models.ForeignKey(Town, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name_Street


class Bundle(models.Model):
    Name_Bundle = models.CharField(max_length=255, unique=True)
    Count_channels = models.IntegerField(default=None, null=True)
    Count_films = models.IntegerField(default=None, null=True)
    Price = models.IntegerField()
    Date_begin = models.DateField(null=True)
    Date_end = models.DateField(null=True)

    def __str__(self):
        return self.Name_Bundle

    def get_absolute_url(self):
        return reverse('appbund', kwargs={'bundles_name': self.Name_Bundle})


class Operator(models.Model):
    Name_Operator = models.CharField(max_length=255)
    Login = models.CharField(max_length=30, unique=True)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Name_Operator


class Application(models.Model):
    Name_Client = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    House = models.CharField(max_length=5)
    Entrance = models.IntegerField()
    Floor = models.IntegerField()
    Flat = models.IntegerField()
    Status = models.BooleanField(null=True, default=False)
    Bundle = models.ForeignKey(Bundle, null=True, on_delete=models.SET_NULL)
    Street = models.ForeignKey(Street, null=True, on_delete=models.SET_NULL)
    Town = models.ForeignKey(Town, null=True, on_delete=models.SET_NULL)
    Operator = models.ForeignKey(Operator, null=True, on_delete=models.SET_NULL)
    Date_application = models.DateField(null=True, default=datetime.date.today())

