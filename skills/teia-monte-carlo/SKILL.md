---
name: teia-monte-carlo
description: Simulação de Monte Carlo para probabilidade de sucesso de estratégias políticas. 10.000 iterações por ator × estratégia.
---

# TEIA Monte Carlo

## Quando usar
Quando precisar QUANTIFICAR a probabilidade de cooptar ou neutralizar um veto player.

## Fórmulas
P_cooptação = 0.15 + PRG*0.04 + MUD*0.03 - IDE*0.05 - ALI*0.01 + ajuste
P_neutralização = 0.10 + VJU*0.03 + VEL*0.02 + VFI*0.02 - POD*0.015 - ALI*0.015
P_combinada = 1 - (1-coopt)(1-neut)

## Execução
N=10.000 iterações com ruído gaussiano σ=0.2
Reportar: média, P10, P90

