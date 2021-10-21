from django.db import models

# Create your models here.

class Shoes(models.Model):
    type = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    brand_url = models.TextField()

    def __str__(self):
        return self.type

class Brand(models.Model):
    name = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name="brand")
    type = models.CharField(max_length=100, default='no shoe type')
    brand_url = models.TextField(default="no brand exist")

    def __str__(self):
        return self.type