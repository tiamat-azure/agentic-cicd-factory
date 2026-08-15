# ☁️ 12 - Production : Agent Platform

> Livrable : **Factory v2.0** - une plateforme agentique de production, capable de
> recevoir une demande, orchestrer les agents, gouverner les actions, mesurer la qualité,
> contrôler le coût et reprendre après incident.

## 🎯 Objectifs pédagogiques

- Transformer la PR Factory v1.1 en plateforme exploitable par plusieurs équipes.
- Dessiner l'architecture cible : Agent Gateway, Runtime, Orchestrator, MCP Gateway, Model
  Gateway, Policy Engine, Eval Service, Observability et Cost Control.
- Dimensionner scalabilité, files de travail, isolation, retries, idempotence et backpressure.
- Appliquer sécurité et gouvernance en production : identités séparées, RBAC, secrets,
  audit, multi-tenancy et validations humaines.
- Relier observabilité, evals et coût dans une boucle d'amélioration continue.
- Préparer haute disponibilité, disaster recovery et runbooks d'exploitation.

## ✅ Prérequis

- Chapitre 11 (PR Factory v1.1 : demande -> plan -> code -> tests -> review -> PR).
- Savoir lire une trace de run, un résultat d'eval, une policy et une matrice de routing.
- Durée estimée : **3 h** (1 h 15 théorie + 45 min atelier architecture + 45 min
  exercices + 15 min synthèse finale).

## 🚪 Gate final du parcours

> **Gate 5 (final)** : tu dois pouvoir expliquer comment une demande devient une PR puis
> une décision de déploiement, avec pour chaque étape : propriétaire, budget, droits,
> trace, eval, coût, point de reprise et critère d'arrêt.

## 🧭 Parcours pas à pas

| Étape | Support | Ce que tu fais |
| ----- | ------- | --------------- |
| 1 | [`slides/01-architecture-plateforme.md`](slides/01-architecture-plateforme.md) | Lire : passer d'une PR Factory à une plateforme |
| 2 | [`slides/02-scalabilite-resilience.md`](slides/02-scalabilite-resilience.md) | Lire : queues, workers, retries et backpressure |
| 3 | [`slides/03-securite-gouvernance.md`](slides/03-securite-gouvernance.md) | Lire : identités, tenants, secrets, audit et RBAC |
| 4 | [`slides/04-observabilite-evals-cout.md`](slides/04-observabilite-evals-cout.md) | Lire : piloter qualité, fiabilité et coût ensemble |
| 5 | [`slides/05-disaster-recovery-exploitation.md`](slides/05-disaster-recovery-exploitation.md) | Lire : HA, DR, runbooks et change management |
| 6 | [`demos/README.md`](demos/README.md) | Examiner : trois scénarios de production commentés |
| 7 | [`exercices/README.md`](exercices/README.md) | Faire les exercices -> **Factory v2.0** |
| 8 | [`solutions/README.md`](solutions/README.md) | Comparer après tentative |

## 📚 Plan théorique

1. Frontière produit : ce qu'une plateforme promet, et ce qu'elle refuse d'automatiser.
1. Architecture cible : gateway, runtime, orchestration, tools, modèles, policies, evals.
1. Scalabilité : files, workers, quotas, idempotence, backpressure, isolation par tenant.
1. Résilience : retries sûrs, fallback modèle, reprise de workflow, dégradation contrôlée.
1. Sécurité : moindre privilège, secrets, sandbox, RBAC, audit, supply chain et approval.
1. Observabilité : traces, métriques, logs, SLO, alertes, dashboards et postmortems.
1. Evals en production : jeux de régression, canary, shadow runs, seuils et rollback.
1. Coût : budgets, attribution par équipe, coût par PR utile, capacity planning.
1. Disaster recovery : RTO, RPO, sauvegardes, restauration, drills et runbooks.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : l'architecture décrit des responsabilités et des contrats, pas
  un orchestrateur imposé.
- **Model-agnostic** : les agents ne ciblent jamais un fournisseur ; ils demandent des
  capacités au Model Gateway et acceptent le failover contrôlé.
- **Eval-first** : aucune automatisation de production ne progresse sans mesure de qualité,
  seuil de régression et trace exploitable.

## 🏗️ Architecture cible

