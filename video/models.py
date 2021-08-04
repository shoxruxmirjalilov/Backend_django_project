from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to='vedeo/%y')
    qisqacha = models.CharField(max_length=1500)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title