---
name: fact-check-economico
description: Verificação de números econômicos brasileiros contra fontes primárias oficiais.
category: análise
---

# Fact-Check Econômico

## Quando usar
Sempre que um documento citar números econômicos do Brasil (PIB, Selic, spread, juros, arrecadação, etc).

## Fontes primárias por tipo de dado

| DADO | FONTE | URL/REFERÊNCIA |
|------|-------|----------------|
| PIB nominal | IBGE | ibge.gov.br, Contas Nacionais |
| IPCA | IBGE | ibge.gov.br, índice de preços |
| Selic | BCB | bcb.gov.br, Copom |
| Spread bancário | BCB | SGS série 20783 |
| Juros da DPF | Tesouro Nacional | tesourotransparente.gov.br |
| Estoque DPF | Tesouro Nacional | Relatório Mensal da DPF |
| Composição dívida | Tesouro Nacional | DPMFi por indexador |
| Arrecadação | Receita Federal | Estudo Carga Tributária |
| Carga tributária | Receita Federal | % do PIB anual |
| Custo Brasil | MBC/CNI | Índice Custo Brasil |
| Conformidade trib. | IBPT/ETCO/World Bank | horas/ano |
| Concentração bancária | BCB | Relatório de Estabilidade Financeira |
| Cooperativas | BCB | Panorama do SNCC |
| Emendas parlamentares | CGU/Portal Transparência | portaldatransparencia.gov.br |
| Doações eleitorais | TSE | DivulgaCandContas |

## Marcadores
- [FC OK] = valor correto (dentro de margem)
- [FC AJUSTAR] = direção certa, valor precisa atualização
- [FC ERRO] = valor significativamente divergente

## Erros comuns
- Confundir PIB nominal com PIB real ou PPP
- Usar Selic nominal sem descontar IPCA (juro real ≠ juro nominal)
- Citar spread de 22 p.p. quando o correto é 28-30 p.p. (SGS 20783)
- Citar prefixação como "15%→25-30%" quando já está em 47% (nov/2024)
- Confundir juros pagos (R$ 950 bi) com "para bancos" (80% vai para SFN mas inclui fundos de pensão, pessoa física, etc.)