```text
User / Ticket / Webhook
        │
        ▼
Agent Gateway ── authn / tenant / quota / request_id
        │
        ▼
Orchestrator ── workflow state / retries / checkpoints
        │
        ├── Agent Runtime ── sandbox / tools / budgets / termination
        │        │
        │        ├── MCP Gateway ── Git / CI / issue tracker / artifacts
        │        └── Model Gateway ── local / cloud / fallback / policy labels
        │
        ├── Policy Engine ── auto / human / deny
        ├── Eval Service ── quality / security / regression / canary
        ├── Observability ── traces / metrics / logs / audit
        └── Cost Control ── budget / attribution / forecast
```

La plateforme n'est pas « un gros agent ». C'est un système qui rend plusieurs agents
**bornés, observables, gouvernés et réparables**.

## 🧩 Contrats de production minimaux

| Contrat | Question à laquelle il répond | Échec si absent |
| ------- | ----------------------------- | --------------- |
| `request_id` | Quelle demande suit-on de bout en bout ? | impossible de diagnostiquer |
| `tenant_id` | Qui consomme le service et paie le coût ? | quotas et audit flous |
| `workflow_state` | Où reprendre après crash ? | relance complète ou doublon |
| `budget` | Quand arrêter automatiquement ? | coût et latence non bornés |
| `policy_decision` | Qui autorise l'action ? | privilège implicite |
| `eval_result` | Pourquoi croire que la sortie est meilleure ? | qualité affirmée, pas prouvée |
| `trace_id` | Où est la preuve de chaque décision ? | postmortem impossible |
| `rollback_plan` | Comment revenir en arrière ? | incident prolongé |

## 🛡️ Niveau d'autonomie accepté

La Factory v2.0 automatise seulement ce qui est mesuré et gouverné.

| Action | Décision par défaut | Raison |
| ------ | ------------------- | ------ |
| Lire un dépôt autorisé | `auto` | faible risque, audit obligatoire |
| Modifier une branche agent | `auto` | isolé de `main`, budgeté, traçable |
| Ouvrir une PR | `auto` | visible, réversible, contrôlé par CI |
| Merger vers `main` | `human` | impact durable sur la base commune |
| Déployer en production | `human` ou `deny` | dépend du risque, des SLO et des evals |
| Accéder à un secret brut | `deny` | utiliser des capacités déléguées, jamais exposer le secret |

## 📦 Livrable

**Factory v2.0** est un dossier de conception opérationnelle contenant :

- une carte d'architecture et des responsabilités par composant ;
- un contrat d'entrée/sortie pour les demandes agentiques ;
- une stratégie de scaling, quotas, queues, idempotence et retries ;
- une matrice sécurité/RBAC/audit et une séparation des identités ;
- des SLO et métriques de production ;
- une boucle evals -> canary -> rollback ;
- un modèle de coût par tenant et par PR utile ;
- un runbook incident + disaster recovery avec RTO/RPO.

## ⚙️ Installation

Aucune installation supplémentaire. Ce chapitre est un chapitre de synthèse et de design
opérationnel : il manipule des matrices, contrats et runbooks. Aucun package ni commande
n'est requis.

## 🔗 Ressources

- [`../06-token-engineering-routing/`](../06-token-engineering-routing/) - budgets,
  routing et coût par succès.
- [`../07-observability-tracing/`](../07-observability-tracing/) - traces et attribution.
- [`../08-evaluation-engineering/`](../08-evaluation-engineering/) - evals et seuils de
  régression.
- [`../09-security-governance/`](../09-security-governance/) - Policy Engine et sécurité.
- [`../11-pr-factory/`](../11-pr-factory/) - PR Factory v1.1, point de départ du chapitre.

## 📝 Auto-évaluation

Tu as terminé le parcours quand tu réponds sans hésiter :

1. Pourquoi une plateforme agentique n'est-elle pas seulement un agent plus puissant ?
1. Où places-tu la frontière entre Orchestrator, Agent Runtime et Policy Engine ?
1. Quelle différence fais-tu entre retry, fallback, reprise de workflow et rollback ?
1. Quelles données faut-il conserver pour auditer une PR générée automatiquement ?
1. Quel SLO surveillerais-tu en premier : latence, coût, taux de succès ou qualité ?
1. Que se passe-t-il si le fournisseur LLM principal est indisponible pendant 2 heures ?
1. Quelle action reste humaine même si les evals sont vertes, et pourquoi ?
