from django.db import models

# Create your models here.
class Maqola(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=1500)
    text = models.TextField()

    def __str__(self):
        return self.title

class Maqolalar(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=1500)
    text = models.TextField()

    def __str__(self):
        return self.title        
