# Fabrica_2024.1
Workshop Fábrica 2024.1

# API Rick and Morty 📚
Está é a API do uiverso de Rick and Morty, que vai fornecer, nome, especie, genero e origem dos personagens

# Como instalar-📝
Você precisara clonar este repositório: git clone (https://github.com/jg0briel/Fabrica_2024.1)
- Em seguida instale a venv no terminal:
``` python -m venv venv```
- Ative a venv
``` .\venv\Scripts\activate ```
- Instale o requirements
``` pip install -r requirements.txt ```
- Ative a venv
``` python manage.py makemigrations ```
``` python manage.py migrate ```

# Pré-Requisito 🗃️
Dependências que estão no requirements.txt para funcionamento correto da API
- Python
- Django 5.0.3
- Django rest framework
- Requests
- Outras dependências presentes no requirements

# Como usar 💻
- Inicio o servidor da API: ``` python manage.py runserver ```
- Acessar a API http://127.0.0.1:8000/
- Para a acessar a api de fato o link deve estar assim http://127.0.0.1:8000/api/
- E para acessar a parte que o usuário vai colocara informação é esta link: http://127.0.0.1:8000/api/RickMorty/
