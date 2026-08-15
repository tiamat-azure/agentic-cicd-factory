# 🧰 00 - Setup

## 🎯 Objectifs pédagogiques

Préparer l'environnement technique avant de démarrer le parcours : aucun concept agentic
n'est abordé ici, uniquement de l'outillage.

## ✅ Prérequis

- [uv](https://docs.astral.sh/uv/) (gestionnaire Python officiel de la formation) et
  Python 3.11+ - `uv` installe et pilote lui-même l'interpréteur et les environnements.
- Un compte GitHub avec un token personnel (`repo`, `workflow`).
- Un accès à au moins un LLM cloud (Anthropic ou OpenAI) via clé API.
- [Ollama](https://ollama.com) ou [vLLM](https://docs.vllm.ai) installé localement pour la
  partie hybride (à partir du chapitre 05).
- Git configuré (nom, email, clé SSH ou token HTTPS).

## 🗺️ Plan

1. Installation d'`uv` et des dépendances communes (`uv sync` dans le chapitre visé).
1. Configuration des accès LLM (clé cloud + modèle local).
1. Vérification que le repo se clone, que la CI de liens morts tourne en local.
1. Premier appel LLM "hello world" pour valider la chaîne bout en bout.

## 📦 Livrable

Un environnement fonctionnel capable d'appeler un LLM cloud et un LLM local.
