# 04 - MCP : transformer les Tools en plateforme

## Objectifs pédagogiques

- Passer de tools codés en dur à une architecture Host / Client / Server standardisée.
- Comprendre les concepts MCP : tools, resources, prompts, sessions, capability
  negotiation.
- Identifier les frontières de sécurité introduites par MCP.

## Prérequis

- Chapitre 03 (Agentic CI/CD Factory v0.3).

## Plan

1. Architecture MCP : Host, Client, Server.
1. Tools, resources et prompts exposés par un serveur MCP.
1. Sessions et capability negotiation.
1. Sécurité : ce qu'un serveur MCP peut et ne peut pas exposer.
1. Migration de tools natifs vers des serveurs MCP (Git, GitHub, Filesystem, CI).

## Ressources

- Model Context Protocol - spécification (architecture).

## Livrable

Remplacement d'au moins 3 tools natifs de l'agent par des serveurs MCP.
