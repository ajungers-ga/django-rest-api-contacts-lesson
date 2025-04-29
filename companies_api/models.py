from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)

    def __str__(self):
        return self.name