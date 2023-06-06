from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Pokemon(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length = 25)
    species_id = models.IntegerField()
    species_name = models.CharField(max_length=50)
    level = models.IntegerField(
            default=1, 
            validators=[
                MaxValueValidator(100),
                MinValueValidator(1)
                ]
            )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
