# from rest_framework import permissions
from rest_framework import viewsets

from .models import Pipe, Valve
from .serializers import PipeSerializer, ValveSerializer


# Create your views here.
class PipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Pipes to be viewed or edited.
    """
    queryset = Pipe.objects.all()
    serializer_class = PipeSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ValveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Valves to be viewed or edited.
    """
    queryset = Valve.objects.all()
    serializer_class = ValveSerializer
    # permission_classes = [permissions.IsAuthenticated]
