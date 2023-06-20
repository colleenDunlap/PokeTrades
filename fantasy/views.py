from django.shortcuts import render
from .models import Trainer
from django.core import serializers
from .serializers import TrainerSerializer, TradeSerializer
# Create your views here
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
def index(request):
    return HttpResponse("Hello and welcome to Pokemon Fantasy index")

def team_details(request, team_id):
    try:
        team = Trainer.objects.get(id = team_id)
    except Trainer.DoesNotExist:
        return HttpResponse(status = 404)
    serializer = TrainerSerializer(team)
    return JsonResponse(serializer.data)

def is_trade_valid(trade_data):
    trainer_1 = Trainer.objects.get(id = trade_data["trainer_1"].id)
    trainer_2 = Trainer.objects.get(id = trade_data["trainer_2"].id)
    trainer_1 = trade_data["trainer_1"]
    trainer_2 = trade_data["trainer_2"]
    if not trainer_1.can_field_team():
        return False
    if not trainer_2.can_field_team():
        return False
    pokemon_1 = trade_data["pokemon_1"]
    pokemon_2 = trade_data["pokemon_2"]
    if pokemon_1 not in trainer_1.pokemon_set.all():
        return False
    if pokemon_2 not in trainer_2.pokemon_set.all():
        return False
    level_diff = pokemon_1.level-pokemon_2.level
    if level_diff<-20 or level_diff>20:
        return False
    return True

class SubmitTrade(APIView):
    def post(self, request, format=None):
        serializer = TradeSerializer(data = request.data)
        if serializer.is_valid():
            if is_trade_valid(serializer.validated_data):#validated data is ordereddict as opposed to dict
                serializer.validated_data['status'] = 'pending'
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("trade rejected by trade validation system", status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
