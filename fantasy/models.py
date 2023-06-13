from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


TRADE_STATUSES = ((1, 'pending'),
            (2, 'invalid'),
            (3, 'valid'),
            (4, 'rejected'),
            (5, 'fulfilled'))
# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    def can_field_team(self):
        if len(self.pokemon_set.all())>=3:
            return True
        else:
            return False

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
    def __str__(self):
        return self.name + ' level:' +str(self.level)

class Trade(models.Model):
    
    trainer_1 = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name = 'trainer_1')
    trainer_2 = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name = 'trainer_2')
    pokemon_1 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name = 'pokemon_1')
    pokemon_2 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name = 'pokemon_2')
    status = MultiSelectField(choices=TRADE_STATUSES, max_choices=1, max_length=1)
