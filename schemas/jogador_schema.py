from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class JogadorSchemaBase(BaseModel):
    name: str
    apelido: str
    nacionalidade: str
    data_nascimento: date
    genero: str
    foto_id : Optional[int] = None

class JogadorCreate(JogadorSchemaBase):
    pass

class JogadorUpdate(JogadorSchemaBase):
    pass

class JogadorResponse(JogadorSchemaBase):
    id: int
    foto: Optional["ArquivoResponse"] = None
    escalacao_jogador: Optional[List["JogadorEscalacaoResponse"]] = None

    model_config = ConfigDict(from_attributes=True)

class JogadorResponseMinimal(BaseModel):
    id: int
    apelido: str

    model_config = ConfigDict(from_attributes=True)

from schemas.jogador_x_escalacao_schema import JogadorEscalacaoResponse
from schemas.arquivos_schema import ArquivoResponse