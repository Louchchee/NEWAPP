from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializers import CounterSerializer
from .models import Counters
from rest_framework.response import Response


@api_view(['GET'])
def countersView(request):
    counters = Counters.objects.all()
    serializer = CounterSerializer(counters, many=True)

    return Response(serializer.data)


