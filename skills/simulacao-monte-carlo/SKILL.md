---
name: simulacao-monte-carlo
description: Simulação de Monte Carlo para calcular probabilidade de sucesso de estratégias políticas.
category: análise quantitativa
---

# Simulação Monte Carlo de Estratégias Políticas

## Quando usar
Quando precisar QUANTIFICAR a probabilidade de cooptar ou neutralizar um veto player.

## Modelo de scores (0-10)
Cada ator recebe:
- PRG: Pragmatismo (flexibilidade ideológica)
- VJU: Vulnerabilidade Jurídica (processos ativos)
- VEL: Vulnerabilidade Eleitoral
- VFI: Vulnerabilidade Financeira/Pessoal
- POD: Poder institucional atual
- IDE: Ideologia/Crença genuína
- MUD: Histórico de mudança de posição
- ALI: Aliados institucionais

## Fórmulas
```python
P_cooptação = 0.15 + PRG*0.04 + MUD*0.03 - IDE*0.05 - ALI*0.01 + ajuste_estratégia
P_neutralização = 0.10 + VJU*0.03 + VEL*0.02 + VFI*0.02 - POD*0.015 - ALI*0.015 - IDE*0.01 + ajuste
P_combinada = 1 - (1-P_coopt)(1-P_neut)  # Pelo menos uma funciona
```

## Estratégias modeláveis
- S1: CPI
- S2: Narrativa pública
- S3: Aliança Judiciário (STF/MPF)
- S4: Coalizão de ganhadores
- S5: Pressão internacional (OCDE)
- S6: CPI + STF combinado
- S7: Via executivo (Planalto)
- S8: Compensação setorial
- S9: Via Judiciário (CNJ/STF sem Congresso)

## Execução
- N = 10.000 iterações por ator × estratégia
- Ruído gaussiano σ=0.2 nos scores
- Reportar média, P10, P90

## Insight crítico
Atores com MAIS processo são MAIS FÁCEIS de mover (têm mais a perder).
Atores LIMPOS e IDEOLÓGICOS são IRREMOVÍVEIS por pressão — só por argumento.
Corrupção é VULNERABILIDADE, não força.

