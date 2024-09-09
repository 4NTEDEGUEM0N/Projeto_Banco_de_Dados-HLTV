import uvicorn
from fastapi import FastAPI
from routers import (jogador_router, time_router, arquivos_router, escalacao_router, jogador_x_escalacao_router,
                     evento_router, trofeu_router, jogador_x_trofeu_router, time_x_evento_router, partida_router,
                     time_x_partida_router, mapa_router, mapa_x_partida_router, ranking_router, time_x_ranking_router,
                     noticia_router, view_router)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(arquivos_router.router)
app.include_router(jogador_router.router)
app.include_router(time_router.router)
app.include_router(escalacao_router.router)
app.include_router(jogador_x_escalacao_router.router)
app.include_router(evento_router.router)
app.include_router(trofeu_router.router)
app.include_router(jogador_x_trofeu_router.router)
app.include_router(time_x_evento_router.router)
app.include_router(partida_router.router)
app.include_router(time_x_partida_router.router)
app.include_router(mapa_router.router)
app.include_router(mapa_x_partida_router.router)
app.include_router(ranking_router.router)
app.include_router(time_x_ranking_router.router)
app.include_router(noticia_router.router)
app.include_router(view_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)