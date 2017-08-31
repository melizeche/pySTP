from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from apps.spr.models import Usuario, Institucion, Nivel, Entidad, UnidadJerarquica, AvanceIndicador
from apps.spr.serializers import UsuarioSerializer, InstitucionSerializer, NivelSerializer, EntidadSerializer, UnidadJerarquicaSerializer, AvanceIndicadorSerializer


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

class AvanceIndicadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = AvanceIndicador.objects.all()
    serializer_class = AvanceIndicadorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('cantidad', 'indicador_id')

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer


class EntidadViewSet(viewsets.ModelViewSet):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'nivel_id')

class UnidadJerarquicaViewSet(viewsets.ModelViewSet):
    queryset = UnidadJerarquica.objects.all()
    serializer_class = UnidadJerarquicaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'entidad','entidad_nivel_id')
