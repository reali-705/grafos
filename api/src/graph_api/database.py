from collections.abc import Generator
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

# Resolve o caminho para o banco de dados e garante que o diretório exista
API_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_DIR = API_DIR / "data"
DATABASE_DIR.mkdir(exist_ok=True)
DATABASE_PATH = DATABASE_DIR / "graph.db"

# Configura a URL do banco de dados SQLite
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def init_db() -> None:
    """Cria as tabelas no banco de dados."""
    SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    """Retorna uma sessão do banco de dados."""
    with Session(engine) as session:
        yield session
