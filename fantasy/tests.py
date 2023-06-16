from django.test import TestCase, Client
from .models import Trainer
from .views import is_trade_valid
# Create your tests here.
class TradeTests(TestCase):
    def test_is_trade_valid(self):
        trainer_1 = Trainer(name = "Trainer 1")
        trainer_2 = Trainer(name = "Trainer 2")
        trainer_1.save()
        trainer_2.save()
        trainer_1.pokemon_set.create(name = "testpoke1",species_name = "testbulba", species_id = 1)
        trainer_2.pokemon_set.create(name = "testpoke2",species_name = "testbulba", species_id = 1)
        pokemon_1 = trainer_1.pokemon_set.all()[0]
        pokemon_2 = trainer_2.pokemon_set.all()[0]
        trade_data = {'trainer_1':trainer_1, 'trainer_2':trainer_2,'pokemon_1':pokemon_1, 'pokemon_2':pokemon_2}
        self.assertIs(is_trade_valid(trade_data), True)
        trade_data = {'trainer_1':trainer_1, 'trainer_2':trainer_2,'pokemon_1':pokemon_1, 'pokemon_2':pokemon_1}
        self.assertIs(is_trade_valid(trade_data), False)
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
        self.assertIs(trainer.can_field_team(),True)
