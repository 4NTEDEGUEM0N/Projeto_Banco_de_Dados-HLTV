from pydantic import BaseModel, ConfigDict
from typing import List, Optional


class TimeSchemaBase(BaseModel):
    name: str

class TimeCreate(TimeSchemaBase):
    pass

class TimeUpdate(TimeSchemaBase):
    pass

class TimeResponse(TimeSchemaBase):
    id: int
    jogadores: Optional[List["JogadorResponse"]] = None

    model_config = ConfigDict(from_attributes=True)


from schemas.jogador_schema import JogadorResponse