from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.spr.models import Usuario, Institucion


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'correo', 'nombre', 'entidad')


class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    unidad_responsable = serializers.SerializerMethodField(method_name='get_unidad_name')

    @staticmethod
    def get_unidad_name(obj):
        return ""#ubicaciones = Ubicacion.objects.filter(user_id=obj.user)

    class Meta:
        model = Institucion
        fields = ('id', 'nombre', 'descripcion', 'unidad_responsable_id', 'unidad_responsable', 'base_legal', 'sigla', 'nivel_id','entidad_id','unidad_jerarquica_id','unidad_responsable_id','abrev','mision','vision','politica','diagnostico','objetivo','usuario_responsable')
