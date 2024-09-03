from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class MapaSchemaBase(BaseModel):
    nome: str

class MapaCreate(MapaSchemaBase):
    pass

class MapaUpdate(MapaSchemaBase):
    pass

class MapaResponse(MapaSchemaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)