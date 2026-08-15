# 🤖 05 - LLM Agnostic : découpler Agent et modèle

## 🎯 Objectifs pédagogiques

- Construire une abstraction `LLMProvider` (generate, count_tokens, capabilities).
- Introduire un Model Gateway entre l'agent et les fournisseurs de modèles.
- Comparer Anthropic, APIs compatibles OpenAI, Ollama, vLLM.
- Pouvoir changer de modèle par simple changement de configuration, sans toucher au code
  métier de l'agent.

## ✅ Prérequis

- Chapitre 04 (agent avec tools MCP).
- Un modèle local disponible via Ollama ou vLLM (voir chapitre 00).

## 🗺️ Plan

1. Pourquoi l'agent ne doit jamais dépendre directement d'une API de modèle.
1. Interface `LLMProvider` : contrat commun.
1. Implémentations : Anthropic, OpenAI-compatible, Ollama, vLLM.
1. Model Gateway et sélection par configuration (`model: claude` / `model: qwen`).
1. Tests de non-régression : même agent, plusieurs modèles.

## 📦 Livrable

**Model Gateway v0.5** - la même Agentic CI/CD Factory fonctionne avec Claude et un modèle
local (Qwen), sans modification du code métier de l'agent.
