from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from sagas.serializers import SagaSerializer
from .models import Saga

class SagaView(APIView):
    def get(self, request):
        saga_list = Saga.objects.all().order_by('number')
        serializer = SagaSerializer(saga_list, many=True)
        return Response(serializer.data)

