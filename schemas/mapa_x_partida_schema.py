from typing import Optional, List

from pydantic import BaseModel, ConfigDict



class MapaPartidaSchemaBase(BaseModel):
    partida_id: int
    mapa_id: int

class MapaPartidaCreate(MapaPartidaSchemaBase):
    pass

class MapaPartidaUpdate(MapaPartidaSchemaBase):
    pass

class MapaPartidaResponse(MapaPartidaSchemaBase):
    partida: Optional["PartidaResponse"]
    mapa: Optional["MapaResponse"]

    model_config = ConfigDict(from_attributes=True)

class MapaPartidaResponseMapa(BaseModel):
    mapa: Optional["MapaResponse"]
    model_config = ConfigDict(from_attributes=True)


from schemas.partida_schema import PartidaResponse
from schemas.mapa_schema import MapaResponse
