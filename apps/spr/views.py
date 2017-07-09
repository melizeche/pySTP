from django.shortcuts import render
from rest_framework import viewsets, permissions
from apps.spr.serializers import UsuarioSerializer, InstitucionSerializer
from apps.spr.models import Usuario, Institucion


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
