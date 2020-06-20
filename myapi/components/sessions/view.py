from rest_framework import viewsets
from .model import Session
from .serializer import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('id')
    serializer_class = SessionSerializer
