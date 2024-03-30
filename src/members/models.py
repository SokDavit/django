from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
# Create your models here.
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

