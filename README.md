# Projeto_Banco_de_Dados-HLTV

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
* docker run --name db_hltv -p 5432:5432 -e POSTGRES_DB=db_hltv -e POSTGRES_PASSWORD=123 -d postgres