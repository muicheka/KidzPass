from django.db import models

# Create your models here.


class Profile(models.Model):
    f_name = models.CharField(max_length=20)  # max_length = required
    s_name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False, max_length=8)
    summary = models.TextField(blank=True, null=True)
    admin = models.BooleanField()


# testing git cause it sucks 