from rest_framework.serializers import ModelSerializer
from ..models import RickMortyModel

class RickMortySerializer(ModelSerializer):
    class Meta:
        model = RickMortyModel
        fields =["id", "nome", "especie", "genero", "origem"]