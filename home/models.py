from django.db import models

# Create your models here
class Trekking(models.Model):
    trekking_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tekking_name

class tour(models.Model):
    tour_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tour_name

