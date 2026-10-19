# DIO Explorer — MCP Server

Servidor [MCP (Model Context Protocol)](https://modelcontextprotocol.io) do projeto **DIO Explorer**.  
Permite que assistentes de IA (Bob, Claude Desktop, etc.) interajam com as trilhas, desafios e certificados da plataforma DIO via protocolo padrão MCP.

---

## Ferramentas disponíveis

| Ferramenta | Descrição |
|---|---|
| `trilha` | Retorna informações completas de uma trilha por tecnologia |
| `desafio` | Gera um desafio de programação aleatório por tecnologia e nível |
| `certificado` | Emite um certificado simulado de conclusão de trilha |

## Resources disponíveis

| URI | Descrição |
|---|---|
| `dio://trilhas/tecnologias` | Lista todas as tecnologias disponíveis |
| `dio://trilhas/catalogo` | Catálogo completo de trilhas em JSON |

---

## Pré-requisitos

- Python 3.10+
- pip

---

## Instalação

```bash
cd Projeto-Final-DIO-/DIO_explorer/mcp
pip install -r requirements.txt
```

---

## Execução

### Modo stdio (Bob / Claude Desktop)

```bash
python server.py
```

### Modo HTTP (acesso via HTTPS / API Key / SSO)

```bash
MCP_TRANSPORT=http MCP_PORT=8080 python server.py
```

Com autenticação por API Key:

```bash
MCP_TRANSPORT=http MCP_PORT=8080 MCP_API_KEY=minha-chave-secreta python server.py
```

> **TLS / HTTPS:** coloque um reverse-proxy (nginx, Caddy) na frente do servidor HTTP para terminar TLS.  
> **SSO:** configure o proxy para validar tokens OAuth/OIDC antes de encaminhar as requisições ao servidor MCP.

---

## Registrar no Bob (stdio)

Adicione ao seu `mcp.json` (workspace ou global):

```json
{
  "mcpServers": {
    "dio-explorer": {
      "command": "python",
      "args": ["/caminho/absoluto/para/DIO_explorer/mcp/server.py"]
    }
  }
}
```

## Registrar no Bob (HTTP remoto)

```json
{
  "mcpServers": {
    "dio-explorer": {
      "url": "http://localhost:8080/mcp",
      "headers": {
        "x-api-key": "${env:DIO_MCP_API_KEY}"
      }
    }
  }
}
```

---

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|---|---|---|
| `MCP_TRANSPORT` | `stdio` | Transporte: `stdio` ou `http` |
| `MCP_PORT` | `8080` | Porta HTTP (apenas quando `MCP_TRANSPORT=http`) |
| `MCP_API_KEY` | _(vazio)_ | Chave de API para autenticar requisições HTTP |

---

## Exemplos de uso (via Bob)

```
/trilha Python
/desafio Java Intermediário
/certificado "Maria Silva" React
```

Ou diretamente em linguagem natural:

> "Quais trilhas de Node.js estão disponíveis na DIO?"  
> "Gere um desafio avançado de Python para mim."  
> "Emita um certificado de conclusão da trilha de Java para João Santos."
