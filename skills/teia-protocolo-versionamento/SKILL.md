---
name: teia-protocolo-versionamento
description: Sistema de protocolo TEIA-AAAA-NNN, versionamento Git, hashes de integridade, manifesto.
---

# TEIA Protocolo de Versionamento

## Numeração
Protocolo: TEIA-AAAA-NNN (ex: TEIA-2026-075)
Versão: v1.0 (entrega), v1.1 (revisão), v2.0 (reestruturação)

## Cabeçalho obrigatório
PROTOCOLO TEIA: TEIA-2026-NNN
VERSÃO: vX.Y | CATEGORIA | TÍTULO | STATUS
DATA | AUTOR | TAMANHO | HASH MD5

## Categorias
01_ANALISE → 02_MAPEAMENTO → 03_SIMULACAO → 04_PLANO
05_ACAO → 06_TERRITORIAL → 07_ACCOUNTABILITY
08_SINTESE → 14_ELEITORAL

## Git
Commit: "TEIA-2026-NNN: Título — descrição"
Tag: vX.Y-nome-do-marco
Push: git push origin main --tags

