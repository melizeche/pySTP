# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or
# field names.
from __future__ import unicode_literals

from django.db import models


class Accion(models.Model):
    costo = models.FloatField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    meta1 = models.FloatField(blank=True, null=True)
    meta2 = models.FloatField(blank=True, null=True)
    meta3 = models.FloatField(blank=True, null=True)
    meta4 = models.FloatField(blank=True, null=True)
    ins_linea_accion_id = models.IntegerField(blank=True, null=True)
    depto_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    id_accion_catalogo = models.ForeignKey(
        'AccionCatalogo', models.DO_NOTHING, db_column='id_accion_catalogo', blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion'


class AccionCatalogo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    id_unidad_medida = models.ForeignKey(
        'UnidadMedida', models.DO_NOTHING, db_column='id_unidad_medida')
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_catalogo'


class AccionCatalogoHasOds(models.Model):
    accion_catalogo = models.OneToOneField(
        AccionCatalogo, models.DO_NOTHING, primary_key=True)
    ods = models.ForeignKey('Ods', models.DO_NOTHING)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_catalogo_has_ods'
        unique_together = (('accion_catalogo', 'ods'),)


class AccionCatalogoHasPnd(models.Model):
    accion_catalogo = models.OneToOneField(
        AccionCatalogo, models.DO_NOTHING, primary_key=True)
    pnd = models.ForeignKey('Pnd', models.DO_NOTHING)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_catalogo_has_pnd'
        unique_together = (('accion_catalogo', 'pnd'),)


class AccionDestinatario(models.Model):
    cantidad = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    beneficiario_tipo_id = models.IntegerField()
    accion_id = models.IntegerField()
    beneficiario_grupo = models.ForeignKey(
        'BeneficiarioGrupo', models.DO_NOTHING, blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_destinatario'
        unique_together = (('id', 'beneficiario_tipo_id', 'accion_id'),)


class AccionHasEtiqueta(models.Model):
    accion_id = models.IntegerField(primary_key=True)
    etiqueta_id = models.IntegerField()
    proporcion = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_has_etiqueta'
        unique_together = (('accion_id', 'etiqueta_id'),)


class AccionHasGeoPoligono(models.Model):
    accion_id = models.IntegerField(primary_key=True)
    geo_poligono_id = models.IntegerField()
    geo_poligono_geo_poligono_id = models.IntegerField()
    geo_poligono_tipo_id = models.IntegerField()
    proporcion = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_has_geo_poligono'
        unique_together = (('accion_id', 'geo_poligono_id',
                            'geo_poligono_geo_poligono_id'),)


class AccionHasProducto(models.Model):
    proporcion = models.IntegerField(blank=True, null=True)
    accion_id = models.IntegerField()
    spr_producto_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    srp_proyecto_id = models.IntegerField()
    spr_subprograma_id = models.IntegerField()
    spr_programa_id = models.IntegerField()
    spr_tiprograma_id = models.IntegerField()
    spr_entidad_id = models.IntegerField()
    spr_nivel_id = models.IntegerField()
    spr_anho = models.IntegerField()
    spr_version = models.IntegerField()
    u_medida = models.TextField(blank=True, null=True)
    cant_fisica = models.FloatField(blank=True, null=True)
    clase = models.TextField(blank=True, null=True)
    cant_financiera = models.FloatField(blank=True, null=True)
    asignacion_financiera = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_has_producto'


class AccionHasResponsable(models.Model):
    accion_id = models.IntegerField(primary_key=True)
    unidad_responsable_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_has_responsable'
        unique_together = (('accion_id', 'unidad_responsable_id'),)


class Actividad(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    proporcion = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    accion = models.ForeignKey(Accion, models.DO_NOTHING)
    unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING)
    hito_tipo = models.ForeignKey('HitoTipo', models.DO_NOTHING)
    acumulable = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    prod_concat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividad'


class AreasAga(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'areas_aga'


class AsignacionPresi(models.Model):
    fila = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    tipo = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    proyecto = models.IntegerField()
    objeto_gasto = models.IntegerField()
    fuente_financiamiento = models.IntegerField()
    organismo_financiador = models.IntegerField()
    pais = models.IntegerField()
    departamento = models.IntegerField()
    producto = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)
    planificado1 = models.FloatField(blank=True, null=True)
    ejecutado1 = models.FloatField(blank=True, null=True)
    planificado2 = models.FloatField(blank=True, null=True)
    ejecutado2 = models.FloatField(blank=True, null=True)
    planificado3 = models.FloatField(blank=True, null=True)
    ejecutado3 = models.FloatField(blank=True, null=True)
    planificado4 = models.FloatField(blank=True, null=True)
    ejecutado4 = models.FloatField(blank=True, null=True)
    planificado5 = models.FloatField(blank=True, null=True)
    ejecutado5 = models.FloatField(blank=True, null=True)
    planificado6 = models.FloatField(blank=True, null=True)
    ejecutado6 = models.FloatField(blank=True, null=True)
    planificado7 = models.FloatField(blank=True, null=True)
    ejecutado7 = models.FloatField(blank=True, null=True)
    planificado8 = models.FloatField(blank=True, null=True)
    ejecutado8 = models.FloatField(blank=True, null=True)
    planificado9 = models.FloatField(blank=True, null=True)
    ejecutado9 = models.FloatField(blank=True, null=True)
    planificado10 = models.FloatField(blank=True, null=True)
    ejecutado10 = models.FloatField(blank=True, null=True)
    planificado11 = models.FloatField(blank=True, null=True)
    ejecutado11 = models.FloatField(blank=True, null=True)
    planificado12 = models.FloatField(blank=True, null=True)
    ejecutado12 = models.FloatField(blank=True, null=True)
    anho = models.IntegerField()
    version = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_presi'


class AsignacionPresiTemp(models.Model):
    fila = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    tipo = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    proyecto = models.IntegerField()
    objeto_gasto = models.IntegerField()
    fuente_financiamiento = models.IntegerField()
    organismo_financiador = models.IntegerField()
    pais = models.IntegerField()
    departamento = models.IntegerField()
    producto = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)
    planificado1 = models.FloatField(blank=True, null=True)
    ejecutado1 = models.FloatField(blank=True, null=True)
    planificado2 = models.FloatField(blank=True, null=True)
    ejecutado2 = models.FloatField(blank=True, null=True)
    planificado3 = models.FloatField(blank=True, null=True)
    ejecutado3 = models.FloatField(blank=True, null=True)
    planificado4 = models.FloatField(blank=True, null=True)
    ejecutado4 = models.FloatField(blank=True, null=True)
    planificado5 = models.FloatField(blank=True, null=True)
    ejecutado5 = models.FloatField(blank=True, null=True)
    planificado6 = models.FloatField(blank=True, null=True)
    ejecutado6 = models.FloatField(blank=True, null=True)
    planificado7 = models.FloatField(blank=True, null=True)
    ejecutado7 = models.FloatField(blank=True, null=True)
    planificado8 = models.FloatField(blank=True, null=True)
    ejecutado8 = models.FloatField(blank=True, null=True)
    planificado9 = models.FloatField(blank=True, null=True)
    ejecutado9 = models.FloatField(blank=True, null=True)
    planificado10 = models.FloatField(blank=True, null=True)
    ejecutado10 = models.FloatField(blank=True, null=True)
    planificado11 = models.FloatField(blank=True, null=True)
    ejecutado11 = models.FloatField(blank=True, null=True)
    planificado12 = models.FloatField(blank=True, null=True)
    ejecutado12 = models.FloatField(blank=True, null=True)
    anho = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    sumprog = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_presi_temp'
        unique_together = (('anho', 'version', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto',
                            'objeto_gasto', 'fuente_financiamiento', 'organismo_financiador', 'pais', 'departamento', 'producto'),)


class Avance(models.Model):
    justificacion = models.TextField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    cantidad_beneficiarios = models.IntegerField(blank=True, null=True)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    distrito_avance = models.IntegerField(blank=True, null=True)
    departamento_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avance'


class AvanceCosto(models.Model):
    monto = models.FloatField(blank=True, null=True)
    codigo_contratacionl = models.TextField(blank=True, null=True)
    objeto_gasto = models.IntegerField(blank=True, null=True)
    avance = models.ForeignKey(Avance, models.DO_NOTHING)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    producto_concat = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avance_costo'


class AvanceCualitativo(models.Model):
    id = models.AutoField(primary_key=True)
    accion_catalogo = models.ForeignKey(
        AccionCatalogo, models.DO_NOTHING, blank=True, null=True)
    ins_linea_accion = models.ForeignKey(
        'InsLineaAccion', models.DO_NOTHING, blank=True, null=True)
    trimestre = models.ForeignKey(
        'Trimestre', models.DO_NOTHING, blank=True, null=True)
    gestiones_realizadas = models.TextField(blank=True, null=True)
    principales_logros_alcanzados = models.TextField(blank=True, null=True)
    dificultades_lecciones_aprendidas = models.TextField(blank=True, null=True)
    objetivos_del_siguiente_trimestre = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avance_cualitativo'


class Avanceshito(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    url = models.CharField(max_length=50)
    fecha = models.DateField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avanceshito'


class Beneficiario(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    beneficiario_tipo_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    cantidad = models.IntegerField(blank=True, null=True)
    avance = models.ForeignKey(
        Avance, models.DO_NOTHING, blank=True, null=True)
    beneficiario_grupo = models.ForeignKey(
        'BeneficiarioGrupo', models.DO_NOTHING, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiario'


class BeneficiarioDetalle(models.Model):
    valor = models.TextField(blank=True, null=True)
    beneficiario_detalle_claves_id = models.IntegerField()
    beneficiario_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiario_detalle'


class BeneficiarioDetalleClave(models.Model):
    clave = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiario_detalle_clave'


class BeneficiarioGrupo(models.Model):
    tipo_beneficiario_grupo = models.ForeignKey(
        'BeneficiarioTipo', models.DO_NOTHING)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiario_grupo'


class BeneficiarioTipo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiario_tipo'


class CiDestinatarios(models.Model):
    id = models.AutoField(primary_key=True)
    avance_id = models.IntegerField(blank=True, null=True)
    ci = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    estado_civil = models.TextField(blank=True, null=True)
    nacionalidad = models.TextField(blank=True, null=True)
    profesion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ci_destinatarios'


class Clase(models.Model):
    codigo = models.CharField(unique=True, max_length=30)
    descripcion = models.CharField(max_length=100)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clase'


class Departamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    paisid = models.ForeignKey(
        'Pais', models.DO_NOTHING, db_column='paisid', blank=True, null=True)
    gobernador_id = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DimFecha(models.Model):
    dim_fecha_pk = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    dia = models.SmallIntegerField(blank=True, null=True)
    mes = models.SmallIntegerField(blank=True, null=True)
    mesano_texto = models.TextField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    administracion = models.TextField(blank=True, null=True)
    trimestre = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dim_fecha'


class Distrito(models.Model):
    departamentoid = models.OneToOneField(
        Departamento, models.DO_NOTHING, db_column='departamentoid', primary_key=True)
    id = models.IntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    intendente_id = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'distrito'
        unique_together = (('departamentoid', 'id'),)


class Documento(models.Model):
    nombre = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Empresa(models.Model):
    razon_social = models.CharField(max_length=1000)
    localid = models.IntegerField(blank=True, null=True)
    capsocial = models.DecimalField(
        max_digits=18, decimal_places=2, blank=True, null=True)
    tiponegocioid = models.ForeignKey(
        'Tiponegocio', models.DO_NOTHING, db_column='tiponegocioid', blank=True, null=True)
    claseid = models.ForeignKey(
        Clase, models.DO_NOTHING, db_column='claseid', blank=True, null=True)
    naturaleza = models.CharField(max_length=100, blank=True, null=True)
    fechainicio = models.DateField(blank=True, null=True)
    ruc = models.CharField(unique=True, max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    contrasenha = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    tipo_sociedad = models.IntegerField(blank=True, null=True)
    rubro = models.IntegerField(blank=True, null=True)
    fecha_constitucion = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    valido = models.CharField(max_length=1, blank=True, null=True)
    siglas = models.CharField(max_length=10, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EntidadSpr(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    nivel_id = models.IntegerField()
    abrev = models.CharField(max_length=45, blank=True, null=True)
    sigla = models.CharField(max_length=45, blank=True, null=True)
    base_legal = models.TextField(blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    politica = models.TextField(blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    ruc = models.TextField(blank=True, null=True)
    borrado = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad_spr'


class Etiqueta(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etiqueta'


class Evidencia(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    ws = models.ForeignKey('Ws', models.DO_NOTHING)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    avance = models.ForeignKey(Avance, models.DO_NOTHING)
    url_documento = models.TextField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evidencia'


class EvidenciaHasDocumento(models.Model):
    evidencia = models.OneToOneField(
        Evidencia, models.DO_NOTHING, primary_key=True)
    documento = models.ForeignKey(Documento, models.DO_NOTHING)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evidencia_has_documento'
        unique_together = (('evidencia', 'documento'),)


class GeoDgeec(models.Model):
    dgeec_id = models.TextField(blank=True, null=True)
    departamento_id = models.IntegerField(blank=True, null=True)
    departamento = models.TextField(blank=True, null=True)
    distrito_id = models.IntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    bar_loc_id = models.IntegerField(blank=True, null=True)
    barrio_localidad = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_dgeec'


class GeoPoligono(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    geo = models.TextField(blank=True, null=True)
    geo_poligono_id = models.IntegerField()
    geo_poligono_tipo_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_poligono'


class GeoPoligonoTipo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_poligono_tipo'


class GrupoSubgrupoObjetoGasto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.TextField(blank=True, null=True)
    es_imputable = models.TextField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    grupo = models.FloatField(blank=True, null=True)
    subgrupo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo_subgrupo_objeto_gasto'


class Hito(models.Model):
    id = models.AutoField(primary_key=True)
    ins_linea_accion_id = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    unidad_medida_id = models.IntegerField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    hito_tipo_id = models.IntegerField()
    accion_id = models.IntegerField()
    evidencia_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hito'


class HitoHasBeneficiario(models.Model):
    hito_id = models.IntegerField(primary_key=True)
    hito_accion_id = models.IntegerField()
    beneficiario_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hito_has_beneficiario'
        unique_together = (('hito_id', 'hito_accion_id', 'beneficiario_id'),)


class HitoTipo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hito_tipo'


class Hitoprueba(models.Model):
    id = models.AutoField(primary_key=True)
    accion = models.TextField(blank=True, null=True)
    nombrehito = models.TextField(blank=True, null=True)
    tipohito = models.TextField(blank=True, null=True)
    unidadmedida = models.TextField(blank=True, null=True)
    cantidadprevista = models.BigIntegerField(blank=True, null=True)
    cantidadreal = models.BigIntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hitoprueba'


class InsLineaAccion(models.Model):
    linea_accion_id = models.IntegerField()
    institucion_id = models.IntegerField()
    periodo_id = models.IntegerField()
    meta = models.FloatField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_linea_accion'


class InsLineaAccionHasEtiqueta(models.Model):
    ins_linea_accion = models.OneToOneField(
        InsLineaAccion, models.DO_NOTHING, primary_key=True)
    etiqueta = models.ForeignKey(Etiqueta, models.DO_NOTHING)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_linea_accion_has_etiqueta'
        unique_together = (('ins_linea_accion', 'etiqueta'),)


class Institucion(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    sigla = models.TextField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    nivel_id = models.IntegerField(blank=True, null=True)
    entidad_id = models.IntegerField(blank=True, null=True)
    unidad_jerarquica_id = models.IntegerField(blank=True, null=True)
    unidad_responsable_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institucion'


class LaHasAreasAga(models.Model):
    linea_accion = models.OneToOneField(
        'LineaAccion', models.DO_NOTHING, primary_key=True)
    areas_aga = models.ForeignKey(AreasAga, models.DO_NOTHING)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'la_has_areas_aga'
        unique_together = (('linea_accion', 'areas_aga'),)


class LaHasOds(models.Model):
    linea_accion = models.OneToOneField(
        'LineaAccion', models.DO_NOTHING, primary_key=True)
    ods = models.ForeignKey('Ods', models.DO_NOTHING)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'la_has_ods'
        unique_together = (('linea_accion', 'ods'),)


class LaHasPnd(models.Model):
    linea_accion = models.OneToOneField(
        'LineaAccion', models.DO_NOTHING, primary_key=True)
    pnd = models.ForeignKey('Pnd', models.DO_NOTHING)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'la_has_pnd'
        unique_together = (('linea_accion', 'pnd'),)


class LineaAccion(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    acumular = models.NullBooleanField()
    tipo_accion_id = models.IntegerField()
    estrategia_id = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    orden = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linea_accion'


class LineaEstrategica(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linea_estrategica'


class Ods(models.Model):
    nombre = models.TextField(blank=True, null=True)
    abrev = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ods'


class Pais(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    nacionalidad = models.CharField(max_length=200, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Periodo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'periodo'


class Pnd(models.Model):
    nombre = models.TextField(blank=True, null=True)
    abrev = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pnd'


class PoblacionConLocalizacionYSituacionDePobreza090816Actual(models.Model):
    depto_cod = models.TextField(blank=True, null=True)
    depto_desc = models.TextField(blank=True, null=True)
    dist_cod = models.TextField(blank=True, null=True)
    barloc_cod = models.TextField(blank=True, null=True)
    dist_desc = models.TextField(blank=True, null=True)
    barloc_desc_localidad = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    manzana = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    nro_casa = models.TextField(blank=True, null=True)
    coordenada_x = models.TextField(blank=True, null=True)
    coordenada_y = models.TextField(blank=True, null=True)
    n_persona = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    apellido = models.TextField(blank=True, null=True)
    edad = models.TextField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    parentesco = models.TextField(blank=True, null=True)
    jefe = models.TextField(blank=True, null=True)
    dia = models.TextField(blank=True, null=True)
    mes = models.TextField(blank=True, null=True)
    ano = models.TextField(blank=True, null=True)
    nro_cedula = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    estado_de_pobreza = models.TextField(blank=True, null=True)
    ano_apliacion_ficha = models.TextField(blank=True, null=True)
    the_geom = models.FloatField(blank=True, null=True)
    cartodb_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    the_geom_webmercator = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poblacion_con_localizacion_y_situacion_de_pobreza_090816_actual'


class Producto(models.Model):
    oid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    clase = models.TextField(blank=True, null=True)
    unidad_medida_id = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoPresupuestoFinanciero(models.Model):
    id = models.FloatField(primary_key=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    grupo_objeto_gasto_id = models.IntegerField(blank=True, null=True)
    subgrupo_objeto_gasto_id = models.IntegerField(blank=True, null=True)
    objeto_gasto_id = models.IntegerField(blank=True, null=True)
    fuente_id = models.IntegerField(blank=True, null=True)
    funcional_id = models.IntegerField(blank=True, null=True)
    funcional_nombre = models.CharField(
        max_length=21845, blank=True, null=True)
    departamento_id = models.IntegerField(blank=True, null=True)
    producto_id = models.IntegerField(blank=True, null=True)
    producto_nombre = models.CharField(max_length=21845, blank=True, null=True)
    unidad_medida_id = models.IntegerField(blank=True, null=True)
    nombre_unidad_medida = models.CharField(
        max_length=21845, blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    snip = models.IntegerField(blank=True, null=True)
    meta = models.FloatField(blank=True, null=True)
    asignacion = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_financiero'


class Programacion(models.Model):
    cantidad = models.FloatField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING)
    id = models.AutoField(primary_key=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programacion'


class SprProducto(models.Model):
    nivel_id = models.IntegerField(blank=True, null=True)
    entidad_id = models.IntegerField(blank=True, null=True)
    tipo_id = models.IntegerField(blank=True, null=True)
    progama_id = models.IntegerField(blank=True, null=True)
    subprograma_id = models.IntegerField(blank=True, null=True)
    proyecto_id = models.IntegerField(blank=True, null=True)
    funcional_id = models.IntegerField(blank=True, null=True)
    unidad_responsable_id = models.IntegerField(blank=True, null=True)
    producto_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spr_producto'


class Tareas(models.Model):
    id = models.IntegerField(primary_key=True)
    asunto = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    tareas_padre = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True, related_name='tareaspadre')
    dias = models.IntegerField(blank=True, null=True)
    porcentaje_avance = models.IntegerField(blank=True, null=True)
    justificacion = models.TextField(blank=True, null=True)
    tareas_estados = models.ForeignKey('TareasEstados', models.DO_NOTHING)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'


class TareasEstados(models.Model):
    nombre = models.TextField(blank=True, null=True)
    decripcion = models.TextField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas_estados'


class TareasHasInstitucion(models.Model):
    tareas = models.OneToOneField(Tareas, models.DO_NOTHING, primary_key=True)
    institucion = models.ForeignKey(Institucion, models.DO_NOTHING)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas_has_institucion'
        unique_together = (('tareas', 'institucion'),)


class TareasHasTareas(models.Model):
    tareas = models.OneToOneField(
        Tareas, models.DO_NOTHING, primary_key=True, related_name='tareas')
    tareas_id1 = models.ForeignKey(
        Tareas, models.DO_NOTHING, db_column='tareas_id1')
    tipores_relaciones = models.ForeignKey(
        'TiposRelaciones', models.DO_NOTHING)
    usuario_responsable = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas_has_tareas'
        unique_together = (('tareas', 'tareas_id1'),)


class TareasHasUsuario(models.Model):
    tareas = models.OneToOneField(Tareas, models.DO_NOTHING, primary_key=True)
    usuario_correo = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_correo')
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas_has_usuario'
        unique_together = (('tareas', 'usuario_correo'),)


class TipoAccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_accion'


class TipoSociedad(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_sociedad'


class Tiponegocio(models.Model):
    descripcion = models.CharField(unique=True, max_length=100)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiponegocio'


class TiposRelaciones(models.Model):
    nombre = models.TextField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_relaciones'


class Trimestre(models.Model):
    nro = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trimestre'
        unique_together = (('nro', 'anho'),)


class UnidadMedida(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    sigla = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.TextField(primary_key=True)
    passwd = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    entidad = models.TextField(blank=True, null=True)
    role_id = models.IntegerField()
    entidad_id = models.IntegerField(blank=True, null=True)
    nivel_id = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    urlimagen = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    email_real = models.CharField(
        max_length=256, blank=True, null=True, default='true')
    unr_id = models.IntegerField(blank=True, null=True)
    role_id_movil = models.IntegerField(blank=True, null=True)
    role_id_tablero = models.IntegerField(blank=True, null=True)
    role_identificaciones = models.IntegerField(blank=True, null=True)
    borrado = models.CharField(
        max_length=256, blank=True, null=True, default='false')
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioEtiqueta(models.Model):
    usuario_correo = models.TextField()
    etiqueta_id = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'usuario_etiqueta'
        unique_together = (('usuario_correo', 'etiqueta_id'),)


class UsuarioLineaAccion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_correo = models.TextField()
    linea_accion_id = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'usuario_linea_accion'
        unique_together = (('usuario_correo', 'linea_accion_id'),)


class UsuarioSpr(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.TextField(blank=True, null=True)
    passwd = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    entidad = models.TextField(blank=True, null=True)
    role_id = models.IntegerField()
    entidad_id = models.IntegerField(blank=True, null=True)
    nivel_id = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    urlimagen = models.TextField(blank=True, null=True)
    unr_id = models.IntegerField()
    borrado = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    role_id_movil = models.IntegerField()
    role_id_tablero = models.IntegerField()
    role_identificaciones = models.IntegerField()
    email_real = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_spr'


class UsuarioTablero(models.Model):
    correo = models.TextField()
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    uni_responsable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_tablero'


class Ws(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    metodo = models.TextField(blank=True, null=True)
    usuario = models.TextField(blank=True, null=True)
    # Field renamed because it was a Python reserved word.
    pass_field = models.TextField(db_column='pass', blank=True, null=True)
    id_clave = models.TextField(blank=True, null=True)
    id_valor = models.TextField(blank=True, null=True)
    ws_tipo_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws'


class WsAccion(models.Model):
    linea_accion_id = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    institucion_id = models.IntegerField(blank=True, null=True)
    accion_id = models.IntegerField(blank=True, null=True)
    dpto_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    meta_trim1 = models.IntegerField(blank=True, null=True)
    meta_trim2 = models.IntegerField(blank=True, null=True)
    meta_trim3 = models.IntegerField(blank=True, null=True)
    meta_trim4 = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_accion'


class WsCronograma(models.Model):
    linea_accion_id = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    institucion_id = models.IntegerField(blank=True, null=True)
    accion_id = models.IntegerField(blank=True, null=True)
    dpto_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    cronograma_tipo_id = models.IntegerField(blank=True, null=True)
    cronograma_um_id = models.IntegerField(blank=True, null=True)
    cronograma_nombre = models.TextField(blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    proporcion = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_cronograma'


class WsHito(models.Model):
    linea_accion_id = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    institucion_id = models.IntegerField(blank=True, null=True)
    accion_id = models.IntegerField(blank=True, null=True)
    dpto_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    cronograma_id = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_hito'


class WsProducto(models.Model):
    id = models.AutoField(primary_key=True)
    clase = models.CharField(max_length=1, blank=True, null=True)
    unidad_medida_id = models.IntegerField()
    nombre = models.CharField(max_length=21845, blank=True, null=True)
    descripcion = models.CharField(max_length=21845, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_producto'


class WsTipo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ws_tipo'
