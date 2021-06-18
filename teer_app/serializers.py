from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Counters


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counters
        fields = '__all__'