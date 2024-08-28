from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ArquivosSchemaBase(BaseModel):
    nome: str

class ArquivoCreate(ArquivosSchemaBase):
    pass

class ArquivoUpdate(ArquivosSchemaBase):
    pass

class ArquivoResponse(ArquivosSchemaBase):
    id: int
    nome_arquivo: str