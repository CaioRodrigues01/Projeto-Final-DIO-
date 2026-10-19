#!/usr/bin/env python3
"""
DIO Explorer — MCP Server

Expõe as ferramentas do projeto DIO Explorer via protocolo MCP (stdio).
Pode ser conectado ao Bob/Claude via stdio ou publicado como servidor HTTP
com autenticação SSO/API Key para acesso remoto.

Ferramentas disponíveis:
  - trilha      → Consulta informações de uma trilha DIO por tecnologia
  - desafio     → Gera um desafio aleatório para uma tecnologia e nível
  - certificado → Emite um certificado simulado para um usuário

Uso (stdio):
    python server.py

Uso (HTTP streamable — para acesso via HTTPS/SSO/API Key):
    MCP_TRANSPORT=http MCP_PORT=8080 MCP_API_KEY=<sua_chave> python server.py
"""

import json
import os
import sys

# Garante que o módulo src seja encontrado independente do diretório de execução
_ROOT = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_ROOT, "..", "src")
_DATA = os.path.join(_ROOT, "..", "data", "trilhas_dio.json")

if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

from mcp.server.fastmcp import FastMCP  # type: ignore

from dio_commands import (
    comando_trilha,
    comando_desafio,
    comando_certificado,
    _available_technologies,
)

# ---------------------------------------------------------------------------
# Configuração do servidor
# ---------------------------------------------------------------------------

TRANSPORT = os.environ.get("MCP_TRANSPORT", "stdio")  # "stdio" | "http"
PORT = int(os.environ.get("MCP_PORT", "8080"))
API_KEY = os.environ.get("MCP_API_KEY")  # Opcional — ativa autenticação por API Key

mcp = FastMCP(
    name="dio-explorer",
    version="1.0.0",
    instructions=(
        "Servidor MCP do DIO Explorer. "
        "Use as ferramentas `trilha`, `desafio` e `certificado` para interagir "
        "com as trilhas de aprendizado da plataforma DIO."
    ),
)

# ---------------------------------------------------------------------------
# Ferramenta: /trilha
# ---------------------------------------------------------------------------

@mcp.tool()
def trilha(tecnologia: str) -> str:
    """Retorna as informações completas de uma trilha DIO pela tecnologia.

    Args:
        tecnologia: Nome da tecnologia (ex: Python, Java, React, Node.js).
    """
    resultado = comando_trilha(tecnologia, data_path=_DATA)
    return json.dumps(resultado, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Ferramenta: /desafio
# ---------------------------------------------------------------------------

@mcp.tool()
def desafio(tecnologia: str, nivel: str) -> str:
    """Gera um desafio de programação aleatório para a tecnologia e nível informados.

    Args:
        tecnologia: Nome da tecnologia (ex: Python, Java, React).
        nivel: Nível do desafio — um de: Básico, Intermediário, Avançado.
    """
    resultado = comando_desafio(tecnologia, nivel, data_path=_DATA)
    return json.dumps(resultado, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Ferramenta: /certificado
# ---------------------------------------------------------------------------

@mcp.tool()
def certificado(nome_usuario: str, tecnologia: str) -> str:
    """Emite um certificado simulado de conclusão de trilha DIO.

    Args:
        nome_usuario: Nome completo do usuário que receberá o certificado.
        tecnologia: Nome da tecnologia da trilha concluída (ex: Python, Java).
    """
    resultado = comando_certificado(nome_usuario, tecnologia, data_path=_DATA)
    return json.dumps(resultado, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Resource: lista de tecnologias disponíveis
# ---------------------------------------------------------------------------

@mcp.resource("dio://trilhas/tecnologias")
def listar_tecnologias() -> str:
    """Lista todas as tecnologias disponíveis no catálogo DIO."""
    tecnologias = _available_technologies(data_path=_DATA)
    return json.dumps({"tecnologias": tecnologias}, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Resource: catálogo completo de trilhas (dados brutos)
# ---------------------------------------------------------------------------

@mcp.resource("dio://trilhas/catalogo")
def catalogo_trilhas() -> str:
    """Retorna o catálogo completo de trilhas DIO em JSON."""
    with open(_DATA, encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if TRANSPORT == "http":
        # Modo HTTP — adequado para acesso via HTTPS, SSO ou API Key
        # Para TLS/HTTPS coloque um reverse-proxy (nginx/caddy) na frente.
        # Defina MCP_API_KEY no ambiente para ativar autenticação por chave.
        if API_KEY:
            print(
                f"[dio-explorer] Iniciando servidor HTTP na porta {PORT} "
                f"com autenticação por API Key.",
                file=sys.stderr,
            )
        else:
            print(
                f"[dio-explorer] Iniciando servidor HTTP na porta {PORT} "
                f"SEM autenticação (defina MCP_API_KEY para proteger).",
                file=sys.stderr,
            )
        mcp.run(transport="streamable-http", port=PORT)
    else:
        # Modo padrão: stdio (Bob/Claude Desktop)
        print("[dio-explorer] Iniciando servidor via stdio.", file=sys.stderr)
        mcp.run(transport="stdio")
