# 06 - Token Engineering & Model Routing

## Objectifs pédagogiques

- Instrumenter chaque run (input/output/cached tokens, tool calls, itérations, latence,
  coût).
- Définir des budgets d'agent (itérations, tool calls, tokens, coût).
- Construire un routeur de modèles selon la complexité de la tâche.
- Optimiser le coût par tâche réussie, pas le nombre brut de tokens.

## Prérequis

- Chapitre 05 (Model Gateway v0.5).

## Plan

1. Instrumentation minimale : quelles métriques capturer sur chaque run.
1. Budgets déclaratifs (`max_iterations`, `max_tool_calls`, `max_input`, `max_cost`, ...).
1. Task classifier : simple / medium / complex.
1. Routing vers modèle local (8B, 32B) ou cloud frontier selon la classification.
1. Fallback et retry policy.

## Livrable

**Model Router v0.6** - routing, budgets de tokens et de coût, fallback, retry policy,
modèle local par défaut et modèle cloud réservé aux tâches complexes.
