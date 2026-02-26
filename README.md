# Banco_de_Dados-HLTV

## Sobre a HLTV
A HLTV é um site dedicado à cobertura do Counter-Strike competitivo. Ele apresenta notícias, calendários, resultados, placares ao vivo, estatísticas, fotografias e um fórum dedicado à comunidade. O site também é conhecido por seu Rating, prêmios de MVP, ranking mundial de equipes, o ranking anual dos Top 20 jogadores e pelo seu Award Show.

## Descrição do Projeto
Este projeto consiste em uma API desenvolvida em Python (utilizando o framework FastAPI e bibliotecas como SQLAlchemy e Pydantic) para simular o banco de dados da plataforma HLTV. O sistema gerencia as principais entidades do cenário competitivo de Counter-Strike, tais como: jogadores, times, escalações, partidas, mapas, eventos, troféus e notícias, contemplando também a execução de *views* e *procedures* (relatórios e estatísticas do banco de dados). O controle estrutural do banco de dados é feito com o Alembic, suportando bancos relacionais como PostgreSQL e SQLite.

## Requirements
* Python 3.12.3
* pip install -r requirements.txt

## Run
* Rodar a main

## Alembic
* ### Gerar arquivos de configuração
  * alembic init alembic
* ### Gerar o SQL automáticamente e atualizar o banco de dados
  * Atualizar o arquivo alembic/env.py com os novos modelos
  * alembic revision --autogenerate -m "Descrição da migração"
  * alembic upgrade head

## PostgresSQL
* ### Criar um container no docker
  * docker run --name db_hltv -p 5432:5432 -e POSTGRES_DB=db_hltv -e POSTGRES_PASSWORD=123 -d postgres
* ### Alterar o DATABASE_URL no arquivo .env
  * DATABASE_URL = postgresql://postgres:123@localhost/db_hltv

## SQLite
* ### Alterar o DATABASE_URL no arquivo .env
  * DATABASE_URL = sqlite:///./db_HLTV.db
