from rest_framework import serializers
from .models import Candidat


class CadidatAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ('id',
                  'nom',
                  'prenom',
                  'email',
                  'date_naiss',
                  'tel',
                  'disp',
                  'exp',
                  'cv',
                  'msg',
                  )