from django.db import models
from django import forms
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=100,blank=False,null=False)
    image = ImageField()
    
    CONDITION_CHOICES = [
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]
    
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=10)

    def __str__(self):
        return self.text