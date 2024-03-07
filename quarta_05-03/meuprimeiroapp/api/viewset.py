from rest_framework.viewsets import ModelViewSet
from .serializer import PessoaSerializer
from ..models import PessoaBancoDeDados

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDeDados.objects.all()