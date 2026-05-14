# 📋 Copilot Instructions: Projeto API de Grafos

Utilize o idioma português para todas as interações. Siga as diretrizes abaixo para garantir que o desenvolvimento da API de Grafos seja consistente, escalável e alinhado com os objetivos do projeto.

## 🎯 Objetivo Principal

Construir uma **API escalável de Gerenciamento de Grafos**, evoluindo de um protótipo acadêmico (V1) para uma solução de produção (V3+). O projeto começa com validação de conceitos para a prova de amanhã, e escala gradualmente integrando Rust, PostgreSQL e React.

---

## 🗺️ Roadmap Evolutivo

### **V1: Núcleo Acadêmico (Hoje - Semana 01)**

**Foco:** Validação lógica e preparação para a prova.

**Tech Stack:**

- Python 3.12+ (gerenciado via `uv`)
- FastAPI (framework web)
- SQLModel (ORM + schema validation)
- SQLite (persistência simples)
- NetworkX (validação e operações complexas)
- PyVis (visualização em HTML)

**Funcionalidades Mínimas:**

- **Representação Computacional**
  - Geração de Matriz de Adjacência ($V \times V$)
  - Geração de Lista de Adjacência ($V+E$)

- **Operações Binárias**
  - Endpoints para União ($G_1 \cup G_2$)
  - Endpoints para Interseção ($G_1 \cap G_2$)
  - Algoritmo de Soma (Join) conectando todos os vértices

- **Propriedades e Métricas**
  - Cálculo de Densidade: $D = \frac{2|E|}{|V|(|V|-1)}$
  - Identificação de Grau $d(v)$
  - Verificação de Conexidade (Forte vs. Fraca)

- **Operação Unitária**
  - Contração de Vértices

**Estrutura de Pastas Recomendada:**

```bash
api/
├── graph_api/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── graph_operations.py      # Lógica de grafos
│   │   ├── implementations/
│   │   │   ├── adjacency_matrix.py
│   │   │   ├── adjacency_list.py
│   │   │   └── connectivity.py
│   │   └── validators.py             # Validações matemáticas
│   ├── models/
│   │   ├── __init__.py
│   │   ├── vertex.py
│   │   ├── edge.py
│   │   └── graph.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── vertices.py
│   │   ├── edges.py
│   │   ├── graphs.py
│   │   └── operations.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py                    # Configuração SQLite
│   └── main.py                      # Entrada da aplicação
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_operations.py
│   └── test_api.py
├── pyproject.toml                   # Dependências (uv)
└── Dockerfile
```

**Requisitos Técnicos da V1:**

- Tabelas separadas para `Vertex` e `Edge`
- Endpoint POST para criar vértices e arestas
- Endpoint GET que retorna Matriz de Adjacência
- Endpoint GET que retorna Lista de Adjacência
- Validação: grafo não pode ter self-loops (configurable)
- Uso de SQLModel para evitar duplicação banco ↔ schema

---

### **V1.5: Portabilidade e Automação (Semana 02)**

**Foco:** Infraestrutura leve e CI/CD automatizado.

**Novas Techs:**

- Docker (Multi-stage builds)
- Docker Compose
- GitHub Actions

**Implementação:**

- Dockerfile com 2 estágios (builder + runtime)
- docker-compose.yml para dev local
- CI pipeline: testes a cada push
- Cobertura de testes para Union/Intersection

---

### **V2: O Pivot de Performance (Semana 04)**

**Foco:** Eficiência bruta e integração híbrida.

**Novas Techs:**

- Rust (núcleo de processamento)
- PyO3 + Maturin (compilação como módulo Python)

**Diferencial:**

- Migrar Matriz de Adjacência para Rust
- Implementar Matriz Triangular (economiza 50% RAM em grafos não-direcionados)
- Benchmark: Python vs. Rust para Caminho Crítico em DAG

---

### **V3: Persistência e Visibilidade (Semana 06+)**

**Foco:** Robustez, análise avançada e interface gráfica.

**Novas Techs:**

- PostgreSQL (backend de produção)
- Apache AGE (extensão graph queries)
- React (front-end)
- Prometheus/Grafana (observability)

**Implementação:**

- Migrar SQLite → PostgreSQL
- Dashboard React visualizando "saúde" das conexões
- Queries híbridas (SQL + Cypher via AGE)
- Métricas: Latency, Cache Hit Ratio

---

## 🛠️ Diretrizes para o Copilot

### Ao começar um novo tópico:

1. Confirme em qual **Versão** você está trabalhando
2. Respeite o escopo dessa versão (não misture V2/V3 com V1)
3. Se aparecer necessidade de escalar, documente como "Future Work" ou "V2+"

### Ao implementar funcionalidades V1:

1. Use `SQLModel` para modelos (evita duplicação)
2. Implemente operações de grafo em `app/core/implementations/`
3. Cada rota em `app/routes/` deve ser testável isoladamente
4. Documente fórmulas matemáticas em docstrings (ex: fórmula de densidade)

### Sobre estrutura de dados:

- Matriz de Adjacência: usada para análise densa, consultas de conectividade
- Lista de Adjacência: usada para grafos esparsos, iteração eficiente
- Ambas devem ser geradas on-the-fly a partir da tabela `Edge`

### Ao encontrar dúvidas:

- Priorize a prova de amanhã (V1)
- Use NetworkX como "oráculo de verdade" para validar suas implementações
- Documente descobertas e decisões em issues

---

## 📊 Organização no GitHub

**Milestones:**

- V1: Núcleo Acadêmico
- V1.5: Portabilidade
- V2: Performance
- V3: Produção

**Estrutura de Issues:**

- Cada issue = um "epic" funcional
- Task lists (checkboxes) dentro de cada issue para subtarefas
- Link issues usando "Relacionada", "Bloqueia", "Bloqueada por"

---

## 🧪 Exemplo de Prompt para o Copilot

> "Estou na V1. Preciso criar o modelo `Vertex` usando SQLModel.
> Requisitos:
>
> 1. id (UUID, primary key)
> 2. label (str, unique)
> 3. weight (float, opcional, default=0)
> 4. Validação: label não pode estar vazio
>
> Crie também o endpoint POST `/vertices` e GET `/vertices/{id}`.
> Use convenções do projeto (pasta `app/models/`, rota em `app/routes/vertices.py`)."

---

## 📝 Notas Importantes

- **Não misture versões:** Se surgir a ideia de migrar para Rust na V1, documente como V2+ Future Work
- **Banco de dados:** V1 usa SQLite em arquivo `.db` (ignorado no git per `.gitignore`)
- **Python version:** Fixe 3.12+ no `pyproject.toml`
- **Ambiente:** Use `uv` para gerenciar dependências (rápido e moderno)

---

## 🎓 Referências Matemáticas

- **Grafo:** $G = (V, E)$ onde $V$ é conjunto de vértices e $E$ é conjunto de arestas
- **Densidade:** $D = \frac{2|E|}{|V|(|V|-1)}$ (grafos não-direcionados)
- **Grau:** $d(v) = $ número de arestas incidentes a $v$
- **Conexidade Forte:** Existe caminho entre qualquer par de vértices (ambas as direções)
- **Conexidade Fraca:** Existe caminho ignorando direção das arestas
