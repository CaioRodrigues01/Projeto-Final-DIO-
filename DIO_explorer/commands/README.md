# 📟 Slash Commands — DIO Explorer

Este diretório contém os slash commands disponíveis no DIO Explorer. Cada arquivo `.md` define um comando, seus parâmetros, instruções de comportamento e o template de saída esperado.

---

## Comandos Disponíveis

| Comando | Arquivo | Descrição |
|---------|---------|-----------|
| `/trilha <tecnologia>` | [`trilha.md`](./trilha.md) | Exibe o plano de estudos de uma trilha a partir do JSON de dados |
| `/desafio <tecnologia> <nivel>` | [`desafio.md`](./desafio.md) | Gera um desafio de código aleatório por tecnologia e nível |
| `/certificado <nome> <tecnologia>` | [`certificado.md`](./certificado.md) | Gera um certificado fictício de conclusão de trilha em Markdown |

---

## Como usar

### `/trilha`
```
/trilha Python
/trilha Java
/trilha React
/trilha Machine Learning
/trilha AWS
```
Consulta o arquivo `data/trilhas_dio.json` e retorna um plano de estudos completo com módulos, badges, lives ao vivo e promoções da trilha.

---

### `/desafio`
```
/desafio Python Básico
/desafio Java Intermediário
/desafio React Avançado
```
Gera um desafio de código aleatório adaptado para a tecnologia e nível informados. Inclui enunciado, exemplos de entrada/saída, restrições e dicas.

---

### `/certificado`
```
/certificado "Ana Silva" Python
/certificado "Carlos Mendes" Java
/certificado "Maria Oliveira" React
```
Gera um certificado fictício de conclusão em Markdown com o nome do usuário, dados da trilha, badges conquistadas e código único de verificação.

---

## Níveis suportados

| Nível | Descrição |
|-------|-----------|
| `Básico` | Conteúdo introdutório, desafios de 15–30 min |
| `Intermediário` | Conteúdo intermediário, desafios de 30–60 min |
| `Avançado` | Conteúdo avançado, desafios de 60–120 min |

---

## Tecnologias disponíveis (via `data/trilhas_dio.json`)

Python · Java · React · Machine Learning · Angular · Node.js · AWS · DevOps · Flutter · Kotlin · TypeScript · Docker · Go · Rust · PHP · Swift · C# · Unity · Data Science · Blockchain

---

> 💡 Os comandos leem dinamicamente o arquivo `data/trilhas_dio.json` — adicionar novas trilhas ao JSON automaticamente expande as capacidades de `/trilha`, `/desafio` e `/certificado`.
