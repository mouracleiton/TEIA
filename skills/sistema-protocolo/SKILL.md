---
name: sistema-protocolo
description: Sistema de versionamento e numeração de protocolo para documentos do TEIA.
category: gestão
---

# Sistema de Protocolo TEIA

## Quando usar
Sempre que criar, revisar ou versionar um documento no repositório TEIA.

## Nomenclatura
- Protocolo: TEIA-AAAA-NNN (ex: TEIA-2026-030)
- Versão: v1.0 (entrega inicial), v1.1 (revisão menor), v2.0 (reestruturação)
- Arquivo: TEIA-2026-NNN_vX.Y_NOME.txt

## Cabeçalho obrigatório
Cada arquivo DEVE iniciar com:
```
================================================================================
PROTOCOLO TEIA: TEIA-2026-NNN
VERSÃO: vX.Y
CATEGORIA: 0X_NOME
TÍTULO: ...
STATUS: INTERNO | PROTOCOLO_PENDENTE | PUBLICACAO_PENDENTE | REGISTRO_PENDENTE
DATA: DD/MM/AAAA
AUTOR: Cleiton Moura (@professorcinza) — TEIA
TAMANHO: X bytes (Y KB)
HASH MD5: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
================================================================================
```

## Categorias
01_ANALISE — Pipeline dialetico, fact-check, refutação
02_MAPEAMENTO — Mapeamento político, veto players
03_SIMULACAO — Monte Carlo, modelagem
04_PLANO — Planos de execução, metas SMART
05_ACAO — Documentos protocoláveis (dossiês, petições, roteiros)
06_TERRITORIAL — Diagnóstico territorial
07_ACCOUNTABILITY — Accountability e comportamento
08_SINTESE_FINAL — Sínteses integradoras

## Status
- INTERNO: análise técnica, não para distribuição
- PROTOCOLO_PENDENTE: pronto para protocolar (CNJ/STF/MPF)
- PUBLICACAO_PENDENTE: pronto para publicar (YouTube/TikTok/podcast)
- REGISTRO_PENDENTE: pronto para registrar (cartório/junta)

## Git workflow
```bash
cd /home/kratos/TEIA_protocolos

# Criar novo documento
# ... editar arquivo ...

# Adicionar e commitar
git add -A
git commit -m "TEIA-2026-NNN: Título — descrição curta"

# Tag em marcos
git tag -a vX.Y-nome-do-marco -m "Descrição do marco"

# Empurrar
git push origin main --tags
```

## Hashes
Cada arquivo tem hash MD5 e SHA-256 no cabeçalho.
Qualquer alteração gera nova versão (v1.1, v1.2...) preservando a anterior.

