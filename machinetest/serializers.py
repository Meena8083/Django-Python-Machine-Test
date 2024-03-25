
from rest_framework import serializers
from .models import machinetest
class machinetestSerializer(serializers.ModelSerializer):
    class Meta:
        model = machinetest
        fields = '__all__'
