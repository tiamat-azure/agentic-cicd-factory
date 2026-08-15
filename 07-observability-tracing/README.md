# 🔭 07 - Observability & Tracing

## 🎯 Objectifs pédagogiques

- Faire produire à chaque run une trace complète (agent, modèle, prompt, tool calls,
  tokens, latence, erreurs, coût, résultat).
- Savoir répondre à "pourquoi cette exécution a coûté X et pris Y secondes ?".

## ✅ Prérequis

- Chapitre 06 (Model Router v0.6).

## 🗺️ Plan

1. Anatomie d'une trace de run agentic.
1. Instrumentation du code (spans, corrélation entre steps).
1. Stockage et consultation des traces.
1. Construction d'un dashboard minimal (coût, latence, tokens par run).

## 🔗 Ressources

- LangChain Academy - Agent Observability & Evaluation (partie tracing).

## 📦 Livrable

**Observability v0.7** - un dashboard permettant d'expliquer le coût et la latence de
n'importe quel run passé.
