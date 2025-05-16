from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    service_img = models.ImageField(upload_to='services/')
    
    def __str__(self):
        return self.name