# Slash Command: /desafio

## Descrição
Gera um desafio de código aleatório baseado na tecnologia e nível escolhidos pelo usuário. O desafio inclui enunciado, exemplos de entrada/saída e dicas.

## Como usar
```
/desafio <tecnologia> <nivel>
```

**Níveis disponíveis:** `Básico` | `Intermediário` | `Avançado`

**Exemplos:**
```
/desafio Python Básico
/desafio Java Intermediário
/desafio React Avançado
/desafio Node.js Intermediário
```

---

## Instruções para o modelo

Quando o usuário chamar `/desafio <tecnologia> <nivel>`:

1. Verifique se a tecnologia e o nível são válidos (consulte `data/trilhas_dio.json` para as tecnologias disponíveis).
2. Gere **aleatoriamente** um dos desafios do banco abaixo correspondente ao nível, adaptando-o para a tecnologia informada.
3. Formate a saída conforme o template abaixo.
4. Ao final, pergunte se o usuário quer ver a solução ou tentar outro desafio.

---

## Banco de Desafios por Nível

### 🟢 Básico
- Calcular a soma de todos os números de uma lista
- Verificar se uma string é um palíndromo
- Contar a frequência de cada elemento em um array
- Converter temperatura de Celsius para Fahrenheit e vice-versa
- Verificar se um número é primo
- Gerar os N primeiros números da sequência de Fibonacci
- Inverter uma string sem usar funções nativas
- Verificar se dois arrays têm os mesmos elementos

### 🟡 Intermediário
- Implementar uma pilha (stack) com as operações push, pop e peek
- Criar uma função de busca binária em uma lista ordenada
- Implementar o algoritmo de ordenação Merge Sort
- Criar um sistema simples de cache com expiração por tempo (TTL)
- Construir um parser de expressões matemáticas simples
- Implementar o padrão Observer (publisher/subscriber)
- Criar uma API REST com operações CRUD para uma entidade simples
- Implementar debounce e throttle manualmente

### 🔴 Avançado
- Implementar um sistema de filas de tarefas com prioridade e workers concorrentes
- Criar um interpretador de uma linguagem de template customizada
- Implementar um algoritmo de pathfinding (A* ou Dijkstra) em um grafo
- Construir um sistema de cache distribuído com invalidação em tempo real
- Implementar um motor de regras de negócio (rule engine) configurável via JSON
- Criar um sistema de versionamento de dados com histórico de alterações
- Implementar lazy evaluation e memoization para expressões matemáticas pesadas
- Construir um compilador simples de expressões regulares

---

## Template de saída

```markdown
# ⚔️ Desafio {tecnologia} — Nível {nivel}

**🆔 Desafio #{numero_aleatorio}**
**🏷️ Categoria:** {categoria}
**⏱️ Tempo Sugerido:** {tempo} minutos
**⭐ XP ao Completar:** {xp} XP

---

## 📋 Enunciado

{enunciado_detalhado_do_desafio}

---

## 📥 Exemplos

### Entrada
```
{exemplo_entrada}
```

### Saída Esperada
```
{exemplo_saida}
```

---

## 📌 Restrições

- {restricao_1}
- {restricao_2}
- {restricao_3}

---

## 💡 Dicas

> 🔍 Dica 1: {dica_1}
> 🔍 Dica 2: {dica_2}

---

## 🚀 Bora codar!

Quando terminar, compartilhe sua solução aqui para receber feedback.
Ou use `/desafio {tecnologia} {nivel}` para gerar outro desafio!
```

---

## Regras de geração

- O **número do desafio** deve ser um número aleatório entre 1 e 999.
- O **tempo sugerido** deve variar: Básico = 15–30 min, Intermediário = 30–60 min, Avançado = 60–120 min.
- O **XP** deve variar: Básico = 100–300 XP, Intermediário = 300–600 XP, Avançado = 600–1200 XP.
- O enunciado deve ser **adaptado para a tecnologia específica** (ex: se for Python, use sintaxe Python nos exemplos; se for React, use JSX/hooks).
- Os exemplos de entrada/saída devem ser **concretos e testáveis**.
- As dicas devem ajudar sem entregar a solução.
