from rest_framework import serializers
#
from .models import Empresa
#

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ConfigurarSerializer(serializers.Serializer):

    nombre = serializers.CharField()
    rut = serializers.CharField()
    pais = serializers.CharField()
    codigo_area = serializers.CharField()
    contacto = serializers.IntegerField()
    año_fundacion = serializers.DateField()
    representante = serializers.CharField()
    region = serializers.CharField()
    comuna = serializers.CharField()
    calle = serializers.CharField()
    numeracion = serializers.CharField()