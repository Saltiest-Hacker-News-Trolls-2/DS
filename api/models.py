from django.db import models
from django.core.validators import int_list_validator
from django_pandas.managers import DataFrameManager

# Create your models here.
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=15)
    by = models.CharField(max_length=50)
    text = models.TextField(default='')

    objects = DataFrameManager()
    
    def __str__(self): 
        return self.text 


class SaltyUser(models.Model):
    by = models.CharField(max_length=50)
    salty_score = models.DecimalField(max_digits=8, decimal_places=3)
    sarcasm_core = models.DecimalField(max_digits=8, decimal_places=3)
    catagory = models.CharField(default='', max_length=15)