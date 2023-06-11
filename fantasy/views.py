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
   # pokemon_to_display = team.pokemon_set.all()
   # data = serializers.serialize('json',list(pokemon_to_display))
   # return HttpResponse(data)

class SubmitTrade(APIView):
    def post(self, request, format=None):
        serializer = TradeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['status'] = 'pending'
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
