from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    