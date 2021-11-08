from django.db import models
from django.utils import timezone
# Create your models here.
class Inventory(models.Model):
    prod_title = models.CharField(max_length=255, unique=True)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    
    
    


    def __str__(self):
        return self.prod_title
