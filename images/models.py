from django.db import models
import uuid


class Image(models.Model):
    id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True, default=uuid.uuid4)
    hash = models.CharField(max_length=100)
