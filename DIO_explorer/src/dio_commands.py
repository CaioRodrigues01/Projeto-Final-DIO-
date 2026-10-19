"""
DIO Explorer — implementação dos comandos /trilha, /desafio e /certificado.
"""

import json
import os
import random
from datetime import date

# Caminho padrão para o JSON de trilhas
_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "trilhas_dio.json")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_trilhas(data_path: str = _DATA_PATH) -> list:
    """Carrega e retorna a lista de trilhas do arquivo JSON."""
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)["trilhas"]


def _find_trilha(tecnologia: str, data_path: str = _DATA_PATH):
    """Busca uma trilha pelo nome da tecnologia (case-insensitive).

    Retorna o dict da trilha ou None se não encontrado.
    """
    trilhas = _load_trilhas(data_path)
    for t in trilhas:
        if t["tecnologia"].lower() == tecnologia.lower():
            return t
    return None


def _available_technologies(data_path: str = _DATA_PATH) -> list:
    """Retorna a lista de tecnologias disponíveis."""
    return [t["tecnologia"] for t in _load_trilhas(data_path)]


# ---------------------------------------------------------------------------
# /trilha
# ---------------------------------------------------------------------------

DESAFIOS_POR_NIVEL = {
    "Básico": [
        "Calcular a soma de todos os números de uma lista",
        "Verificar se uma string é um palíndromo",
        "Contar a frequência de cada elemento em um array",
        "Converter temperatura de Celsius para Fahrenheit e vice-versa",
        "Verificar se um número é primo",
        "Gerar os N primeiros números da sequência de Fibonacci",
        "Inverter uma string sem usar funções nativas",
        "Verificar se dois arrays têm os mesmos elementos",
    ],
    "Intermediário": [
        "Implementar uma pilha (stack) com as operações push, pop e peek",
        "Criar uma função de busca binária em uma lista ordenada",
        "Implementar o algoritmo de ordenação Merge Sort",
        "Criar um sistema simples de cache com expiração por tempo (TTL)",
        "Construir um parser de expressões matemáticas simples",
        "Implementar o padrão Observer (publisher/subscriber)",
        "Criar uma API REST com operações CRUD para uma entidade simples",
        "Implementar debounce e throttle manualmente",
    ],
    "Avançado": [
        "Implementar um sistema de filas de tarefas com prioridade e workers concorrentes",
        "Criar um interpretador de uma linguagem de template customizada",
        "Implementar um algoritmo de pathfinding (A* ou Dijkstra) em um grafo",
        "Construir um sistema de cache distribuído com invalidação em tempo real",
        "Implementar um motor de regras de negócio (rule engine) configurável via JSON",
        "Criar um sistema de versionamento de dados com histórico de alterações",
        "Implementar lazy evaluation e memoization para expressões matemáticas pesadas",
        "Construir um compilador simples de expressões regulares",
    ],
}

XP_RANGES = {
    "Básico": (100, 300),
    "Intermediário": (300, 600),
    "Avançado": (600, 1200),
}

TEMPO_RANGES = {
    "Básico": (15, 30),
    "Intermediário": (30, 60),
    "Avançado": (60, 120),
}


def comando_trilha(tecnologia: str, data_path: str = _DATA_PATH) -> dict:
    """Executa o comando /trilha.

    Returns:
        dict com ``status`` ('ok' ou 'not_found') e campos relevantes.
    """
    trilha = _find_trilha(tecnologia, data_path)
    if trilha is None:
        return {
            "status": "not_found",
            "mensagem": f"Trilha '{tecnologia}' não encontrada.",
            "tecnologias_disponiveis": _available_technologies(data_path),
        }

    promo = trilha["promocoes"]
    return {
        "status": "ok",
        "id": trilha["id"],
        "nome": trilha["nome"],
        "tecnologia": trilha["tecnologia"],
        "nivel": trilha["nivel"],
        "numero_de_modulos": trilha["numero_de_modulos"],
        "xp_total": trilha["xp_total"],
        "badges_disponiveis": trilha["badges_disponiveis"],
        "lives_ao_vivo": trilha["lives_ao_vivo"],
        "promocao": {
            "desconto_percentual": promo["desconto_percentual"],
            "cupom": promo["cupom"],
            "validade": promo["validade"],
        },
        "vitalicio": trilha["vitalicio"],
    }


# ---------------------------------------------------------------------------
# /desafio
# ---------------------------------------------------------------------------

def comando_desafio(tecnologia: str, nivel: str, data_path: str = _DATA_PATH) -> dict:
    """Executa o comando /desafio.

    Returns:
        dict com ``status`` e os campos do desafio gerado.
    """
    niveis_validos = list(DESAFIOS_POR_NIVEL.keys())

    # Valida tecnologia
    trilha = _find_trilha(tecnologia, data_path)
    if trilha is None:
        return {
            "status": "not_found",
            "mensagem": f"Tecnologia '{tecnologia}' não encontrada.",
            "tecnologias_disponiveis": _available_technologies(data_path),
        }

    # Valida nível
    nivel_normalizado = next(
        (n for n in niveis_validos if n.lower() == nivel.lower()), None
    )
    if nivel_normalizado is None:
        return {
            "status": "nivel_invalido",
            "mensagem": f"Nível '{nivel}' inválido.",
            "niveis_validos": niveis_validos,
        }

    enunciado = random.choice(DESAFIOS_POR_NIVEL[nivel_normalizado])
    xp_min, xp_max = XP_RANGES[nivel_normalizado]
    tempo_min, tempo_max = TEMPO_RANGES[nivel_normalizado]

    return {
        "status": "ok",
        "tecnologia": trilha["tecnologia"],
        "nivel": nivel_normalizado,
        "numero_desafio": random.randint(1, 999),
        "enunciado": enunciado,
        "xp": random.randint(xp_min, xp_max),
        "tempo_sugerido_minutos": random.randint(tempo_min, tempo_max),
    }


# ---------------------------------------------------------------------------
# /certificado
# ---------------------------------------------------------------------------

def _gerar_codigo_certificado(hoje: date = None) -> str:
    """Gera um código único no formato DIO-AAAAMMDD-XXXX."""
    hoje = hoje or date.today()
    sufixo = random.randint(1000, 9999)
    return f"DIO-{hoje.strftime('%Y%m%d')}-{sufixo}"


def comando_certificado(
    nome_usuario: str,
    tecnologia: str,
    data_path: str = _DATA_PATH,
    hoje: date = None,
) -> dict:
    """Executa o comando /certificado.

    Returns:
        dict com ``status`` e os dados do certificado.
    """
    trilha = _find_trilha(tecnologia, data_path)
    if trilha is None:
        return {
            "status": "not_found",
            "mensagem": f"Trilha '{tecnologia}' não encontrada.",
            "tecnologias_disponiveis": _available_technologies(data_path),
        }

    hoje = hoje or date.today()
    codigo = _gerar_codigo_certificado(hoje)

    return {
        "status": "ok",
        "nome_usuario": nome_usuario,
        "nome_trilha": trilha["nome"],
        "tecnologia": trilha["tecnologia"],
        "nivel": trilha["nivel"],
        "numero_de_modulos": trilha["numero_de_modulos"],
        "xp_total": trilha["xp_total"],
        "badges": trilha["badges_disponiveis"],
        "lives_participadas": len(trilha["lives_ao_vivo"]),
        "vitalicio": trilha["vitalicio"],
        "data_emissao": hoje.strftime("%d/%m/%Y"),
        "codigo_certificado": codigo,
    }
