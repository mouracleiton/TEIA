---
name: teia-transparencia-dados
description: Scraping de APIs públicas (CGU, BCB, TSE, IBGE), dashboard web, detecção de anomalias estatísticas.
---

# TEIA Transparência e Dados

## APIs Públicas Brasileiras
CGU: portaldatransparencia.gov.br/api-de-dados (emendas, convênios)
BCB: olinda.bcb.gov.br (SGS: Selic=11, spread=20783)
TSE: divulgacandcontas.tse.jus.br (candidaturas, doações)
IBGE: servicodados.ibge.gov.br (PIB, IPCA, Censo)
STF: portal.stf.jus.br/api (ADIs, ADPFs)

## Detecção de Anomalias
Z-score robusto: z = 0.6745 × (x - mediana) / MAD; |z|>3.5 = anomalia
Isolation Forest: para anomalias multidimensionais em licitações

## Dashboard
Python + Flask (dashboard_orcamento.py)
API REST: /api/juros, /api/spread, /api/selic, /api/emendas

