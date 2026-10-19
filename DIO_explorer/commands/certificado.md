# Slash Command: /certificado

## Descrição
Gera um certificado fictício em Markdown com o nome do usuário e a trilha por ele concluída, simulando o certificado de conclusão da DIO.

## Como usar
```
/certificado <nome_do_usuario> <tecnologia>
```

**Exemplos:**
```
/certificado "Ana Silva" Python
/certificado "Carlos Mendes" Java
/certificado "Maria Oliveira" React
/certificado "João Costa" AWS
```

---

## Instruções para o modelo

Quando o usuário chamar `/certificado <nome_do_usuario> <tecnologia>`:

1. Leia o arquivo `data/trilhas_dio.json`.
2. Busque a trilha correspondente à tecnologia informada (ignore maiúsculas/minúsculas).
3. Se não encontrar, informe ao usuário e liste as trilhas disponíveis.
4. Gere a data de emissão com o dia atual.
5. Gere um código de certificado único no formato `DIO-{ANO}{MES}{DIA}-{4_digitos_aleatorios}`.
6. Formate o certificado conforme o template abaixo.

---

## Template de saída

```markdown
---

<div align="center">

# 🎓 CERTIFICADO DE CONCLUSÃO

### *Digital Innovation One — DIO*

---

## Este certificado é conferido a

# ✨ {NOME_DO_USUARIO} ✨

---

### Pela conclusão com êxito da trilha:

## 📘 {nome_da_trilha}

**Tecnologia:** {tecnologia}
**Nível:** {nivel}
**Módulos Concluídos:** {numero_de_modulos} módulos
**XP Conquistado:** {xp_total} XP

---

### 🏅 Badges Conquistadas

{lista_de_badges_com_icone_🔖}

---

### 📊 Conquistas

| Métrica | Resultado |
|---------|-----------|
| ✅ Taxa de Conclusão | 100% |
| 🏆 Nível Alcançado | {nivel} |
| ⭐ XP Total | {xp_total} XP |
| 🎯 Desafios Práticos | Concluídos |
| 📡 Lives Participadas | {quantidade_de_lives} ao vivo |

---

### 📅 Informações do Certificado

**Emitido em:** {data_atual_formato_DD_de_MMMM_de_AAAA}
**Código de Verificação:** `{codigo_certificado}`
**Validade:** Vitalício

---

*"O aprendizado contínuo é o caminho para a excelência em tecnologia."*

**— Equipe DIO | Digital Innovation One**

🌐 [www.dio.me](https://www.dio.me)

</div>

---

> 📌 *Este é um certificado fictício gerado para fins de aprendizado e simulação.*
> *Para um certificado oficial, complete a trilha na plataforma [DIO](https://www.dio.me).*
```

---

## Regras de geração

- O **nome do usuário** deve aparecer exatamente como digitado, com capitalização respeitada.
- O **código de verificação** deve ser único e aleatório, no formato `DIO-AAAAMMDD-XXXX` (ex: `DIO-20250715-4892`).
- A **data de emissão** deve ser a data atual formatada de forma legível em português (ex: "15 de julho de 2025").
- As **badges** devem ser listadas individualmente com emoji 🔖.
- Se a trilha tiver `vitalicio: true`, o certificado deve destacar "Acesso Vitalício à Trilha".
- O certificado deve ter tom **celebratório e motivacional**.
- Ao final do certificado, sempre sugerir o próximo passo: `Use /trilha <próxima_tecnologia> para continuar aprendendo!`
