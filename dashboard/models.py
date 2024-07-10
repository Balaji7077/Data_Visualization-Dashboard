from django.db import models

# Create your models here.

class Data(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField(default=None, null=True)
    country = models.CharField(max_length=100, null=True)
    topic = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.topic} - {self.country} ({self.year})"