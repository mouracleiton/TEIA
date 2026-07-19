# Skills do TEIA — Sistema Operacional Político Brasileiro

O TEIA mantém 20 skills que codificam toda a inteligência desenvolvida no pipeline. As skills estão divididas em dois grupos: as 10 skills originais (metodologia geral) e as 10 skills TEIA (sistema operacional político específico).

## Skills TEIA (10 novas — sistema operacional político)

| # | Skill | Quando usar |
|---|-------|-------------|
| 11 | `teia-pipeline-dialetico` | Tese → fact-check → refutação → contra → síntese |
| 12 | `teia-mapeamento-veto-players` | 8 scores por ator + 9 estratégias de cooptação |
| 13 | `teia-monte-carlo` | Simulação 10.000 iterações de probabilidade política |
| 14 | `teia-sistema-operacional-politico` | 9 axiomas + 12 níveis + 66 dimensões (SOPBRA) |
| 15 | `teia-documentos-juridicos` | Petição CNJ, amicus STF, representação MPF |
| 16 | `teia-conteudo-advocacy` | Documentário YouTube, TikTok 60s, podcast |
| 17 | `teia-framework-matriz` | Matriz 66×24 + PET (5 fases) + Quality (32 itens) |
| 18 | `teia-eleitoral-2026` | Agenda-setting, Cartão de Emendas, Compromisso TEIA |
| 19 | `teia-transparencia-dados` | APIs CGU/BCB/TSE, dashboard, anomalias z-score |
| 20 | `teia-protocolo-versionamento` | TEIA-AAAA-NNN, Git workflow, hashes MD5/SHA-256 |

## Skills Originais (10 — metodologia geral)

| # | Skill | Quando usar |
|---|-------|-------------|
| 1 | `pipeline-dialetico` | Estrutura do pipeline (mesma que TEIA-11) |
| 2 | `fact-check-economico` | Fontes primárias brasileiras (BCB, STN, IBGE, TSE) |
| 3 | `mapeamento-veto-players` | Framework Tsebelis + nomes concretos |
| 4 | `simulacao-monte-carlo` | Modelo de 8 scores + 9 estratégias |
| 5 | `redacao-juridica-advocacy` | Tipos de documento jurídico |
| 6 | `producao-conteudo-advocacy` | Formatos de conteúdo |
| 7 | `diagnostico-territorial` | Bomba de drenagem financeira |
| 8 | `accountability-publica` | 7 mecanismos de comportamento |
| 9 | `sistema-protocolo` | Numeração TEIA + Git |
| 10 | `posts-instagram-dados` | Carrossel Pillow + opencli |

## Como usar

Cada skill em `skills/<nome>/SKILL.md` com:
- **Quando usar**: critério de ativação
- **Passos**: procedimento
- **Armadilhas**: erros a evitar
- **Exemplos**: referência a documentos do pipeline

## Estrutura

```
TEIA_protocolos/
├── skills/
│   ├── [10 skills originais]/
│   ├── teia-pipeline-dialetico/SKILL.md
│   ├── teia-mapeamento-veto-players/SKILL.md
│   ├── teia-monte-carlo/SKILL.md
│   ├── teia-sistema-operacional-politico/SKILL.md
│   ├── teia-documentos-juridicos/SKILL.md
│   ├── teia-conteudo-advocacy/SKILL.md
│   ├── teia-framework-matriz/SKILL.md
│   ├── teia-eleitoral-2026/SKILL.md
│   ├── teia-transparencia-dados/SKILL.md
│   └── teia-protocolo-versionamento/SKILL.md
```

## O que cada skill TEIA comprime

**teia-pipeline-dialetico**: Todo o método de validação por escrutínio hostil desenvolvido ao longo de 50+ documentos. O pipeline completo de tese → fact-check → refutação → contra-refutação → síntese, com as armadilhas identificadas (não somar custos heterogêneos, não confundir custo de mercado com liberação fiscal, separar portaria de Congresso).

**teia-mapeamento-veto-players**: O modelo de 8 scores (PRG, VJU, VEL, VFI, POD, IDE, MUD, ALI) aplicado a 14+ parlamentares brasileiros. A tipologia (VULNERÁVEL/PRAGMÁTICO/IDEOLÓGICO/IRREMOVÍVEL) e a descoberta crítica de que corrupção é vulnerabilidade, não força.

**teia-monte-carlo**: A formula matemática completa de P_cooptação e P_neutralização, com as 9 estratégias modeladas e seus resultados validados (Via Planalto P=87%, Via CNJ P=74%, etc.).

**teia-sistema-operacional-politico**: Os 9 axiomas do kernel (K1-K9) que governam o sistema político brasileiro, os 12 níveis de profundidade do poder, e as 66 dimensões de captura organizadas do gene ao espaço sideral.

**teia-documentos-juridicos**: As 3 categorias de documento jurídico (petição CNJ, amicus STF, representação MPF) com base legal específica de cada um, estrutura formal, e regras de ouro (presunção de inocência, fonte pública, revisão OAB).

**teia-conteudo-advocacy**: A estrutura de comunicação em 3 níveis: documentário YouTube (7 blocos), série TikTok (60 segundos com hook/corpo/CTA), e podcast quinzenal. Regras de rigor (nunca inventar dado, sempre citar fonte) e de psicologia (Sistema 1 emocional E Sistema 2 analítico).

**teia-framework-matriz**: A matriz completa 66×24=1.584 perspectivas, o PET (Protocolo de Execução em 5 fases), e o Protocolo de Qualidade de 32 itens que todo documento TEIA deve passar antes de publicar.

**teia-eleitoral-2026**: A estratégia eleitoral completa: 5 pilares (agenda-setting, Cartão de Emendas, coalizão, narrativa gestão vs captura, integridade), a campanha "Não É Todo Político", e o Questionário TEIA de 10 perguntas para candidatos.

**teia-transparencia-dados**: As APIs públicas brasileiras mapeadas (CGU, BCB, TSE, IBGE, STF, INPE, DATASUS), os métodos de detecção de anomalias (z-score robusto, Isolation Forest), e a arquitetura do dashboard Flask.

**teia-protocolo-versionamento**: O sistema completo de protocolo TEIA-AAAA-NNN, versionamento Git com tags em marcos, hashes MD5/SHA-256 para integridade, e o manifesto de rastreabilidade.
