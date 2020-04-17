from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return self.username + "," + self.first_name + " " + self.last_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pesel = models.CharField(max_length=11)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
