from django.test import TestCase
from .models import Trainer

# Create your tests here.

class TrainerModelTests(TestCase):
    def test_can_field_team(self):
        trainer = Trainer(name = "test trainer")
        trainer.save()
        self.assertIs(trainer.can_field_team(),False)
        trainer.pokemon_set.create(name = "testpoke1",species_name = "testbulba", species_id = 1)
        trainer.save()
        self.assertIs(trainer.can_field_team(), False)
        trainer.pokemon_set.create(name = "testpoke2",species_name = "testbulba", species_id = 1)
        trainer.pokemon_set.create(name = "testpoke3",species_name = "testbulba", species_id = 1)
        trainer.pokemon_set.create(name = "testpoke4",species_name = "testbulba", species_id = 1)
        trainer.pokemon_set.create(name = "testpoke5",species_name = "testbulba", species_id = 1)
        self.assertIs(trainer.can_field_team(),True)
