<div align="center">
  <img height="150" src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif"  />
</div>

###

<h1 align="center">DevLab Projects - Sistema de Gestão</h1>

###

<h3 align="left">👩‍💻  Sistema de backend para gestão de projetos acadêmicos do DevLab!</h3>

###

<h5 align="left">Como Rodar (Instruções de Instalação)<br>1. Clone o repositório.<br>2. Crie um ambiente virtual: `python -m venv venv`<br>3. Ative o ambiente e instale as dependências: `pip install -r requirements.txt`<br>4. Configure o banco: `python manage.py migrate`<br>5. Crie um admin: `python manage.py createsuperuser`<br>6. Rode o servidor: `python manage.py runserver`<br><br>Documentação da API (Endpoints)<br><br>Autenticação<br>* O sistema utiliza Basic Auth ou Session Auth do Django Rest Framework.<br><br>Projetos<br>* `GET /api/projetos/` - Lista todos os projetos.<br>* `POST /api/projetos/` - Cria novo projeto.<br>* `GET /api/projetos/{id}/` - Detalhes do projeto.<br>* `POST /api/projetos/{id}/participantes/` - Adiciona usuário ao projeto. Body: `{"user_id": 1}`.<br><br>
### Equipes<br>* `GET /api/equipes/` - Lista equipes.<br>* `POST /api/equipes/` - Cria equipe.<br>* `PUT /api/equipes/{id}/definir-lider/` - Define líder. Body: `{"user_id": 1}`.<br><br>Usuários<br>* `GET /api/usuarios/` - Lista usuários.<br>* `GET /api/usuarios/{id}/visao-geral/` - **Rota de Composição**: Retorna dados do usuário, seus projetos e suas equipes em um único JSON.<br><br>Modelo de Dados (Explicação)<br>* **Usuário (N:N) Projeto**: Um usuário participa de vários projetos através da tabela de junção implícita.<br>* **Projeto (1:N) Equipe**: Um projeto tem várias equipes.<br>* **Usuário (1:1) Equipe (Líder)**: Um usuário pode liderar apenas uma equipe.</h5>

###

<h3 align="left">👩‍💻  Realização</h3>

###

<h5 align="left">Nosso projeto foi realizado como atividade final do curso de Desenvolvimento Back-end em Python e Django, ofertado pela Bolsa Futuro Digital, no Instituto Federal de Brasília - Campus Gama.<br><br>Letícia Castro de Souza</h5>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="django logo"  />
</div>

###
