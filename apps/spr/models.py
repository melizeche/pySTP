# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccionHasProducto(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
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


class AccionHasProductoHasPresupuesto(models.Model):
    codigoobjetogasto = models.IntegerField(blank=True, null=True)
    id_accion_has_producto = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accion_has_producto_has_presupuesto'


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
    anho = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_presi'
        unique_together = (('anho', 'version', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto', 'objeto_gasto', 'fuente_financiamiento', 'organismo_financiador', 'pais', 'departamento', 'producto'), ('anho', 'version', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto', 'objeto_gasto', 'fuente_financiamiento', 'organismo_financiador', 'pais', 'departamento', 'producto'),)


class AsignacionPresiAnt(models.Model):
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
        db_table = 'asignacion_presi_ant'


class AsignacionPresiN(models.Model):
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
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_presi_n'
        unique_together = (('anho', 'version', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto', 'objeto_gasto', 'fuente_financiamiento', 'organismo_financiador', 'pais', 'departamento', 'producto'),)


class AsignacionPresiShadow(models.Model):
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
        db_table = 'asignacion_presi_shadow'


class Asignfinanproducto(models.Model):
    numerofila = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    codorigen = models.IntegerField(blank=True, null=True)
    coddetalle = models.IntegerField(blank=True, null=True)
    fuentefinanc = models.IntegerField(blank=True, null=True)
    montoprogramado = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignfinanproducto'


class AsignfinanproductoPresi(models.Model):
    numerofila = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    codorigen = models.IntegerField(blank=True, null=True)
    coddetalle = models.IntegerField(blank=True, null=True)
    fuentefinanc = models.IntegerField(blank=True, null=True)
    montoprogramado = models.FloatField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignfinanproducto_presi'


class AvanceIndicador(models.Model):
    cantidad = models.TextField(blank=True, null=True)
    vencimiento = models.TextField(blank=True, null=True)
    indicador_id = models.IntegerField()
    zona_geografica_id = models.IntegerField()
    demografia_id = models.IntegerField()
    borrado_int = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    borrado = models.NullBooleanField()
    producto_concat = models.TextField()
    objetivo_id = models.IntegerField()
    tipo_objetivo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'avance_indicador'
        unique_together = (('id', 'indicador_id', 'zona_geografica_id', 'demografia_id', 'objetivo_id', 'tipo_objetivo_id', 'nivel', 'entidad'),)


class CatalogoDestinatario(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_catalogo_destinatario = models.ForeignKey('TipoCatalogoDestinatario', models.DO_NOTHING)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_destinatario'
        unique_together = (('id', 'tipo_catalogo_destinatario'),)


class CatalogoDncp(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    objeto_de_gasto = models.ForeignKey('ObjetoDeGasto', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_dncp'
        unique_together = (('id', 'objeto_de_gasto'),)


class CoberturaDemograficaAlcances(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobertura_demografica_alcances'


class CoberturaGeograficaAlcances(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobertura_geografica_alcances'


class Demografia(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descipcion = models.TextField(blank=True, null=True)
    tipo_demografica = models.ForeignKey('TipoDemografica', models.DO_NOTHING)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demografia'
        unique_together = (('id', 'tipo_demografica'),)


class Departamento(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    pais = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DiccionarioCampos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()
    referencia_html = models.TextField()
    formulario = models.ForeignKey('DiccionarioFormularios', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diccionario_campos'


class DiccionarioDato(models.Model):
    clase = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    titulo = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    instructivo = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diccionario_dato'


class DiccionarioFormularios(models.Model):
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'diccionario_formularios'


class DictamenStp(models.Model):
    id = models.AutoField(primary_key=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    eleccion = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    url_documento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dictamen_stp'


class DimFecha(models.Model):
    dim_fecha_pk = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
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
    id = models.IntegerField(primary_key=True)
    departamento_id = models.IntegerField()
    distrito_id = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distrito'
        unique_together = (('id', 'departamento_id', 'distrito_id'),)


class Documentos(models.Model):
    nombre = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_valides = models.DateField(blank=True, null=True)
    tipos_id = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class EjeEstrategico(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    plan = models.ForeignKey('Plan', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eje_estrategico'
        unique_together = (('id', 'plan'),)


class Entidad(models.Model):
    #oid = models.IntegerField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING)
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
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " - " + self.nombre
    class Meta:
        managed = False
        db_table = 'entidad'
        unique_together = (('id', 'nivel'),)


class Estrategia(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    eje_estrategico_id = models.IntegerField()
    linea_transversal_id = models.IntegerField()
    plan = models.IntegerField()
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estrategia'
        unique_together = (('id', 'eje_estrategico_id', 'linea_transversal_id', 'plan'),)


class EstrategiaHasObjetivo(models.Model):
    id = models.AutoField(primary_key=True)
    estrategia_id = models.IntegerField()
    estrategia_eje_estrategico_id = models.IntegerField()
    estrategia_linea_transversal_id = models.IntegerField()
    objetivo_id = models.IntegerField()
    objetivo_tipo_objetivo_id = models.IntegerField()
    es_principal = models.NullBooleanField()
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estrategia_has_objetivo'


class EstructuraProgramatica(models.Model):
    anho = models.IntegerField()
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    tipo = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    proyecto = models.IntegerField()
    nfprograma = models.IntegerField()
    nfsubprograma = models.IntegerField()
    nfproyecto = models.IntegerField()
    departamento = models.IntegerField()
    unidad_responsable = models.IntegerField()
    funcional = models.ForeignKey('Funcional', models.DO_NOTHING, db_column='funcional')
    diagnostico = models.TextField()
    objetivo = models.TextField()
    resultado_esperado = models.TextField()
    base_legal = models.TextField()
    nombre = models.TextField()
    abrev = models.TextField()
    descripcion = models.TextField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estructura_programatica'
        unique_together = (('id', 'anho', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto', 'funcional'),)


class Etiquetas(models.Model):
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'etiquetas'


class FuenteFinanciamiento(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuente_financiamiento'


class FuenteVerificacion(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuente_verificacion'


class Funcional(models.Model):
    numero_fila = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    es_imputable = models.CharField(max_length=1, blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcional'


class FundamentacionPresi(models.Model):
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
    secuencia = models.IntegerField()
    precio = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    cantmeses = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    clg = models.IntegerField()
    anho = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fundamentacion_presi'
        unique_together = (('anho', 'version', 'nivel', 'entidad', 'tipo', 'programa', 'subprograma', 'proyecto', 'objeto_gasto', 'fuente_financiamiento', 'organismo_financiador', 'pais', 'departamento', 'clg', 'secuencia'),)


class FundamentaciongastoPresi(models.Model):
    numerofila = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    codigoprograma = models.IntegerField(blank=True, null=True)
    codigosubprograma = models.IntegerField(blank=True, null=True)
    codigoproyecto = models.IntegerField(blank=True, null=True)
    objetogasto = models.IntegerField(blank=True, null=True)
    fuente = models.IntegerField(blank=True, null=True)
    orgfinanciador = models.IntegerField(blank=True, null=True)
    pais = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    cantmeses = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    clgcodigo = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fundamentaciongasto_presi'


class Indicador(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_indicador_id = models.IntegerField()
    metodo_calculo_id_int = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    frecuencia_meses = models.IntegerField(blank=True, null=True)
    desagregacion_tipo_zona_geografica_id = models.IntegerField()
    tipo_demografica_id = models.IntegerField()
    fuente_verificacion_id_old = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    objetivo_id = models.IntegerField()
    borrado_int = models.IntegerField(blank=True, null=True)
    cobertura_geografica_alcance = models.IntegerField(blank=True, null=True)
    nivel_despliegue_geografico = models.IntegerField(blank=True, null=True)
    cobertura_demografica_alcance = models.IntegerField(blank=True, null=True)
    nivel_despliegue_demografica = models.IntegerField(blank=True, null=True)
    institucion_responsable_calculo_indicador = models.TextField(blank=True, null=True)
    evaluacion_heci = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)
    fecha_disponibilidad_informacion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    fuente_verificacion_id = models.TextField()
    metodo_calculo_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador'
        unique_together = (('id', 'tipo_indicador_id', 'unidad_medida_id', 'desagregacion_tipo_zona_geografica_id', 'tipo_demografica_id', 'objetivo_id', 'nivel', 'entidad'),)


class IndicadorN(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_indicador_id = models.IntegerField()
    metodo_calculo_id_int = models.IntegerField(blank=True, null=True)
    unidad_medida_id = models.IntegerField(blank=True, null=True)
    frecuencia_meses = models.IntegerField(blank=True, null=True)
    desagregacion_tipo_zona_geografica_id = models.IntegerField()
    tipo_demografica_id = models.IntegerField()
    fuente_verificacion_id_old = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    objetivo_id = models.IntegerField()
    borrado_int = models.IntegerField(blank=True, null=True)
    cobertura_geografica_alcance = models.IntegerField(blank=True, null=True)
    nivel_despliegue_geografico = models.IntegerField(blank=True, null=True)
    cobertura_demografica_alcance = models.IntegerField(blank=True, null=True)
    nivel_despliegue_demografica = models.IntegerField(blank=True, null=True)
    institucion_responsable_calculo_indicador = models.TextField(blank=True, null=True)
    evaluacion_heci = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)
    fecha_disponibilidad_informacion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    fuente_verificacion_id = models.TextField(blank=True, null=True)
    metodo_calculo_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_n'


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
    abrev = models.TextField(blank=True, null=True)
    base_legal = models.TextField(blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    politica = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    ruc = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    nro_fila = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institucion'


class Justificacion(models.Model):
    id = models.AutoField(primary_key=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'justificacion'


class LineaTransversal(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    plan = models.ForeignKey('Plan', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linea_transversal'
        unique_together = (('id', 'plan'),)


class Mes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes'


class Meta(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.TextField(blank=True, null=True)
    vencimiento = models.TextField(blank=True, null=True)
    indicador_id = models.IntegerField()
    zona_geografica_id = models.IntegerField()
    demografia_id = models.IntegerField()
    borrado_int = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    producto_concat = models.TextField()
    objetivo_id = models.IntegerField(blank=True, null=True)
    tipo_objetivo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta'


class Meta1(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.TextField(blank=True, null=True)
    vencimiento = models.TextField(blank=True, null=True)
    indicador_id = models.IntegerField()
    zona_geografica_id = models.IntegerField()
    demografia_id = models.IntegerField()
    borrado_int = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    b = models.TextField(blank=True, null=True)
    producto_concat = models.TextField(blank=True, null=True)
    objetivo_id = models.IntegerField(blank=True, null=True)
    tipo_objetivo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta1'


class MetodoCalculo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    clase = models.CharField(max_length=1, blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metodo_calculo'


class Modulo(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class ModuloHasPermiso(models.Model):
    role = models.ForeignKey('Role', models.DO_NOTHING, primary_key=True)
    modulo = models.ForeignKey(Modulo, models.DO_NOTHING)
    permiso = models.ForeignKey('Permiso', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_has_permiso'
        unique_together = (('role', 'modulo', 'permiso'),)


class Modulos(models.Model):
    nombre = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulos'


class Nivel(models.Model):
    numero_fila = models.IntegerField(blank=True, null=True)
    cod_nivel = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    es_imputable = models.CharField(max_length=1, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    verion = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel'


class NivelDespliegueDemograficaDesagregacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_despliegue_demografica_desagregacion'


class NivelDespliegueGeograficaDesagregaciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_despliegue_geografica_desagregaciones'


class Objetivo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_objetivo = models.ForeignKey('TipoObjetivo', models.DO_NOTHING)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    funcional = models.IntegerField(blank=True, null=True)
    borrado_int = models.IntegerField(blank=True, null=True)
    version = models.IntegerField()
    anho = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo'
        unique_together = (('id', 'tipo_objetivo', 'version', 'anho'),)


class ObjetivoAbreviacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        managed = False
        db_table = 'objetivo_abreviacion'


class ObjetivoCatalogo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    tipo_objetivo = models.ForeignKey('TipoObjetivo', models.DO_NOTHING)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_catalogo'
        unique_together = (('id', 'tipo_objetivo'),)


class ObjetivoHasIndicador(models.Model):
    objetivo_id = models.IntegerField(primary_key=True)
    objetivo_tipo_objetivo_id = models.IntegerField()
    objetivo_anho = models.IntegerField()
    objetivo_version = models.IntegerField()
    indicador_id = models.IntegerField()
    indicador_tipo_indicador_id = models.IntegerField(blank=True, null=True)
    indicador_unidad_medida_id = models.IntegerField(blank=True, null=True)
    indicador_desagregacion_tipo_zona_geografica_id = models.IntegerField(blank=True, null=True)
    indicador_tipo_demografica_id = models.IntegerField(blank=True, null=True)
    indicador_fuente_verificacion_id_old = models.IntegerField(blank=True, null=True)
    indicador_objetivo_id = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    producto_concat = models.TextField()
    indicador_fuente_verificacion_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'objetivo_has_indicador'
        unique_together = (('objetivo_id', 'objetivo_tipo_objetivo_id', 'objetivo_anho', 'objetivo_version', 'indicador_id', 'producto_concat'),)


class ObjetivoHasObjetivo(models.Model):
    objetivo = models.ForeignKey(Objetivo, models.DO_NOTHING, primary_key=True)
    objetivo_tipo_objetivo_id = models.IntegerField()
    objetivo_anho = models.IntegerField()
    objetivo_version = models.IntegerField()
    objetivo_rel = models.ForeignKey(Objetivo, models.DO_NOTHING, related_name='objetivorel')
    objetivo_rel_tipo_objetivo_id = models.IntegerField()
    objetivo_rel_anho = models.IntegerField()
    objetivo_rel_version = models.IntegerField()
    colaboracion = models.FloatField(blank=True, null=True)
    influencia = models.FloatField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    unidad_responsable = models.IntegerField(blank=True, null=True)
    producto_concat = models.TextField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_has_objetivo'
        unique_together = (('objetivo', 'objetivo_tipo_objetivo_id', 'objetivo_anho', 'objetivo_version', 'objetivo_rel', 'objetivo_rel_tipo_objetivo_id', 'objetivo_rel_anho', 'objetivo_rel_version', 'producto_concat'),)


class ObjetivoSugerido(models.Model):
    objetivo = models.ForeignKey(Objetivo, models.DO_NOTHING, primary_key=True)
    objetivo_tipo_objetivo_id = models.IntegerField()
    objetivo_anho = models.IntegerField()
    objetivo_version = models.IntegerField()
    objetivo_sugerido = models.ForeignKey(Objetivo, models.DO_NOTHING, related_name='objetivosuge')
    objetivo_sugerido_tipo_id = models.IntegerField()
    objetivo_sugerido_anho = models.IntegerField()
    objetivo_sugerido_version = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objetivo_sugerido'
        unique_together = (('objetivo', 'objetivo_tipo_objetivo_id', 'objetivo_anho', 'objetivo_version', 'objetivo_sugerido', 'objetivo_sugerido_tipo_id', 'objetivo_sugerido_anho', 'objetivo_sugerido_version'),)


class ObjetoDeGasto(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    es_imputable = models.CharField(max_length=1, blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objeto_de_gasto'


class OrganismoFinanciador(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organismo_financiador'


class Permiso(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permiso'


class PermisosModulos(models.Model):
    nombre = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos_modulos'


class PermisosPorModulos(models.Model):
    id = models.AutoField(primary_key=True)
    modulos = models.ForeignKey(Modulos, models.DO_NOTHING, primary_key=True)
    usuario_id = models.IntegerField()
    permisos_modulos = models.ForeignKey(PermisosModulos, models.DO_NOTHING)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos_por_modulos'
        unique_together = (('modulos', 'usuario_id'),)


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    detalle = models.CharField(max_length=50, blank=True, null=True)
    entidad_responsable = models.IntegerField()
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class PnpPgn2016(models.Model):
    ani_aniopre = models.IntegerField()
    nen_codigo = models.IntegerField()
    ent_codigo = models.IntegerField()
    tip_codigo = models.IntegerField()
    pro_codigo = models.IntegerField()
    sub_codigo = models.IntegerField()
    pry_codigo = models.IntegerField()
    obj_codigo = models.IntegerField()
    fue_codigo = models.IntegerField()
    fin_codigo = models.IntegerField()
    vrs_codigo = models.IntegerField()
    pai_codigo = models.IntegerField()
    dpt_codigo = models.IntegerField()
    ver_desembolso = models.IntegerField()
    ver_contrnac = models.IntegerField()
    ver_programado = models.IntegerField()
    ver_fching = models.DateTimeField()
    ver_usring = models.TextField(blank=True, null=True)
    ver_fchact = models.DateTimeField()
    ver_usract = models.TextField()
    ver_justifica = models.TextField(blank=True, null=True)
    ver_destino = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pnp_pgn_2016'


class PresupuestoGasto(models.Model):
    codigonivel = models.IntegerField(blank=True, null=True)
    codigoentidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    codigoprograma = models.IntegerField(blank=True, null=True)
    codigosubprograma = models.IntegerField(blank=True, null=True)
    codigoproyecto = models.IntegerField(blank=True, null=True)
    codigoobjetogasto = models.IntegerField(blank=True, null=True)
    codigofuentefinan = models.IntegerField(blank=True, null=True)
    codigoorgfinanciador = models.IntegerField(blank=True, null=True)
    codigodpto = models.IntegerField(blank=True, null=True)
    codigopais = models.IntegerField(blank=True, null=True)
    aprobado = models.FloatField(blank=True, null=True)
    modificaciones = models.FloatField(blank=True, null=True)
    vigente = models.FloatField(blank=True, null=True)
    planfinanciero = models.FloatField(blank=True, null=True)
    obligado = models.FloatField(blank=True, null=True)
    pagado = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto_gasto'
        unique_together = (('codigonivel', 'codigoentidad', 'tipoprograma', 'codigoprograma', 'codigosubprograma', 'codigoproyecto', 'codigoobjetogasto', 'codigofuentefinan', 'codigoorgfinanciador', 'codigodpto', 'codigopais', 'borrado', 'anho', 'version'),)


class PresupuestogastoPresi(models.Model):
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    tipo = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    proyecto = models.IntegerField()
    objeto = models.IntegerField()
    pais = models.IntegerField()
    departamento = models.IntegerField()
    fuente = models.IntegerField()
    organismo = models.IntegerField()
    verjustifica = models.TextField(blank=True, null=True)
    verprogramado = models.FloatField()
    fila = models.IntegerField()
    anho = models.IntegerField()
    version = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuestogasto_presi'


class PresupuestoingresoPresi(models.Model):
    numerofila = models.IntegerField(blank=True, null=True)
    anio = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    codorigen = models.IntegerField(blank=True, null=True)
    coddetalle = models.IntegerField(blank=True, null=True)
    fuentefinanc = models.IntegerField(blank=True, null=True)
    montoprogramado = models.FloatField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuestoingreso_presi'


class Producto(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    clase = models.CharField(max_length=1, blank=True, null=True)
    unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('id', 'unidad_medida'),)


class ProductoFinanciero(models.Model):
    nro_fila = models.IntegerField(blank=True, null=True)
    codigonivel = models.IntegerField(blank=True, null=True)
    codigoentidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    codigoprograma = models.IntegerField(blank=True, null=True)
    codigosubprograma = models.IntegerField(blank=True, null=True)
    codigoproyecto = models.IntegerField(blank=True, null=True)
    codigoproducto = models.IntegerField(blank=True, null=True)
    descripcionproducto = models.TextField(blank=True, null=True)
    codigoobjetogasto = models.IntegerField(blank=True, null=True)
    codigofuentefinan = models.IntegerField(blank=True, null=True)
    codigoorgfinanciador = models.IntegerField(blank=True, null=True)
    codigodpto = models.IntegerField(blank=True, null=True)
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
    fechacreacion = models.DateTimeField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_financiero'


class ProductoFisico(models.Model):
    codigonivel = models.IntegerField(blank=True, null=True)
    codigoentidad = models.IntegerField(blank=True, null=True)
    tipoprograma = models.IntegerField(blank=True, null=True)
    codigoprograma = models.IntegerField(blank=True, null=True)
    codigosubprograma = models.IntegerField(blank=True, null=True)
    codigoproyecto = models.IntegerField(blank=True, null=True)
    codigoproducto = models.IntegerField(blank=True, null=True)
    descripcionproducto = models.TextField(blank=True, null=True)
    unidadmedida = models.TextField(blank=True, null=True)
    clase = models.TextField(blank=True, null=True)
    meta1 = models.FloatField(blank=True, null=True)
    avance1 = models.FloatField(blank=True, null=True)
    meta2 = models.FloatField(blank=True, null=True)
    avance2 = models.FloatField(blank=True, null=True)
    meta3 = models.FloatField(blank=True, null=True)
    avance3 = models.FloatField(blank=True, null=True)
    meta4 = models.FloatField(blank=True, null=True)
    avance4 = models.FloatField(blank=True, null=True)
    meta5 = models.FloatField(blank=True, null=True)
    avance5 = models.FloatField(blank=True, null=True)
    meta6 = models.FloatField(blank=True, null=True)
    avance6 = models.FloatField(blank=True, null=True)
    meta7 = models.FloatField(blank=True, null=True)
    avance7 = models.FloatField(blank=True, null=True)
    meta8 = models.FloatField(blank=True, null=True)
    avance8 = models.FloatField(blank=True, null=True)
    meta9 = models.FloatField(blank=True, null=True)
    avance9 = models.FloatField(blank=True, null=True)
    meta10 = models.FloatField(blank=True, null=True)
    avance10 = models.FloatField(blank=True, null=True)
    meta11 = models.FloatField(blank=True, null=True)
    avance11 = models.FloatField(blank=True, null=True)
    meta12 = models.FloatField(blank=True, null=True)
    avance12 = models.FloatField(blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_fisico'


class ProductoPresupuestoDestinatario(models.Model):
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    catalogo_destinatario = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_destinatario'
        unique_together = (('nivel', 'entidad', 'tipo_presupuesto', 'programa', 'subprograma', 'proyecto', 'producto', 'catalogo_destinatario', 'departamento'),)


class ProductoPresupuestoDestinatarioShadow(models.Model):
    id = models.AutoField(primary_key=True)
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    subprograma = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    producto = models.IntegerField(blank=True, null=True)
    catalogo_destinatario = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_destinatario_shadow'


class ProductoPresupuestoFinanciero(models.Model):
    id = models.FloatField(primary_key=True)
    nivel = models.IntegerField()
    entidad = models.IntegerField()
    tipo = models.IntegerField()
    programa = models.IntegerField()
    subprograma = models.IntegerField()
    proyecto = models.IntegerField()
    grupo_objeto_gasto_id = models.IntegerField()
    subgrupo_objeto_gasto_id = models.IntegerField()
    objeto_gasto_id = models.IntegerField()
    fuente_id = models.IntegerField()
    funcional_id = models.IntegerField()
    funcional_nombre = models.TextField()
    departamento_id = models.IntegerField()
    producto_id = models.IntegerField()
    producto_nombre = models.TextField()
    unidad_medida_id = models.IntegerField()
    nombre_unidad_medida = models.TextField()
    mes = models.IntegerField()
    snip = models.IntegerField(blank=True, null=True)
    meta = models.FloatField()
    asignacion = models.FloatField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_financiero'


class ProductoPresupuestoMeta(models.Model):
    mes = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    catalogo_destinatario_id = models.IntegerField()
    departamento_id = models.IntegerField()
    producto_presupusto_id = models.IntegerField()
    producto_id = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    proyecto_id = models.IntegerField()
    subprograma_id = models.IntegerField()
    programa_id = models.IntegerField()
    tipo_presupuesto_id = models.IntegerField()
    entidad_id = models.IntegerField()
    nivel_id = models.IntegerField()
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_meta'
        unique_together = (('id', 'catalogo_destinatario_id', 'departamento_id', 'producto_presupusto_id', 'producto_id', 'unidad_medida_id', 'proyecto_id', 'subprograma_id', 'programa_id', 'tipo_presupuesto_id', 'entidad_id', 'nivel_id'),)


class ProductoPresupuestoMetaN(models.Model):
    id = models.AutoField(primary_key=True)
    mes = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    catalogo_destinatario_id = models.IntegerField()
    departamento_id = models.IntegerField()
    producto_presupusto_id = models.IntegerField()
    producto_id = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    proyecto_id = models.IntegerField()
    subprograma_id = models.IntegerField()
    programa_id = models.IntegerField()
    tipo_presupuesto_id = models.IntegerField()
    entidad_id = models.IntegerField()
    nivel_id = models.IntegerField()
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_meta_n'


class ProductoPresupuestoMetaShadow(models.Model):
    id = models.AutoField(primary_key=True)
    mes = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    catalogo_destinatario_id = models.IntegerField()
    departamento_id = models.IntegerField()
    producto_presupusto_id = models.IntegerField()
    producto_id = models.IntegerField()
    unidad_medida_id = models.IntegerField()
    proyecto_id = models.IntegerField()
    subprograma_id = models.IntegerField()
    programa_id = models.IntegerField()
    tipo_presupuesto_id = models.IntegerField()
    entidad_id = models.IntegerField()
    nivel_id = models.IntegerField()
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_presupuesto_meta_shadow'


class ProductoPresupusto(models.Model):
    id = models.AutoField(primary_key=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    producto_id = models.IntegerField()
    producto_unidad_medida_id = models.IntegerField()
    proyecto_id = models.IntegerField()
    proyecto_subprograma_id = models.IntegerField()
    proyecto_subprograma_programa_id = models.IntegerField()
    proyecto_subprograma_programa_tipo_presupuesto_id = models.IntegerField()
    proyecto_subprograma_programa_entidad_id = models.IntegerField()
    proyecto_subprograma_programa_entidad_nivel_id = models.IntegerField()
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    intermedio = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'producto_presupusto'


class ProductoPresupustoHasEtiquetas(models.Model):
    id = models.AutoField(primary_key=True)
    producto_concat = models.TextField(blank=True, null=True)
    etiquetas_id = models.IntegerField()
    producto_id = models.IntegerField(primary_key=True)
    proyecto_id = models.IntegerField()
    subprograma_id = models.IntegerField()
    programa_id = models.IntegerField()
    tipo_presupuesto_id = models.IntegerField()
    entidad_id = models.IntegerField()
    nivel_id = models.IntegerField()
    version = models.IntegerField()
    anho = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto_presupusto_has_etiquetas'
        unique_together = (('producto_id', 'proyecto_id', 'subprograma_id', 'programa_id', 'tipo_presupuesto_id', 'entidad_id', 'nivel_id', 'anho', 'version', 'etiquetas_id'),)


class Programa(models.Model):
    id = models.IntegerField(primary_key=True)
    numerofila = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    cod_programa = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    abrev = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    base_legal = models.TextField(blank=True, null=True)
    resultado = models.TextField(blank=True, null=True)
    codigodepartamento = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.ForeignKey('TipoPresupuesto', models.DO_NOTHING)
    entidad_id = models.IntegerField()
    entidad_nivel_id = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa'
        unique_together = (('id', 'tipo_presupuesto', 'entidad_id', 'entidad_nivel_id'),)


class Programatico(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_programatico = models.ForeignKey('TipoProgramatico', models.DO_NOTHING)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programatico'
        unique_together = (('id', 'tipo_programatico'),)


class ProgramaticoHasObjetivo(models.Model):
    programatico = models.ForeignKey(Programatico, models.DO_NOTHING, primary_key=True)
    programatico_tipo_programatico_id = models.IntegerField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programatico_has_objetivo'
        unique_together = (('programatico', 'programatico_tipo_programatico_id'),)


class Proyecto(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    subprograma_id = models.IntegerField()
    subprograma_programa_id = models.IntegerField()
    subprograma_programa_tipo_presupuesto_id = models.IntegerField()
    subprograma_programa_entidad_id = models.IntegerField()
    subprograma_programa_entidad_nivel_id = models.IntegerField()
    unidad_responsable_id = models.IntegerField()
    funcional_id = models.IntegerField()
    diagnostico = models.TextField(blank=True, null=True)
    resultado_esperado = models.TextField(blank=True, null=True)
    codigo_departamento = models.IntegerField(blank=True, null=True)
    codigo_snip = models.IntegerField(blank=True, null=True)
    objetivo_estrategico_id = models.IntegerField(blank=True, null=True)
    objetivo_estrategico_id_old = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto'
        unique_together = (('id', 'subprograma_id', 'subprograma_programa_id', 'subprograma_programa_tipo_presupuesto_id', 'subprograma_programa_entidad_id', 'subprograma_programa_entidad_nivel_id', 'unidad_responsable_id', 'funcional_id'),)


class ProyectoHasObjetivo(models.Model):
    nivel = models.IntegerField(blank=True, null=True)
    entidad = models.IntegerField(blank=True, null=True)
    tipo_presupuesto = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    sub_programa = models.IntegerField(blank=True, null=True)
    funcional = models.IntegerField(blank=True, null=True)
    proyecto = models.IntegerField(blank=True, null=True)
    objetivo = models.IntegerField(blank=True, null=True)
    valoracion = models.IntegerField(blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_has_objetivo'


class ProyectoSnip(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.IntegerField()
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_snip'


class ProyectoSnipAutorizado(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    anho = models.IntegerField()
    monto = models.IntegerField()
    entidad = models.ForeignKey(Entidad, models.DO_NOTHING)
    entidad_nivel_id = models.IntegerField()
    proyecto_snip = models.ForeignKey(ProyectoSnip, models.DO_NOTHING)
    organismo_financiador = models.ForeignKey(OrganismoFinanciador, models.DO_NOTHING)
    fuente_financiamiento = models.ForeignKey(FuenteFinanciamiento, models.DO_NOTHING)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_snip_autorizado'
        unique_together = (('id', 'entidad', 'entidad_nivel_id', 'proyecto_snip', 'organismo_financiador', 'fuente_financiamiento'), ('entidad_nivel_id', 'entidad', 'proyecto_snip'),)


class Role(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    urlimagen = models.TextField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class Subprograma(models.Model):
    id = models.IntegerField(primary_key=True)
    programa = models.ForeignKey(Programa, models.DO_NOTHING)
    programa_tipo_presupuesto_id = models.IntegerField()
    programa_entidad_id = models.IntegerField()
    programa_entidad_nivel_id = models.IntegerField()
    anho = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    objetivo = models.TextField(blank=True, null=True)
    codigo_departamento = models.IntegerField(blank=True, null=True)
    baselegal = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subprograma'
        unique_together = (('id', 'programa', 'programa_tipo_presupuesto_id', 'programa_entidad_id', 'programa_entidad_nivel_id'),)


class TipoCatalogoDestinatario(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_catalogo_destinatario'


class TipoDemografica(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_demografica'


class TipoDocumentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documentos'


class TipoIndicador(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_indicador'


class TipoObjetivo(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_objetivo'


class TipoPresupuesto(models.Model):
    nombre = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    descipcion = models.CharField(max_length=45, blank=True, null=True)
    anho = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_presupuesto'


class TipoProgramatico(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_programatico'


class TipoZonaGeografica(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descipcion = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_zona_geografica'


class UnidadJerarquica(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descipcion = models.TextField(blank=True, null=True)
    entidad = models.ForeignKey(Entidad, models.DO_NOTHING)
    entidad_nivel_id = models.IntegerField()
    anho = models.IntegerField(blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_jerarquica'
        unique_together = (('id', 'entidad', 'entidad_nivel_id'),)


class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=60)
    abrev = models.CharField(max_length=20, blank=True, null=True)
    simbolo = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.NullBooleanField()
    anho = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class UnidadResponsable(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.CharField(max_length=45, blank=True, null=True)
    numero_fila = models.IntegerField(blank=True, null=True)
    entidad_id = models.IntegerField()
    entidad_nivel_id = models.IntegerField()
    unidad_jerarquica_id = models.IntegerField()
    anho = models.IntegerField(blank=True, null=True)
    borrado = models.NullBooleanField()
    version = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_responsable'
        unique_together = (('id', 'entidad_id', 'entidad_nivel_id', 'unidad_jerarquica_id'),)


class Usuario(models.Model):
    correo = models.TextField(unique=True, blank=True, null=True)
    passwd = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    entidad = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    entidad_id = models.IntegerField(blank=True, null=True)
    nivel_id = models.IntegerField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    urlimagen = models.TextField(blank=True, null=True)
    unr_id = models.IntegerField()
    borrado = models.NullBooleanField()
    url = models.TextField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)
    role_id_movil = models.IntegerField()
    role_id_tablero = models.IntegerField()
    role_identificaciones = models.IntegerField()
    email_real = models.NullBooleanField()
    ultima_etiqueta_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('id', 'role'),)


class Version(models.Model):
    nro = models.BigIntegerField(primary_key=True)
    anho = models.BigIntegerField()
    descripcion = models.TextField()
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'
        unique_together = (('nro', 'anho'),)


class VersionDb(models.Model):
    id_anterior = models.IntegerField(blank=True, null=True)
    usuario_git = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_insercion = models.TimeField(blank=True, null=True)
    fecha_actualizacion = models.TimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_db'


class ZonaGeografica(models.Model):
    nombre = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    abrev = models.TextField(blank=True, null=True)
    tipo_zona_geografica = models.ForeignKey(TipoZonaGeografica, models.DO_NOTHING)
    cod_geo_unif = models.TextField(blank=True, null=True)
    borrado = models.NullBooleanField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_insercion = models.DateTimeField(blank=True, null=True)
    usuario_responsable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona_geografica'
        unique_together = (('id', 'tipo_zona_geografica'),)
