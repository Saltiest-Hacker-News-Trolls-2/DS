from django.db import models
from django.utils import timezone 
from django.core.validators import int_list_validator

# Create your models here.
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=15)
    text = models.TextField(max_length=500)
    by = models.CharField(max_length=50)
    time = models.DateField(default=timezone.now)
    parent = models.CharField(max_length=50)
    # kids = models.Inte(validators=int_list_validator)
    url = models.URLField(max_length=75)
    score = models.IntegerField()
    title = models.TextField(max_length=100)
    # parts = models.CharField(validators=int_list_validator)
    descendants = models.IntegerField()

    def __str__(self): 
        return self.title 