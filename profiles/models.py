from django.db import models

# Create your models here.


class Profile(models.Model):
    f_name = models.CharField(max_length=20)  # max_length = required
    s_name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False, max_length=8)
    password = models.DecimalField(decimal_places=2, max_digits=4)
    summary = models.TextField(blank=True, null=True)
    admin = models.BooleanField()
