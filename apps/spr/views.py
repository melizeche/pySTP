from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from apps.spr.models import Usuario, Institucion, Nivel, Entidad
from apps.spr.serializers import UsuarioSerializer, InstitucionSerializer, NivelSerializer, EntidadSerializer

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

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'nivel_id')
