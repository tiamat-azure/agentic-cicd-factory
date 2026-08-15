# Agentic CI/CD Factory

Formation - parcours, prérequis, sommaire.

## Objectif

Concevoir, produire et déployer une usine CI/CD nativement agentic : LLM-agnostic, hybride
(cloud + local), optimisée en consommation de tokens, avec observabilité et évaluation
structurée.

## Fil rouge

Un seul projet traverse les 12 chapitres : la **Agentic CI/CD Factory**, une plateforme
capable de recevoir une demande de développement, l'analyser, la planifier, modifier le
code, tester, reviewer, produire une PR, puis décider - selon des policies et des
évaluations - de continuer automatiquement ou de demander une validation humaine. Voir
[`ressources/prd/01-PRD.md`](ressources/prd/01-PRD.md) pour le raisonnement complet.

## Prérequis

Voir [`00-setup/`](00-setup/).

## Sommaire

Seuls les chapitres listés comme "prêt" ont un contenu au-delà du plan. Ce qui n'est pas
listé n'est pas prêt.

| #   | Chapitre                                                              | Livrable                  | Statut      |
| --- | --------------------------------------------------------------------- | ------------------------- | ----------- |
| 00  | [Setup](00-setup/)                                                    | Environnement fonctionnel | _à rédiger_ |
| 01  | [Comprendre l'Agent](01-comprendre-agent/)                            | Agent v0.1                | **prêt**    |
| 02  | [Tools, Function Calling & environnement](02-tools-function-calling/) | Agent v0.2 - Coding Agent | _à rédiger_ |
| 03  | [Workflows & orchestration](03-workflows-orchestration/)              | Factory v0.3              | _à rédiger_ |
| 04  | [MCP](04-mcp/)                                                        | Tools via MCP             | _à rédiger_ |
| 05  | [LLM Agnostic](05-llm-agnostic/)                                      | Model Gateway v0.5        | _à rédiger_ |
| 06  | [Token Engineering & Model Routing](06-token-engineering-routing/)    | Model Router v0.6         | _à rédiger_ |
| 07  | [Observability & Tracing](07-observability-tracing/)                  | Observability v0.7        | _à rédiger_ |
| 08  | [Evaluation Engineering](08-evaluation-engineering/)                  | Evaluation Framework v0.8 | _à rédiger_ |
| 09  | [Agent Security & Governance](09-security-governance/)                | Policy Engine v0.9        | _à rédiger_ |
| 10  | [Agentic CI/CD](10-agentic-cicd/)                                     | Factory v1.0              | _à rédiger_ |
| 11  | [Automatic PR Factory](11-pr-factory/)                                | PR Factory v1.1           | _à rédiger_ |
| 12  | [Production : Agent Platform](12-production-platform/)                | Factory v2.0              | _à rédiger_ |

## Ressources

Voir [`ressources/`](ressources/) - cheatsheets, glossaire, liens (jamais dupliqué dans
les chapitres).

## Structure

Voir [`ressources/prd/PRD.md`](ressources/prd/PRD.md) pour le raisonnement derrière
l'organisation du repo (Scénario A : dossiers numérotés sur `main`) et
[`ressources/prd/01-PRD.md`](ressources/prd/01-PRD.md) pour le raisonnement derrière le
parcours en 12 chapitres.
