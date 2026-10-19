# DIO Explorer — Projeto Final IBM Bob

Servidor MCP que expõe trilhas de aprendizado, desafios de código e certificados da plataforma DIO via protocolo MCP (stdio ou HTTP).

---

## Estrutura do Projeto

```
DIO_explorer/
├── commands/        # Definição dos slash commands
├── data/            # Base de dados JSON com as trilhas
├── docs/            # Resultados dos testes
├── mcp/             # Servidor MCP (server.py, pyproject.toml)
└── src/             # Código-fonte e testes
```

---

## Como executar o projeto

### Pré-requisitos

- Python **3.9+**
- pip

### 1. Instale as dependências

```bash
cd DIO_explorer/mcp
pip install -r requirements.txt
```

### 2. Execute o servidor MCP

**Modo stdio** (padrão — para uso com Bob/Claude Desktop):

```bash
python DIO_explorer/mcp/server.py
```

**Modo HTTP** (acesso remoto via HTTPS/API Key):

```bash
MCP_TRANSPORT=http MCP_PORT=8080 MCP_API_KEY=<sua_chave> python DIO_explorer/mcp/server.py
```

> O servidor ficará disponível em `http://localhost:8080`. Para proteger o acesso, defina a variável `MCP_API_KEY`.

---

## Como usar os comandos

O servidor expõe três ferramentas via MCP. Quando integrado ao Bob, utilize os slash commands diretamente no chat.

### `/trilha <tecnologia>`

Retorna o plano de estudos completo de uma trilha DIO.

```
/trilha Python
/trilha Java
/trilha React
/trilha Machine Learning
/trilha AWS
```

**Resposta inclui:** nome da trilha, nível, número de módulos, XP total, badges disponíveis, lives ao vivo e promoção ativa.

---

### `/desafio <tecnologia> <nivel>`

Gera um desafio de programação aleatório para a tecnologia e nível informados.

```
/desafio Python Básico
/desafio Java Intermediário
/desafio React Avançado
```

| Nível | Tempo estimado | XP |
|---|---|---|
| `Básico` | 15–30 min | 100–300 XP |
| `Intermediário` | 30–60 min | 300–600 XP |
| `Avançado` | 60–120 min | 600–1200 XP |

---

### `/certificado <nome> <tecnologia>`

Emite um certificado simulado de conclusão de trilha.

```
/certificado "Ana Silva" Python
/certificado "Carlos Mendes" Java
/certificado "Maria Oliveira" React
```

**Resposta inclui:** nome do usuário, trilha concluída, nível, módulos, XP, badges, código único no formato `DIO-AAAAMMDD-XXXX` e data de emissão.

---

### Tecnologias disponíveis

Python · Java · React · Machine Learning · Angular · Node.js · AWS · DevOps · Flutter · Kotlin · TypeScript · Docker · Go · Rust · PHP · Swift · C# · Unity · Data Science · Blockchain

---

## Como executar os testes

Os testes estão em `DIO_explorer/src/test_dio_commands.py` e utilizam **pytest**.

### 1. Instale o pytest (caso ainda não tenha)

```bash
pip install pytest
```

### 2. Execute os testes

```bash
cd DIO_explorer/src
pytest test_dio_commands.py -v
```

### 3. Verifique a cobertura (opcional)

```bash
pip install pytest-cov
pytest test_dio_commands.py -v --cov=dio_commands --cov-report=term-missing
```

Os resultados dos testes estão documentados em [`docs/resultado_testes.txt`](DIO_explorer/docs/resultado_testes.txt).

---

## Desenvolvido com

- [IBM Bob](https://www.ibm.com/products/bob) — assistente de desenvolvimento
- [FastMCP](https://github.com/jlowin/fastmcp) — framework MCP para Python
- [DIO](https://www.dio.me/) — plataforma de aprendizado
