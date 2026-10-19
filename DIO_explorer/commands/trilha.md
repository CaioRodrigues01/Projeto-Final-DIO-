# Slash Command: /trilha

## Descrição
Busca uma trilha de estudos no arquivo `data/trilhas_dio.json` pelo nome da tecnologia e retorna um plano de estudos formatado com os módulos e informações da trilha.

## Como usar
```
/trilha <nome_da_tecnologia>
```

**Exemplos:**
```
/trilha Python
/trilha Java
/trilha React
/trilha Machine Learning
/trilha AWS
```

---

## Instruções para o modelo

Quando o usuário chamar `/trilha <tecnologia>`:

1. Leia o arquivo `data/trilhas_dio.json`.
2. Busque uma trilha cuja propriedade `tecnologia` corresponda (ignore maiúsculas/minúsculas) ao argumento informado.
3. Se não encontrar nenhuma trilha, informe ao usuário e liste as tecnologias disponíveis.
4. Se encontrar, gere um plano de estudos formatado em Markdown conforme o template abaixo.

---

## Template de saída

```markdown
# 🎯 Trilha de Estudos: {nome}

**🏷️ Tecnologia:** {tecnologia}
**📊 Nível:** {nivel}
**📦 Total de Módulos:** {numero_de_modulos}
**⭐ XP Total:** {xp_total} XP

---

## 📚 Plano de Estudos — {numero_de_modulos} Módulos

| # | Módulo | Objetivo |
|---|--------|----------|
| 1 | Fundamentos de {tecnologia} | Introdução e conceitos básicos |
| 2 | Ambiente e Ferramentas | Configuração do ambiente de desenvolvimento |
| ... (gerar módulos realistas até o total de {numero_de_modulos}) |

---

## 🏅 Badges Disponíveis

{para cada badge em badges_disponiveis: "- 🔖 {badge}"}

---

## 📡 Lives ao Vivo

{para cada live em lives_ao_vivo:
"### 🎥 {titulo}
📅 Data: {data}
⏱️ Duração: {duracao_minutos} minutos"}

---

## 💰 Promoção Ativa

{se desconto_percentual > 0:
"- 🎟️ Cupom: `{cupom}`
- 💸 Desconto: {desconto_percentual}%
- 📅 Válido até: {validade}"
senão: "Nenhuma promoção ativa no momento."}

---

## ♾️ Acesso

{se vitalicio: "✅ Acesso **Vitalício**" senão: "⏳ Acesso **por tempo limitado**"}

---

> 💡 *Use `/desafio {tecnologia}` para receber um desafio de código e `/certificado <seu_nome> {tecnologia}` ao concluir a trilha!*
```
