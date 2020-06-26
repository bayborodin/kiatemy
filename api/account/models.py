from django.db import models


class Account(models.Model):
    """Account model"""
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
