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
    escalacao: Optional[List["EscalacaoResponse"]] = None

    model_config = ConfigDict(from_attributes=True)

class TimeResponseMinimal(TimeSchemaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


from schemas.escalacao_schema import EscalacaoResponse