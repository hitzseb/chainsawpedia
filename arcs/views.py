from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Arc
from .serializers import ArcSerializer

class ArcView(APIView):
    def get(self, request):
        arc_list = Arc.objects.all().order_by('number')
        serializer = ArcSerializer(arc_list, many=True)
        return Response(serializer.data)