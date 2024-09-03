from pydantic import BaseModel, ConfigDict


class NoticiaSchemaBase(BaseModel):
    cabecalho: str
    corpo: str
    autor: str
    regiao: str

class NoticiaCreate(NoticiaSchemaBase):
    pass

class NoticiaUpdate(NoticiaSchemaBase):
    pass

class NoticiaResponse(NoticiaSchemaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)