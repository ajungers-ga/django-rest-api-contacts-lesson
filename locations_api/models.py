from django.db import models

# Create your models here.

class Location(models.Model):
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)


#BELOW = # Dunder method (double underscore method).
# Django uses __str__ to control what gets displayed when the object is shown as text.
# This improves the Admin view — instead of showing 'Company object (1)', it shows a readable name like 'Apple' or 'Google'.
def __str__(self):
    return f"{self.street}, {self.city}, {self.state}"
