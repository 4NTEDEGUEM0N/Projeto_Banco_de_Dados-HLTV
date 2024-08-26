import uvicorn
from fastapi import FastAPI
from routers import jogador_router, time_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(jogador_router.router)
app.include_router(time_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)