from rest_framework import viewsets

from .models import Candidat
from .serializers import CadidatAppSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CandidatViewSet(viewsets.ModelViewSet):

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = Candidat.objects.all()
    serializer_class = CadidatAppSerializer
