from django.db import models


class Town(models.Model):
    Name_Town = models.CharField(max_length=255)

    def __str__(self):
        return self.Name_Town


class Street(models.Model):
    Name_Street = models.CharField(max_length=255)
    Number_Street = models.IntegerField()
    Town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name_Street


class Bundle(models.Model):
    Name_Bundle = models.CharField(max_length=255)
    Discription = models.TextField()
    Price = models.IntegerField()
    Date_begin = models.DateField()
    Date_end = models.DateField()


class Operator(models.Model):
    Name_Operator = models.CharField(max_length=255)
    Login = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)


class Application(models.Model):
    Name_Client = models.CharField(max_length=255)
    Phone_Number = models.IntegerField()
    House = models.CharField(max_length=10)
    Entrance = models.IntegerField()
    Floor = models.IntegerField()
    Flat = models.IntegerField()
    Status = models.BooleanField()
    Bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE, null=True)
    Street = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    Town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    Operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True)
