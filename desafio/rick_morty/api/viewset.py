from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import RickMortyModel
from .serializer import RickMortySerializer
import requests


class RickMortyViewSet(ModelViewSet):
    queryset = RickMortyModel.objects.all()
    serializer_class = RickMortySerializer

    def create(self, request):
        nome = request.data.get("nome", "")

        site = f"https://rickandmortyapi.com/api/character/?name={nome}&status=alive"
        requisicao = requests.get(site)
        json = requisicao.json()


        nome = json.get("name", "")
        especie = json.get("species", "")
        genero = json.get("gender", "")
        origem = [character["origin"]["name"] for character in json.get("results", [])]

        dados_recebidos ={
            "nome":f"{nome}",
            "especie":f"{especie}",
            "genero":f"{genero}",
            "origem":",".join(origem)
        }

        meuserializer = RickMortySerializer(data=dados_recebidos)

        if meuserializer.is_valid():
            personagem_pesquisado = RickMortyModel.objects.filter(nome=nome)

            personagem_pesquisado_existe = personagem_pesquisado.exists()

            if personagem_pesquisado_existe:
                return Response({"aviso":"esse personagem já está no banco de dados"})
            
            meuserializer.save()
            return Response(meuserializer.data)
        else:
            return Response({"aviso":"Ocorreu um erro!"})
        
    def delete(self, pk=None):
        try:
            personagem = RickMortyModel.objects.get(id=pk)
            personagem.delete()
            return Response({"aviso": "O personagem foi excluído com sucesso"})
        
        except RickMortyModel.DoesNotExist:
            return Response({"aviso": "Esse personagem não existe"})