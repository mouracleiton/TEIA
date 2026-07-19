---
name: pipeline-dialetico
description: Pipeline de análise dialética para documentos de política econômica: tese → fact-check → refutação → contra-refutação → síntese.
category: análise
---

# Pipeline Dialético

## Quando usar
Sempre que precisar produzir um documento de política econômica que precisa SOBREVIVER a escrutínio técnico hostil. Use para teses, propostas de reforma, dossiês de advocacy.

## Pré-requisitos
- Documento inicial (tese/proposta) em TXT
- Acesso a web_search e web_extract para fact-check
- Capacidade de spawnar subagents (delegate_task)

## Passos

### 1. FACT-CHECK (paralelo com refutação)
Para cada número do documento original, verificar contra fonte primária:
- BCB (bcb.gov.br): Selic, spread, crédito, inadimplência
- Tesouro Nacional: DPF, juros, composição da dívida
- IBGE (ibge.gov.br): PIB, IPCA, população
- Receita Federal: arrecadação, carga tributária
- World Bank / FMI: comparações internacionais

Marcar cada item: [FC OK], [FC AJUSTAR], [FC ERRO]

### 2. REFUTAÇÃO (paralelo com fact-check)
Produzir documento hostil atacando:
- Contradições lógicas internas
- Erros de decomposição (somar custos heterogêneos)
- Inversão de causalidade
- Ausência de teoria de mudança
- Falta de teoria de crescimento
- Ignorar limitações constitucionais

Usar teoria econômica: Sargent-Wallace, Goodhart's Law, Baumol, Olson.

### 3. CONTRA-REFUTAÇÃO
Para cada ataque da refutação, aplicar 3 testes:
- VEREDITO = "REFUTAÇÃO VENCE" (remover/reformular)
- VEREDITO = "TEIA VENCE" (manter)
- VEREDITO = "EMPATE TÉCNICO" (reformular)

### 4. SÍNTESE V4.0
Reescrever o documento incorporando:
- Propostas que sobreviveram (intactas)
- Propostas reformuladas (com correções)
- Propostas removidas (derrubadas)
- Categorias separadas (fiscal vs renda privada)

## Armadilhas
- NUNCA somar custos de naturezas diferentes como "poupança redirecionável"
- NUNCA confundir redução de custo de mercado com liberação fiscal
- SEMPRE separar o que precisa de Congresso do que sai via portaria
- SEMPRE citar fonte primária para cada número

## Exemplo de uso
Ver: TEIA-2026-027 (tese) → TEIA-2026-028 (refutação) → TEIA-2026-029 (contra-refutação)

