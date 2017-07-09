from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.spr.models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'correo','nombre','entidad')
