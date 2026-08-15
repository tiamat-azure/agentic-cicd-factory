# 🏗️ Solution 1 - Blueprint de plateforme

## 🧭 Diagramme cible

```text
User / Ticket / Webhook
        │
        ▼
Agent Gateway ── request_id / tenant_id / quota
        │
        ▼
Orchestrator ── workflow_id / checkpoints / queue
        │
        ├── Agent Runtime ── sandbox / budget / termination
        │        ├── MCP Gateway ── tools autorisés / audit
        │        └── Model Gateway ── profils modèles / failover
        │
        ├── Policy Engine ── auto / human / deny
        ├── Eval Service ── qualité / sécurité / régression
        ├── Observability ── trace_id / métriques / logs
        └── Cost Control ── budget / attribution / forecast
```

## 🧱 Responsabilités

| Composant | Responsabilité |
| --------- | -------------- |
| Agent Gateway | crée la demande canonique, authentifie et applique les quotas d'entrée |
| Orchestrator | pilote l'état durable du workflow et reprend après incident |
| Agent Runtime | exécute les agents avec sandbox, budgets et terminaison explicite |
| MCP Gateway | expose les tools sous contrat, avec audit et permissions |
| Model Gateway | route vers des profils de modèles et gère le failover |
| Policy Engine | transforme contexte + droits + evals en décision explicable |
| Eval Service | exécute les jeux de qualité, sécurité et non-régression |
| Observability | corrèle toutes les décisions avec traces, métriques et logs |
| Cost Control | attribue les coûts et déclenche budgets ou backpressure |

## 🔌 Contrats échangés

| Contrat | Producteur | Consommateurs |
| ------- | ---------- | ------------- |
| `request_id` | Agent Gateway | tous les composants |
| `tenant_id` | Agent Gateway | quotas, cost, audit, policy |
| `workflow_id` | Orchestrator | runtime, evals, observability |
| `budget` | Cost Control + policy | runtime, model gateway, orchestrator |
| `policy_decision` | Policy Engine | orchestrator, audit, UI |
| `trace_id` | Observability | tous les spans et artefacts |
| `eval_result` | Eval Service | policy, CI/CD, dashboards |

## ⚠️ Frontières de risque

| Frontière | Risque | Protection |
| --------- | ------ | ---------- |
| Agent -> modèle | dépendance fournisseur, coût non borné | Model Gateway + budgets + failover |
| Agent -> tools | accès trop large au monde réel | MCP Gateway + RBAC + audit |
| Workflow -> action durable | doublon, merge ou déploiement non voulu | checkpoints + idempotence + policy |

## 🧠 Justification

L'agent ne parle pas directement au fournisseur LLM ni aux tools internes parce que ces
dépendances portent les risques de coût, de sécurité, d'audit et de disponibilité. Les
gateways transforment ces risques en contrats observables et gouvernables.
