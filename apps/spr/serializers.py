from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.spr.models import Usuario, Institucion, Nivel, Entidad


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'correo', 'nombre', 'entidad')


class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    unidad_responsable = serializers.SerializerMethodField(
        method_name='get_unidad_name')

    @staticmethod
    def get_unidad_name(obj):
        return ""  # ubicaciones = Ubicacion.objects.filter(user_id=obj.user)

    class Meta:
        model = Institucion
        fields = ('id', 'nombre', 'descripcion', 'unidad_responsable_id', 'unidad_responsable', 'base_legal', 'sigla', 'nivel_id', 'entidad_id',
                  'unidad_jerarquica_id', 'unidad_responsable_id', 'abrev', 'mision', 'vision', 'politica', 'diagnostico', 'objetivo', 'usuario_responsable')


class NivelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Nivel
        fields = ('id','numero_fila', 'cod_nivel', 'anho', 'nombre', 'descripcion', 'abrev', 'es_imputable',
                  'fecha_creacion', 'verion', 'borrado', 'fecha_actualizacion', 'fecha_insercion',
                  'usuario_responsable')


class EntidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entidad
        fields = ('id','nombre', 'descripcion', 'anho', 'nivel', 'abrev', 'sigla', 'base_legal',
                  'mision', 'vision', 'politica', 'objetivo', 'diagnostico', 'fecha_creacion',
                  'version', 'numero_fila', 'ruc', 'borrado', 'fecha_actualizacion', 'fecha_insercion',
                  'usuario_responsable')
