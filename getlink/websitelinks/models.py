from django.db import models

# Create your models here.
class users(models.Model):
    urls = models.CharField(max_length=64)
    def __str__(self):        
        return f"{self.urls}"    

      