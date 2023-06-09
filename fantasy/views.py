from django.shortcuts import render
from .models import Trainer
from django.core import serializers
from .serializers import TrainerSerializer
# Create your views here
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello and welcome to Pokemon Fantasy index")

def team_details(request, team_id):
    try:
        team = Trainer.objects.get(id = team_id)
    except Trainer.DoesNotExist:
        return HttpResponse(status = 404)
    serializer = TrainerSerializer(team)
    return JsonResponse(serializer.data)
   # pokemon_to_display = team.pokemon_set.all()
   # data = serializers.serialize('json',list(pokemon_to_display))
   # return HttpResponse(data)
