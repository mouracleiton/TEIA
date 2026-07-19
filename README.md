<div align="center">

# TEIA

### Centro de Estudos em Hacker Cultura Periférica

**Pipeline completo de diagnóstico econômico, mapeamento político e plano de execução para reforma institucional no Brasil.**

</div>

---

## O que é

TEIA é um repositório de inteligência analítica que mapeia como o sistema econômico-político brasileiro captura recursos públicos e privados, quem são os atores que lucram com essa captura, e como neutralizá-los para redirecionar capital para qualidade de vida da população.

Não é um manifesto. É um **sistema operacional de advocacy** — 29 documentos técnicos, 1.260.000 simulações matemáticas, 10 documentos de ação prontos, 10 skills metodológicas, tudo versionado em Git.

## Os números

| Indicador | Valor | Fonte |
|-----------|-------|-------|
| Juros da dívida pública pagos em 2024 | R$ 950,4 bi | Tesouro Nacional |
| Spread bancário médio | 28-30 p.p. | BCB SGS 20783 |
| Custo Brasil | R$ 1,7 tri/ano | MBC/CNI |
| Conformidade tributária | 1.501 horas/ano/empresa | World Bank |
| Emendas parlamentares | R$ 28,8 bi/ano (2024) | CGU/Portal da Transparência |
| Cartórios | 13.233 unidades, R$ 31,4 bi/ano | CNJ |
| Probabilidade de prisão por desvio | <2% | estimado |
| Reeleição de prefeitos em cidades-cativo | 93-98% | dados eleitorais |

## Estrutura do repositório

```
TEIA/
│
├── 01_ANALISE/              Pipeline dialético (tese → refutação → contra-refutação)
├── 02_MAPEAMENTO/           Nomes concretos: quem captura, como, por quê
├── 03_SIMULACAO/            Monte Carlo: 1.260.000 cálculos de probabilidade
├── 04_PLANO/                Plano de execução com 20 ações e metas SMART
├── 05_ACAO/                 9 documentos prontos para protocolar/publicar
├── 06_TERRITORIAL/          Fluxo de dinheiro público + privado entre regiões
├── 07_ACCOUNTABILITY/       7 mecanismos para mudar comportamento de gestores
├── 08_SINTESE_FINAL/        Qualidade de vida em 10 dimensões
├── skills/                  10 skills metodológicas reusáveis
└── MANIFESTO_PROTOCOLOS.txt Índice master com hashes de integridade
```

## As 7 fases do pipeline

### Fase 1 — Pipeline Dialético
Tese original (V2.0) → fact-check de 15 números contra fontes primárias → refutação hostil com 6 ataques técnicos → síntese V3.0 incorporando correções.

**Método**: Sargent-Wallace, Goodhart's Law, decomposição oficial BCB do spread, teoria de mudança.

### Fase 2 — Mapeamento Político
Identificação nominal de 50+ parlamentares da legislatura 2023-2027 por eixo de captura: orçamento secreto (Overclean, Moriá), setor financeiro (Banco Master), indústria da complexidade (cartórios, contadores, Sistema S).

**Resultado**: mapa consolidado de 3 sistemas de captura com sobreposição de veto players.

### Fase 3 — Simulação Matemática
Modelo de Monte Carlo com 8 scores por ator (pragmatismo, vulnerabilidade jurídica/eleitoral/financeira, poder, ideologia, histórico de mudança, aliados) × 9 estratégias × 10.000 iterações.

**Descoberta chave**: a estratégia mais eficaz (Via Planalto) custa R$ 0 e tem P=87%. Atores corruptos são MAIS fáceis de mover (têm mais a perder). Atores honestos e ideológicos são irremovíveis por pressão.

### Fase 4 — Plano de Execução
20 ações específicas, 18 metas SMART, 5 KPIs de sucesso, cronograma de 12 meses, orçamento de R$ 6,8 milhões.

### Fase 5 — Documentos de Ação
9 entregáveis prontos:
- Dossiê técnico para o Ministério da Fazenda (3 propostas a custo R$ 0)
- Petição ao CNJ (digitalização de cartórios)
- Amicus curiae no STF (transparência de emendas)
- Representação ao MPF (conflitos de interesse)
- Dossiê Banco Master (10 correlações temporais)
- Roteiro de documentário YouTube
- Série de TikTok (20 roteiros)
- Planejamento de podcast (5 episódios)
- Estatuto social da organização

### Fase 6 — Diagnóstico Territorial
3 eixos: transferências constitucionais (R$ 595 bi/ano), emendas parlamentares (R$ 28,8 bi/ano), concentração de crédito privado.

**Conceito chave**: "Bomba de Drenagem Financeira" — dinheiro público entra no N/NE mas dinheiro privado sai via sistema financeiro, neutralizando as transferências.

### Fase 7 — Accountability
7 mecanismos para transformar a equação de custo-benefício do desvio de recursos públicos. Princípio: não existe sistema que torne todos bons, mas existe sistema que torna o mau comportamento caro.

---

## Como usar

### 1. Entender o diagnóstico

Comece pela síntese:

```bash
# Documento principal (integra todo o pipeline)
cat 08_SINTESE_FINAL/TEIA-2026-027_v1.0_*.txt

# Diagnóstico territorial (fluxo de dinheiro nacional)
cat 06_TERRITORIAL/TEIA-2026-025_v1.0_*.txt
```

### 2. Entender a refutação (teste de stress)

O documento passou por pipeline dialético. Leia a refutação e a contra-refutação para entender o que sobreviveu e o que caiu:

