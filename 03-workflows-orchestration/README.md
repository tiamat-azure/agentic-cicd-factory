# 🕸️ 03 - Workflows & orchestration

## 🎯 Objectifs pédagogiques

- Introduire LangGraph comme runtime d'orchestration (sans en devenir expert).
- Maîtriser les concepts : State, Node, Edge, Conditional Edge, Checkpoint, Human
  approval.
- Connaître les patterns Anthropic : sequential, parallel, evaluator-optimizer,
  orchestration.

## ✅ Prérequis

- Chapitre 02 (Agent v0.2 - Coding Agent).

## 🗺️ Plan

1. Pourquoi passer d'une boucle agent unique à un graphe de nodes explicites.
1. State, Node, Edge, Conditional Edge.
1. Checkpoints et reprise sur erreur.
1. Points d'approbation humaine dans un graphe.
1. Construction du workflow REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW ->
   PR.

## 🔗 Ressources

- Hugging Face Agents Course - module LangGraph.
- Anthropic - Building Effective AI Agents (patterns d'orchestration).

## 📦 Livrable

**Agentic CI/CD Factory v0.3** - un workflow déterministe, avec étapes explicites, capable
de transformer une demande en modification de code.
