from django.shortcuts import render
from .models import Trainer
from django.core import serializers

# Create your views here
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello and welcome to Pokemon Fantasy index")

def team_details(request, team_id):
    team = Trainer.objects.get(id = team_id)
    pokemon_to_display = team.pokemon_set.all()
    data = serializers.serialize('json',list(pokemon_to_display))
    return HttpResponse(data)
