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

    class Meta:
        ordering = ('id',)

class SaltyUser(models.Model):
    id = models.IntegerField(primary_key=True)
    hacker = models.CharField(max_length=50)
    hacker_salt_ranking = models.IntegerField()
    comment = models.TextField(default='')
    comment_saltiness_score = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        ordering = ('hacker_salt_ranking',)