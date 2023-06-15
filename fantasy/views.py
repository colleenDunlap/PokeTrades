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

class SubmitTrade(APIView):
    def is_trade_valid(self,trade_data):
        trainer_1 = Trainer.objects.get(id = trade_data["trainer_1"].id)
        trainer_2 = Trainer.objects.get(id = trade_data["trainer_2"].id)
        if not trainer_1.pokemon_set.all().filter(id=trade_data["pokemon_1"].id):
            return False
        if not trainer_2.pokemon_set.all().filter(id=trade_data["pokemon_2"].id):
            return False
        return True
    def post(self, request, format=None):
        serializer = TradeSerializer(data = request.data)
        if serializer.is_valid():
            if self.is_trade_valid(serializer.validated_data):#validated data is ordereddict as opposed to dict
                serializer.validated_data['status'] = 'pending'
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
