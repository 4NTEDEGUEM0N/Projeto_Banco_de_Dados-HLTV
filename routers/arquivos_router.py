from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List
import crud.arquivos_crud
from database.database import get_db
from schemas.arquivos_schema import ArquivoResponse
import io
import magic

router = APIRouter(prefix="/arquivos", tags=["Arquivos"])

@router.post("/uploadfile", response_model=ArquivoResponse, status_code=201)
async def create_arquivo(nome: str = Form(...), arquivo: UploadFile = File(...), db: Session = Depends(get_db)):
    dados = await arquivo.read()
    return crud.arquivos_crud.create_arquivo(db=db, dados=dados, nome_foto=arquivo.filename, nome=nome)

@router.get("/{id_foto}/download")
def get_arquivo_download(id_foto: int, db: Session = Depends(get_db)):
    db_arquivo = crud.arquivos_crud.read_arquivo(db=db, id_foto=id_foto)
    if not db_arquivo:
        raise HTTPException(status_code=404, detail="Foto not found")
    return StreamingResponse(io.BytesIO(db_arquivo.dados), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={db_arquivo.nome_arquivo}"})


@router.get("/{id_foto}/visualizar")
def get_arquivo_visualizar(id_foto: int, db: Session = Depends(get_db)):
    db_arquivo = crud.arquivos_crud.read_arquivo(db=db, id_foto=id_foto)
    if not db_arquivo:
        raise HTTPException(status_code=404, detail="Foto not found")

    mime = magic.Magic(mime=True)
    media_type = mime.from_buffer(db_arquivo.dados)
    file_stream = io.BytesIO(db_arquivo.dados)
    return StreamingResponse(file_stream, media_type=media_type)


@router.get("/{id_foto}/info", response_model=ArquivoResponse, status_code=200)
def get_arquivo_info(id_foto: int, db: Session = Depends(get_db)):
    db_arquivo = crud.arquivos_crud.read_arquivo(db=db, id_foto=id_foto)
    if not db_arquivo:
        raise HTTPException(status_code=404, detail="Foto not found")
    return db_arquivo

@router.get("/", response_model=List[ArquivoResponse], status_code=200)
def read_arquivos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.arquivos_crud.read_arquivos(db, skip=skip, limit=limit)


@router.delete("/{id_foto}", status_code=204)
def delete_arquivo(id_foto: int, db: Session = Depends(get_db)):
    db_arquivo = crud.arquivos_crud.read_arquivo(db, id_foto=id_foto)
    if db_arquivo is None:
        raise HTTPException(status_code=404, detail="Foto not found")
    crud.arquivos_crud.delete_arquivo(db, id_foto=id_foto)

