from django.db import models

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=10)
    f_name = models.CharField(max_length=20)  # max_length = required
    s_name = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    admin = models.BooleanField(default=False)

#auto_now=False, auto_now_add=False, max_length=8