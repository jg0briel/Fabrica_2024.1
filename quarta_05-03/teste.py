import requests 
nome = requests.get("http://127.0.0.1:8000/api/pessoa/3")

json = nome.json()
print(json.get("primeiro_nome", "Informação não encontrada"))