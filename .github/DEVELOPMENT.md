# 🛠️ Guia de Desenvolvimento

Este documento descreve como configurar o ambiente de desenvolvimento e rodar o projeto localmente.

## 📋 Pré-requisitos

- **Python 3.12+**
- **uv** (gerenciador de pacotes ultrarrápido)
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
  - Linux/Mac: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Git**
- **Docker** (para V1.5+)

## 🚀 Setup Inicial (V1)

### 1. Clonar o repositório

```bash
git clone https://github.com/reali-705/grafos.git
cd grafos
```

### 2. Criar ambiente virtual com uv

```bash
uv venv
```

Ativar:

- **Windows:** `.venv\Scripts\activate.ps1`
- **Linux/Mac:** `source .venv/bin/activate`

### 3. Instalar dependências

```bash
# Instalação básica
uv install -e .

# Instalação com dependências de desenvolvimento
uv install -e .[dev]
```

### 4. Rodar a API

Deve entrar em `api/`

```bash
cd api
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`

Documentação Swagger: `http://localhost:8000/docs`

<!-- TODO: Adicionar configuração do pytest e tags -->
## 🧪 Testes

### Rodar todos os testes

```bash
pytest tests/ -v
```

### Rodar testes com cobertura

```bash
pytest tests/ --cov=app --cov-report=html
```

Abra `htmlcov/index.html` para visualizar cobertura.

### Rodar um teste específico

```bash
pytest tests/test_models.py::test_vertex_creation -v
```

## 📊 Estrutura de Banco de Dados (V1)

SQLite é armazenado em `api/app.db` (ignorado no git).

**Tabelas:**

- `vertex`: id, label, weight
- `edge`: id, source_id, target_id, weight, is_directed

Para inspecionar:

```bash
sqlite3 app.db
sqlite> .tables
sqlite> SELECT * FROM vertex;
```

<!-- TODO: Adicionar configuração do Docker-Compose -->
## 🐳 Docker (V1.5+)

### Build

```bash
docker build -t grafos-api:latest .
```

### Rodar

```bash
docker run -p 8000:8000 grafos-api:latest
```

### Docker Compose

```bash
docker-compose up
```

## 🔗 Endpoints Principais (V1)

### Vértices

- `POST /vertices` - Criar vértice
- `GET /vertices` - Listar vértices
- `GET /vertices/{id}` - Obter vértice
- `DELETE /vertices/{id}` - Deletar vértice

### Arestas

- `POST /edges` - Criar aresta
- `GET /edges` - Listar arestas
- `DELETE /edges/{id}` - Deletar aresta

### Operações

- `POST /graphs/union` - União de grafos
- `POST /graphs/intersection` - Interseção de grafos
- `GET /graphs/{id}/density` - Calcular densidade
- `GET /graphs/{id}/adjacency-matrix` - Matriz de adjacência
- `GET /graphs/{id}/adjacency-list` - Lista de adjacência
- `POST /graphs/{id}/connectivity` - Verificar conexidade

## 🐛 Debugging

### Log detalhado

```bash
PYTHONUNBUFFERED=1 uvicorn app.main:app --reload --log-level debug
```

### Usar debugger do VS Code

Crie `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": ["app.main:app", "--reload"],
            "cwd": "${workspaceFolder}/api",
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

## 📚 Dependências Principais (V1)

| Pacote | Versão | Propósito |
| --- | --- | --- |
| FastAPI | ^0.104 | Framework Web |
| Uvicorn | ^0.24 | ASGI Server |
| SQLModel | ^0.0.14 | ORM + Schema |
| NetworkX | ^3.2 | Validação de Grafos |
| PyVis | ^0.3.2 | Visualização |
| Pytest | ^7.4 | Testes |

## 🚨 Problemas Comuns

### "ModuleNotFoundError: No module named 'app'"

Certifique-se de que você rodou o comando de dentro de `api/`:

```bash
cd api
uvicorn app.main:app --reload
```

### "sqlite3.OperationalError: no such table: vertex"

O banco não foi inicializado. FastAPI deve criar automaticamente na primeira requisição, mas se falhar:

```bash
python -c "from app.database.db import create_db_and_tables; create_db_and_tables()"
```

### Porta 8000 já em uso

Rode em outra porta:

```bash
uvicorn app.main:app --port 8001 --reload
```

## 📖 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [NetworkX Documentation](https://networkx.org/)
- [uv Documentation](https://docs.astral.sh/uv/)
