from rest_framework import serializers, pagination
#
from .models import FichaTecnica, Procedimientos, Documento
#
from applications.users.models import User

class FichaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaTecnica
        fields = ('__all__')

class ProcedimientoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Procedimientos
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'tipo_usuario'
        )

class DocumentosSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = Documento
        fields = (
            'documento',
            'valor',
            'imagen',
            'prod_created',
        )

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50    

###
class ProcesarDocumentos(serializers.Serializer):
    documento = serializers.IntegerField()
    valor = serializers.CharField()
    imagen = serializers.ImageField()


class pkSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

class ProcesarProcedimientos(serializers.Serializer):
    proceder = pkSerializer(many=True)
    tipo_procedimiento = serializers.CharField()
    descripcion_procedimiento = serializers.CharField()

class ProcesarFichaTecnica(serializers.Serializer):
    enfermedad = serializers.CharField()
    alergia = serializers.CharField()
    enfermedades = serializers.CharField()
    alergias = serializers.CharField()
###
    

