# 10 - Agentic CI/CD

## Objectifs pédagogiques

- Faire quitter le projet du statut de prototype.
- Brancher la Factory sur GitHub Actions (lint, tests, security, evals, cost budget, tests
  d'intégration).
- Traiter prompts, tools, modèles, workflows et policies comme des artefacts soumis au
  CI/CD, déclenchant automatiquement les evals.

## Prérequis

- Chapitre 09 (Policy Engine v0.9).

## Plan

1. Pipeline CI/CD cible : build -> tests -> agent evals -> security -> cost checks ->
   deploy.
1. Déclenchement automatique des evals sur changement de
   prompt/tool/modèle/workflow/policy.
1. Intégration avec la CI existante du repo (liens morts) sans la casser.
1. Politique de blocage : un score d'eval sous le seuil bloque le pipeline.

## Livrable

**Agentic CI/CD Factory v1.0** - un `git push` déclenche automatiquement build, tests,
agent evals, security, cost checks et déploiement.
