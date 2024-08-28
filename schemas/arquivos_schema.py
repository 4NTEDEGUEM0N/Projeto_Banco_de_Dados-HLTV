from pydantic import BaseModel, ConfigDict


class ArquivoSchemaBase(BaseModel):
    nome: str

class ArquivoCreate(ArquivoSchemaBase):
    pass

class ArquivoUpdate(ArquivoSchemaBase):
    pass

class ArquivoResponse(ArquivoSchemaBase):
    id: int
    nome_foto: str

    model_config = ConfigDict(from_attributes=True)