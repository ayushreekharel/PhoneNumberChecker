from django.db import models
from datetime import time
from django.utils import timezone
# Create your models here.
 

class Details(models.Model):
    country=models.CharField(max_length=20)
    number=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):

        print(f"{self.country},{self.number}")
        return f"{self.country},{self.number},{self.time}"
    


 