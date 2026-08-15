# 🧪 08 - Evaluation Engineering

## 🎯 Objectifs pédagogiques

- Construire un dataset d'évaluation (task, expected, constraints).
- Maîtriser evaluation déterministe, code-based, LLM-as-judge, pairwise.
- Mettre en place des regression datasets et des seuils de blocage.

## ✅ Prérequis

- Chapitre 07 (Observability v0.7).

## 🗺️ Plan

1. Construction d'un dataset de tâches avec résultats attendus.
1. Evaluation déterministe et code-based.
1. LLM-as-judge et évaluation pairwise.
1. Regression set : empêcher qu'une évolution dégrade un comportement déjà validé.
1. Score global (correctness, tests, security, cost, latency) et seuils de blocage.

## 🔗 Ressources

- LangChain Academy - Agent Observability & Evaluation (partie evals).
- Hugging Face Agents Course - unité observabilité/évaluation.

## 📦 Livrable

**Evaluation Framework v0.8** - un score global par run, avec une règle explicite : une
régression fonctionnelle doit pouvoir bloquer l'agent.
