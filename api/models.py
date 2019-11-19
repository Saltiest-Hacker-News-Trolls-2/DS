from django.db import models
from django.utils import timezone 
from django.core.validators import int_list_validator

# Create your models here.
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=15)
    by = models.CharField(max_length=50)
    time = models.IntegerField()
    dead = models.BooleanField(default=False)
    kids = models.IntegerField(default=0, validators=[int_list_validator])
    parent = models.IntegerField(default=0)
    text = models.TextField(default='')

    def __str__(self): 
        return self.text 


class SaltyUser(models.Model):
    by = models.ForeignKey(Items, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=8, decimal_places=3)
    catagory = models.CharField(default='', max_length=15)