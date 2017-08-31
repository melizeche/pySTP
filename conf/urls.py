"""pystp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from apps.tablerocp import views as tablero_views
from apps.spr import views as spr_views

router = routers.DefaultRouter()
router.register(r'users', tablero_views.UserViewSet)
router.register(r'groups', tablero_views.GroupViewSet)
router.register(r'usuario', spr_views.UsuarioViewSet)
router.register(r'institucion', spr_views.InstitucionViewSet)
router.register(r'nivel', spr_views.NivelViewSet)
router.register(r'entidad', spr_views.EntidadViewSet)
router.register(r'unidad_jerarquica', spr_views.UnidadJerarquicaViewSet)
router.register(r'avanceindicador', spr_views.AvanceIndicadorViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
admin.site.site_header = 'Administración PySTP'
