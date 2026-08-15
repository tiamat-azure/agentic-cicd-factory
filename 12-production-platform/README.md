# 12 - Production : Agent Platform

## Objectifs pédagogiques

- Transformer le prototype en plateforme : Agent Gateway, Agent Runtime, Orchestrator,
  MCP, Model Gateway, Observability/Evals/Cost/Audit.
- Traiter scalabilité, queues, retries, isolation, secrets, multi-tenancy, audit, RBAC,
  haute disponibilité, disaster recovery, model failover, coût, gouvernance.

## Prérequis

- Chapitre 11 (PR Factory v1.1).

## Plan

1. Architecture cible de la plateforme (Gateway, Runtime, Orchestrator, Model Gateway).
1. Scalabilité et résilience : queues, retries, isolation, failover de modèle.
1. Sécurité et gouvernance à l'échelle : secrets, multi-tenancy, RBAC, audit.
1. Observabilité, évaluation et coût en continu, en production.
1. Disaster recovery.

## Livrable final

**Agentic CI/CD Factory v2.0** - une plateforme complète : demande utilisateur -> workflow
agentic -> routing cloud/local -> tools MCP -> modification de code -> tests -> sécurité
-> évaluation -> PR -> approbation humaine -> déploiement -> monitoring en production.