```bash
cat 01_ANALISE/TEIA-2026-028_v1.0_REFUTACAO_*.txt  # 7 ataques
cat 01_ANALISE/TEIA-2026-029_v1.0_CONTRA_REFUTACAO.txt  # vereditos
```

**Placar**: Refutação venceu 2 pontos (RBU impossível, opacidade fiscal). TEIA venceu 2 (gestão em saúde/educação, perfil da dívida). Empate em 3.

### 3. Executar uma ação

Cada documento em `05_ACAO/` tem um destinatário e status:

| Protocolo | Documento | Destinatário | Status |
|-----------|-----------|--------------|--------|
| TEIA-2026-013 | Dossiê Haddad | Min. Fazenda | PROTOCOLO_PENDENTE |
| TEIA-2026-014 | Petição CNJ | Presidente CNJ | PROTOCOLO_PENDENTE |
| TEIA-2026-015 | Amicus curiae | Min. Flávio Dino (STF) | PROTOCOLO_PENDENTE |
| TEIA-2026-016 | Representação MPF | PGR | PROTOCOLO_PENDENTE |
| TEIA-2026-017 | Dossiê Master | Público (online) | PUBLICACAO_PENDENTE |
| TEIA-2026-018 | Documentário | YouTube | PUBLICACAO_PENDENTE |
| TEIA-2026-021 | Estatuto TEIA | Cartório | REGISTRO_PENDENTE |

### 4. Usar uma skill

As 10 skills em `skills/` codificam a metodologia:

```bash
# Ver skills disponíveis
ls skills/

# Exemplo: aplicar pipeline dialético a um novo documento
cat skills/pipeline-dialetico/SKILL.md

# Exemplo: fazer fact-check de um número econômico
cat skills/fact-check-economico/SKILL.md
```

### 5. Verificar integridade

Cada documento tem hash MD5 e SHA-256 no cabeçalho. O manifesto master lista todos:

```bash
cat MANIFESTO_PROTOCOLOS.txt
```

### 6. Versionamento Git

```bash
# Histórico completo
git log --oneline

# Marcos (tags)
git tag

# Comparar versões
git diff v1.0-pipeline-completo..v2.0-dialectico-completo --stat
```

---

## As 10 skills

| # | Skill | O que faz |
|---|-------|-----------|
| 1 | `pipeline-dialetico` | Tese → fact-check → refutação → contra-refutação → síntese |
| 2 | `fact-check-economico` | Verificação contra BCB, STN, IBGE, RFB, TSE, CNJ |
| 3 | `mapeamento-veto-players` | Framework Tsebelis + nomes concretos + vulnerabilidades |
| 4 | `simulacao-monte-carlo` | 8 scores × 9 estratégias × 10.000 iterações |
| 5 | `redacao-juridica-advocacy` | Petição CNJ, amicus STF, representação MPF |
| 6 | `producao-conteudo-advocacy` | Documentário, TikTok, podcast |
| 7 | `diagnostico-territorial` | Bomba de drenagem financeira inter-regional |
| 8 | `accountability-publica` | 7 mecanismos de comportamento |
| 9 | `sistema-protocolo` | TEIA-AAAA-NNN + Git workflow |
| 10 | `posts-instagram-dados` | Carrossel dark/neon com Pillow + opencli |

---

## Resultados da simulação

### Probabilidade de aprovação dos 4 vetores (Combo Ótimo)

| Vetor | Status Quo | Combo Ótimo | Ganho |
|-------|-----------|-------------|-------|
| Gestão da Dívida | 88,2% | 97,7% | +9,5 p.p. |
| Spread Bancário | 61,2% | 85,1% | +23,9 p.p. |
| Desburocratização | 81,9% | 93,8% | +11,9 p.p. |
| Transparência | 88,7% | 97,2% | +8,5 p.p. |

**Combo Ótimo** = Via Planalto + Via CNJ + Aliança Judiciário + CPI Master + Narrativa Pública
**Custo**: R$ 6-12 milhões em 12 meses (mais barato que o V2.0 original)

### Estratégia mais eficaz

**Via Planalto (Lula/Haddad)**: P=87,1%, custo R$ 0, prazo 3-6 meses. Não precisa convencer 257 deputados. Precisa convencer 1 ministro.

---

## Descobertas-chave

1. **A corrupção é vulnerabilidade, não força.** Atores com mais processo (Motta: 98,7%, Lira: 97,4%) são os MAIS fáceis de mover. Atores limpos e ideológicos (André Figueiredo: 8,4%) só se movem por argumento.

2. **70% das ações do plano não precisam de Congresso.** Saem via portaria (Tesouro), resolução (CMN/BCB) ou Judiciário (CNJ/STF).

3. **O dinheiro público que entra no N/NE é aproximadamente igual ao dinheiro privado que sai.** As transferências constitucionais são neutralizadas pela drenagem financeira do sistema bancário.

4. **A pauta é o prêmio.** Quem controla o que NÃO chega a votação (Hugo Motta na Câmara, Alcolumbre no Senado) tem mais poder do que quem vota.

5. **Não existe sistema que torne todos bons. Existe sistema que torna o mau comportamento caro.**

---

## Quem mantém

**Cleiton Moura** (@professorcinza) — analista geopolítico e econômico brasileiro. Criador de conteúdo em TikTok, Instagram e YouTube.

## Licença

Domínio público. Use, modifique, distribua.

---

<div align="center">

**O dinheiro da reforma virá do trabalho.**
**O instrumento de mudança é a gestão.**
**O objetivo é qualidade de vida para todos.**

</div>
