# Sistema de Chamados — Nexa Solutions

Projeto para a disciplina de Manutenção e Evolução de Software.

## Contexto
A Nexa Solutions possui um sistema interno para abertura e acompanhamento de chamados de suporte. O projeto possui uma API REST desenvolvida em Django e uma interface HTML simples para consulta e cadastro de chamados.

## Tecnologias
- Python
- Django & Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Git

## Estrutura
`backend/`   # API Django
`frontend/`  # Interface HTML simples
`docs/`      # Documentação e demandas

## Configuração Inicial (Variáveis de Ambiente)
Antes de rodar o projeto, é necessário configurar as credenciais de segurança:
1. Faça uma cópia do arquivo `.env.example` localizado na raiz do projeto.
2. Renomeie essa cópia para `.env`.
3. Preencha os valores dentro do `.env` com suas credenciais locais. O arquivo `.env` não deve ser versionado no Git.

## Executando com Docker
O sistema foi conteinerizado para garantir um ambiente reproduzível. Para iniciar a API e o banco de dados, execute o comando abaixo na raiz do projeto:

> docker compose up --build

A API estará disponível em: `http://localhost:8000/api/chamados/`

## Executando os Testes Automatizados
Para garantir a qualidade do sistema, você pode executar a suíte de testes. Com o Docker rodando, abra um novo terminal e digite:

> docker compose exec api python manage.py test

## Principais Endpoints da API
* **`GET /api/chamados/`**: Lista os chamados cadastrados. Pode ser filtrado por status (ex: `?status=ABERTO`).
* **`POST /api/chamados/`**: Cria um novo chamado. O campo `titulo` é obrigatório.
* **`GET /api/indicadores/`**: Retorna um resumo com o volume total de chamados, segmentados pelo status atual.g