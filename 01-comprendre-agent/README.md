# 01 - Comprendre réellement ce qu'est un Agent

## Objectifs pédagogiques

- Sortir de la définition marketing "un LLM qui utilise des outils".
- Comprendre la boucle fondamentale : LLM -> Tool calling -> Think/Act/Observe -> State ->
  Loop -> Agent.
- Distinguer LLM application, chain, workflow, agent et système multi-agent.
- Savoir répondre à : quand NE PAS utiliser un agent ?

## Prérequis

- Chapitre 00 (environnement fonctionnel).
- Bases Python (fonctions, classes, boucles).

## Plan

1. Définitions : LLM application vs chain vs workflow vs agent vs multi-agent.
1. La boucle Think -> Act -> Observe.
1. Notion de state et de terminaison.
1. Construction d'un agent minimal sans framework (`agent.py`, `tools.py`, `state.py`).
1. Discussion : critères de décision agent vs non-agent.

## Ressources

- Hugging Face Agents Course, Unit 1.
- Anthropic - Building Effective AI Agents (distinction workflow / agent / multi-agent).

## Livrable

**Agent v0.1** - un agent Python minimal, sans framework, capable d'exécuter 2 à 3 tools
et de terminer une tâche.
