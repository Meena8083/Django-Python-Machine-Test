from rest_framework import viewsets
from .models import machinetest
from .serializers import machinetestSerializer

class machinetestViewSet(viewsets.ModelViewSet):
    queryset = machinetest.objects.all()
    serializer_class = machinetestSerializer