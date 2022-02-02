from rest_framework import viewsets
from .serializers import FishSerializer
from .models import Fish

class FishViewSet(viewsets.ModelViewSet):
    serializer_class = FishSerializer
    queryset = Fish.objects.all()
