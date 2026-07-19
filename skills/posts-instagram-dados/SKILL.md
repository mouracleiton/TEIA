---
name: posts-instagram-dados
description: Criação de carrosséis de Instagram com dados econômicos verificados e design dark/neon.
category: comunicação
---

# Posts de Instagram com Dados

## Quando usar
Quando precisar transformar dados econômicos em carrossel visual para Instagram.

## Ferramentas
- Python + Pillow (geração de imagens)
- opencli (publicação no Instagram)

## Estrutura do carrossel (8 slides)
1. CAPA: título de impacto + número-chave + @professorcinza
2. A CONTA: comparação (juros vs áreas sociais)
3. PROPORÇÃO: per capita ou por dia
4. QUEM RECEBE: distribuição (% por setor)
5. COMPARAÇÃO: internacional ou histórica
6. IMPACTO: o que significa para o cidadão
7. SISTEMA: como funciona (ciclo)
8. SOLUÇÃO + CTA: o que fazer + compartilha/cobre

## Design
- Tamanho: 1080x1080 (quadrado)
- Cores: BG_DARK=(10,12,20), BG_CARD=(18,22,35), NEON_BLUE=(0,191,255), NEON_RED=(255,51,51)
- Fontes: DejaVuSans-Bold (sistema)
- Cada número na tela tem FONTE citada

## Publicação
```bash
opencli instagram post "LEGENDA" --media slide_01.png,slide_02.png,...
```

## Regras
1. NUNCA inventar dados — usar verificados do pipeline
2. SEMPRE citar fonte no slide (overlay)
3. Corrigir números antes de publicar (ex: R$ 950 bi não R$ 800 bi)
4. Legenda com hashtags relevantes
5. CTAs claros: compartilha, envia pro grupo, cobra seu deputado

