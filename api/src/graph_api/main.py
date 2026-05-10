from contextlib import asynccontextmanager

from fastapi import FastAPI

from graph_api.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Eventos de inicialização e finalização do aplicativo.

    Precisa ser async para garantir que o banco de dados seja inicializado antes de processar qualquer solicitação."""
    # Inicializa o banco de dados antes de processar qualquer solicitação
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}
