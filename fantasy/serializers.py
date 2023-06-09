from rest_framework import serializers
from fantasy.models import Trainer, Trade, Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'name', 'species_id', 'species_name', 'level')
class TrainerSerializer(serializers.ModelSerializer):
    pokemon_set = PokemonSerializer(many=True)
    class Meta:
        model = Trainer
        fields = ('id','name','pokemon_set')
class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'pokemon_1','pokemon_2','trainer_1','trainer_2')
