from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.spr.serializers import UsuarioSerializer
from apps.spr.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
